# -*- coding: utf-8 -*-
"""
Batch download PDFs listed in README.md (direct DOI parsing only).

- Parse '## 📂 Research Domains Covered' in README.md
- Extract [*(paper)*](https://doi.org/...) lines under each "### N. Section"
- Resolve publisher-specific PDF URLs (Nature, ACS, Wiley, Springer, Elsevier, etc.)
- Save to downloaded_papers/<section>/<YEAR>_<JOURNAL>_<TITLE>.pdf
- Concurrent downloads, retry, and CSV reports (failures appended row-by-row)

Usage:
  python download.py
  python download.py --workers 6
"""

import re
import csv
import time
import argparse
import logging
import threading
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup
from slugify import slugify


# ------------------------- Config & Regex -------------------------

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/pdf,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
TIMEOUT: Tuple[int, int] = (8, 240)
RETRY = 2
SLEEP_BETWEEN = 0.6

SEC_RE = re.compile(r"^###\s*(\d+)\.\s*(.+?)\s*$")
# match ANY markdown link whose href contains doi.org (case-insensitive), not just "[*(paper)*]"
DOI_RE = re.compile(r"\[[^\]]*\]\((https?://(?:dx\.)?doi\.org/[^\s)]+)\)", re.IGNORECASE)



# ------------------------- Small helpers -------------------------

def is_pdf_response(resp: requests.Response) -> bool:
    """Return True if response looks like a PDF."""
    ctype = (resp.headers.get("Content-Type") or "").lower()
    disp = (resp.headers.get("Content-Disposition") or "").lower()
    return ("application/pdf" in ctype) or ("attachment" in disp and ".pdf" in disp)


def clean_slug(text: str, max_len: int = 110) -> str:
    """Return filesystem-safe slug while keeping CJK."""
    s = text.replace(":", " ").replace("/", " ")
    return slugify(s, lowercase=False, max_length=max_len, word_boundary=True,
                   regex_pattern=r"[^-\w\s\u4e00-\u9fff]") or "paper"


def prepare_folder(folder: Path) -> None:
    """Create folder if not exists."""
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)


def handle_existing_pdf(pdf_path: Path, overwrite: bool = False) -> bool:
    """Return True if should skip because file exists and not overwriting."""
    if pdf_path.exists():
        if overwrite:
            pdf_path.unlink(missing_ok=True)
            return False
        logging.info(f"SKIP  already exists: {pdf_path.name}")
        return True
    return False


def extract_title_from_citation(line: str) -> str:
    """Extract title between first post-author period and the period before first italic segment."""
    m = re.search(r"\.\s+(?P<title>.+?)\.\s*\*", line)
    if m:
        return m.group("title").strip()
    parts = [p.strip() for p in line.split(".")]
    return parts[1] if len(parts) >= 3 else ""


def filename_from_citation(line: str, doi: str) -> str:
    """Build filename as YEAR_JOURNAL_TITLE.pdf."""
    year = ""
    m_year = re.search(r"\((\d{4})\)", line)
    if m_year:
        year = m_year.group(1).strip()
    journal = ""
    m_j = re.search(r"\*([^\*]+)\*", line)
    if m_j:
        journal = m_j.group(1).strip()
    title = extract_title_from_citation(line)
    base = "_".join(x for x in (year, journal, title) if x) or doi.replace("/", "_")
    return f"{clean_slug(base)}.pdf"


# ------------------------- Publisher-related -------------------------

def extract_pii_from_html(html: str) -> Optional[str]:
    """Try to extract ScienceDirect PII from landing HTML."""
    try:
        soup = BeautifulSoup(html, "html.parser")
        m = soup.find("meta", attrs={"name": "citation_pii"})
        if m and m.get("content"):
            return m["content"].strip()
        text = soup.get_text(" ", strip=True)
        m2 = re.search(r"\bpii[:\s]+([A-Za-z0-9\.]+)\b", text)
        if m2:
            return m2.group(1).strip()
    except Exception:
        pass
    return None


def probe_pdf_head(url: str, session: requests.Session, referer: Optional[str] = None) -> bool:
    """Quickly test a candidate URL with HEAD then small GET."""
    hdrs = dict(HEADERS)
    if referer:
        hdrs["Referer"] = referer
    try:
        r = session.head(url, headers=hdrs, timeout=TIMEOUT, allow_redirects=True, verify=False)
        if r.status_code == 200 and is_pdf_response(r):
            return True
    except Exception:
        pass
    try:
        r = session.get(url, headers=hdrs, timeout=TIMEOUT, allow_redirects=True, stream=True, verify=False)
        return r.status_code == 200 and is_pdf_response(r)
    except Exception:
        return False


def build_pdf_candidates(doi: str, landing_url: str, landing_html: str) -> List[str]:
    """Return ordered candidate PDF URLs per publisher; deduplicated."""
    cands: List[str] = []
    host = requests.utils.urlparse(landing_url).netloc.lower()

    # Nature / npj / Nat. Commun.
    if doi.startswith("10.1038/") or "nature.com" in host:
        art_id = doi.split("/")[-1]
        cands += [f"https://www.nature.com/articles/{art_id}.pdf"]

    # ACS
    if doi.startswith("10.1021/") or "pubs.acs.org" in host:
        cands += [
            f"https://pubs.acs.org/doi/pdfdirect/{doi}?download=true",
            f"https://pubs.acs.org/doi/pdf/{doi}",
        ]

    # Wiley
    if doi.startswith("10.1002/") or "onlinelibrary.wiley.com" in host:
        base = "https://onlinelibrary.wiley.com/doi"
        cands += [
            f"{base}/epdf/{doi}",
            f"{base}/pdf/{doi}",
            f"{base}/pdfdirect/{doi}?download=true",
        ]

    # Optica / OSA
    if doi.startswith("10.1364/") or "opg.optica.org" in host or "osapublishing.org" in host:
        cands += [f"https://opg.optica.org/DirectPDFAccess/{doi}?download=true"]

    # De Gruyter
    if doi.startswith("10.1515/") or "degruyter" in host:
        cands += [
            f"https://www.degruyter.com/document/doi/{doi}/pdf",
            f"https://www.degruyterbrill.com/document/doi/{doi}/pdf",
            f"https://www.degruyter.com/document/doi/{doi}/pdf?download=true",
        ]

    # SpringerLink
    if doi.startswith("10.1007/") or "link.springer.com" in host:
        cands += [f"https://link.springer.com/content/pdf/{doi}.pdf"]

    # Elsevier / ScienceDirect
    if doi.startswith("10.1016/") or "sciencedirect.com" in host:
        pii = extract_pii_from_html(landing_html) or doi.split("/")[-1]
        if pii:
            cands += [
                f"https://www.sciencedirect.com/science/article/pii/{pii}/pdf",
                f"https://www.sciencedirect.com/science/article/pii/{pii}/pdfft?download=true",
            ]

    # AIP
    if doi.startswith("10.1063/") or "aip.scitation.org" in host:
        cands += [f"https://aip.scitation.org/doi/pdf/{doi}"]

    # IOP
    if doi.startswith("10.1088/") or "iopscience.iop.org" in host:
        cands += [f"https://iopscience.iop.org/article/{doi}/pdf"]

    # IEEE
    if doi.startswith("10.1109/") or "ieeexplore.ieee.org" in host:
        m = re.search(r"/document/(\d+)/", landing_url) or re.search(r"[?&]arnumber=(\d+)", landing_url)
        if m:
            ar = m.group(1)
            cands += [f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={ar}"]

    # MDPI
    if doi.startswith("10.3390/") or "mdpi.com" in host:
        cands += [
            f"https://www.mdpi.com/{doi}/pdf?download=true",
            f"https://www.mdpi.com/{doi}/pdf",
        ]

    # RSC (fallbacks; often meta has citation_pdf_url)
    if doi.startswith("10.1039/") or "pubs.rsc.org" in host:
        cands += [
            f"https://pubs.rsc.org/en/content/articlepdf/{doi}",
            f"https://pubs.rsc.org/en/content/articlelanding/{doi}",
        ]

    # Taylor & Francis
    if doi.startswith("10.1080/") or "tandfonline.com" in host:
        cands += [
            f"https://www.tandfonline.com/doi/pdf/{doi}?needAccess=true",
            f"https://www.tandfonline.com/doi/pdf/{doi}",
        ]

    seen, out = set(), []
    for u in cands:
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def find_pdf_in_html(base_url: str, html: str) -> Optional[str]:
    """Search landing HTML for a PDF link via meta/link/anchors."""
    soup = BeautifulSoup(html, "html.parser")
    host = requests.utils.urlparse(base_url).netloc.lower()

    m = soup.find("meta", attrs={"name": "citation_pdf_url"})
    if m and m.get("content"):
        return requests.compat.urljoin(base_url, m["content"].strip())

    for link in soup.find_all("link", href=True):
        rels = [x.lower() for x in (link.get("rel") or [])]
        typ = (link.get("type") or "").lower()
        if ("alternate" in rels) and ("application/pdf" in typ):
            return requests.compat.urljoin(base_url, link["href"].strip())

    cands: List[str] = []

    if "onlinelibrary.wiley.com" in host:
        a1 = soup.find("a", attrs={"data-test": "pdf-link"}) or soup.find("a", attrs={"data-type": "pdf"})
        if a1 and a1.get("href"):
            cands.append(a1.get("href").strip())
        a2 = soup.find("a", id="pdfLink")
        if a2 and a2.get("href"):
            cands.append(a2.get("href").strip())
        ifr = soup.find("iframe", id="pdfDocument") or soup.find("iframe", attrs={"name": "pdfPreview"})
        if ifr and ifr.get("src"):
            cands.append(ifr.get("src").strip())
        for a in soup.find_all("a", href=True):
            h = a["href"]
            if "/doi/epdf/" in h or "/doi/pdf/" in h or "/doi/pdfdirect/" in h:
                cands.append(h.strip())

    if "opg.optica.org" in host or "osapublishing.org" in host:
        for a in soup.find_all("a", href=True):
            if "DirectPDFAccess" in a["href"]:
                cands.append(a["href"].strip())

    if "degruyter" in host:
        for a in soup.find_all("a", href=True):
            h = a["href"]
            if "/document/doi/" in h and "/pdf" in h:
                cands.append(h.strip())

    if "sciencedirect.com" in host:
        for a in soup.find_all("a", href=True):
            h = a["href"]
            if "/science/article/pii/" in h and ("/pdf" in h or "/pdfft" in h):
                cands.append(h.strip())

    if "link.springer.com" in host:
        for a in soup.find_all("a", href=True):
            h = a["href"]
            if "/content/pdf/" in h and h.lower().endswith(".pdf"):
                cands.append(h.strip())

    if cands:
        return requests.compat.urljoin(base_url, cands[0])

    m2 = re.search(r'https?://[^\s"\']+?\.pdf(?:\?[^\s"\']*)?', html, flags=re.IGNORECASE)
    if m2:
        return m2.group(0)

    if "link.springer.com" in host:
        m3 = re.search(r'name=["\']citation_doi["\']\s+content=["\']([^"\']+)["\']', html)
        if m3:
            doi = m3.group(1).strip()
            return f"https://link.springer.com/content/pdf/{doi}.pdf"

    return None


# ------------------------- Download one item -------------------------

def download_pdf(pdf_url: str, dest: Path, session: requests.Session, referer: Optional[str]) -> bool:
    """Download a PDF to dest; return True on success."""
    hdrs = dict(HEADERS)
    if referer:
        hdrs["Referer"] = referer
    for attempt in range(1, RETRY + 1):
        try:
            with session.get(pdf_url, headers=hdrs, timeout=TIMEOUT, stream=True, allow_redirects=True, verify=False) as r:
                if r.status_code == 200 and is_pdf_response(r):
                    tmp = dest.with_suffix(dest.suffix + ".part")
                    with open(tmp, "wb") as f:
                        for chunk in r.iter_content(8192):
                            if chunk:
                                f.write(chunk)
                    tmp.replace(dest)
                    return True
                return False
        except Exception as e:
            logging.warning(f"Download error ({attempt}/{RETRY}) {pdf_url} | {e!r}")
            time.sleep(SLEEP_BETWEEN * attempt)
    return False


def process_entry(section: str, line: str, out_root: Path, session: requests.Session
                  ) -> Tuple[str, str, str, str, str]:
    """Process one citation line; return (status, section, title, doi_url, info)."""
    m = DOI_RE.search(line)
    if not m:
        return ("FAIL", section, "", "", "No DOI link found in line")

    doi_url = m.group(1).strip()
    title = extract_title_from_citation(line)
    logging.info(f"START {doi_url} | section='{section}' | title='{title}'")

    doi = doi_url.split("doi.org/")[-1]
    filename = filename_from_citation(line, doi)
    save_dir = out_root / section
    prepare_folder(save_dir)
    dest = save_dir / filename

    if handle_existing_pdf(dest, overwrite=False):
        return ("OK", section, title, doi_url, str(dest))

    try:
        landing = session.get(doi_url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True, verify=False)
    except Exception as exc:
        return ("FAIL", section, title, doi_url, f"Landing request error: {exc!r}")

    landing_url = landing.url
    landing_html = landing.text

    candidates = build_pdf_candidates(doi, landing_url, landing_html)
    pdf_url: Optional[str] = None
    for cand in candidates:
        if probe_pdf_head(cand, session, referer=landing_url):
            pdf_url = cand
            break
    if not pdf_url:
        pdf_url = find_pdf_in_html(landing_url, landing_html)

    if not pdf_url:
        return ("FAIL", section, title, doi_url, "No PDF link found (may require institutional access)")

    ok = download_pdf(pdf_url, dest, session, referer=landing_url)
    if ok:
        logging.info(f"[OK]   {doi_url} -> {dest}")
        return ("OK", section, title, doi_url, str(dest))

    fb = save_dir / (doi.replace("/", "_") + ".pdf")
    if not dest.exists():
        if download_pdf(pdf_url, fb, session, referer=landing_url):
            logging.info(f"[OK]   {doi_url} -> {fb} (fallback)")
            return ("OK", section, title, doi_url, str(fb))

    return ("FAIL", section, title, doi_url, f"Download failed: {pdf_url}")


# ------------------------- README parsing -------------------------

def parse_readme_sections(readme_path: Path) -> Dict[str, List[str]]:
    """
    Extract {section: [citation lines]} from the 'Research Domains Covered' block.
    Robust to blank lines, indentation, emoji prefixes, and minor wording variants.
    If the block cannot be found or yields no matches, fall back to scanning the entire README.
    """
    lines = readme_path.read_text(encoding="utf-8", errors="ignore").splitlines()

    # --- locate block start (tolerant to emoji / spacing / case) ---
    start = None
    for i, raw in enumerate(lines):
        norm = raw.strip()
        low = norm.lower()
        # prefer a line that has the emoji + "research"
        if ("📂" in norm and "research" in low):
            start = i
            break
        # or any H2 whose text contains "research domains covered"
        if low.startswith("##") and "research" in low and "domain" in low:
            start = i
            break

    # --- locate block end: next H2 (allow leading spaces) ---
    end = None
    if start is not None:
        for j in range(start + 1, len(lines)):
            if lines[j].lstrip().startswith("## "):
                end = j
                break

    def _scan(target_lines: List[str]) -> Dict[str, List[str]]:
        sections: Dict[str, List[str]] = {}
        current: Optional[str] = None
        for raw in target_lines:
            line = raw.rstrip()
            m = SEC_RE.match(line)  # ### 1. Section Title
            if m:
                current = f"{m.group(1)}. {m.group(2).strip()}"
                sections.setdefault(current, [])
                continue
            if DOI_RE.search(line):
                # if DOI appears before any ### section, drop it into 'Uncategorized'
                key = current or "Uncategorized"
                sections.setdefault(key, []).append(line)
        return sections

    sections: Dict[str, List[str]] = {}
    if start is not None:
        target = lines[start:end] if end is not None else lines[start:]
        sections = _scan(target)

    # --- fallback: if block not found or no DOI matched, scan whole README ---
    if not sections or all(len(v) == 0 for v in sections.values()):
        sections = _scan(lines)

    # strip empty sections
    sections = {k: v for k, v in sections.items() if v}
    return sections


# ------------------------- Main -------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch download PDFs from README.md (direct DOI parsing only).")
    parser.add_argument("--readme", type=str,
                        default=str(Path(__file__).resolve().parent.parent / "README.md"),
                        help="Path to README.md (default: ../README.md)")
    parser.add_argument("--outdir", type=str, default="downloaded_papers",
                        help="Output directory (default: downloaded_papers)")
    parser.add_argument("--workers", type=int, default=6,
                        help="Number of concurrent workers (default: 6)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

    readme_path = Path(args.readme).resolve()
    out_root = Path(args.outdir).resolve()
    prepare_folder(out_root)

    reports_dir = out_root / "_reports"
    prepare_folder(reports_dir)
    failures_csv = reports_dir / "failures.csv"

    # ensure header for failures CSV
    if not failures_csv.exists():
        with failures_csv.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["section", "title", "url"])
    fail_lock = threading.Lock()

    if not readme_path.exists():
        logging.error("README not found: %s", readme_path)
        return

    sec_map = parse_readme_sections(readme_path)
    total = sum(len(v) for v in sec_map.values())
    if total == 0:
        logging.warning("No [*(paper)*](https://doi.org/...) lines found under the 'Research Domains Covered' block.")
        return

    logging.info("Found %d sections, %d entries.", len(sec_map), total)
    requests.packages.urllib3.disable_warnings()

    ok_cnt = 0
    fail_cnt = 0

    with requests.Session() as session:
        session.trust_env = False  # ignore system proxies by default

        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = [pool.submit(process_entry, sec, line, out_root, session)
                       for sec, lines in sec_map.items() for line in lines]

            for fut in as_completed(futures):
                status, section, title, doi_url, info = fut.result()
                if status == "OK":
                    ok_cnt += 1
                    logging.info(f"[OK]   {doi_url} | {info}")
                else:
                    fail_cnt += 1
                    logging.info(f"[FAIL] {doi_url} | {info}")
                    # append one failure row immediately
                    with fail_lock:
                        with failures_csv.open("a", newline="", encoding="utf-8-sig") as f:
                            csv.writer(f).writerow([section, title, doi_url])

    logging.info("==== SUMMARY ====")
    logging.info("Success: %d | Failures: %d", ok_cnt, fail_cnt)
    logging.info("Failures CSV: %s (columns: section,title,url)", failures_csv)
    logging.info("Done.")


if __name__ == "__main__":
    main()
