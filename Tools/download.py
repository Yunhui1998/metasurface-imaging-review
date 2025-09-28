# tools/download_from_readme.py
# -*- coding: utf-8 -*-
"""
Batch download PDFs listed in README.md (designed for your current structure):
- Parse sections like "### 1. Chromatic Aberration Correction"
- Extract [*(paper)*](https://doi.org/...) links
- Try Unpaywall (if --email provided) for OA PDFs; otherwise follow DOI and
  detect PDF via headers/meta/links
- Save PDFs under downloaded_papers/<section_name>/ with normalized filenames
- Concurrent downloads (threads), retry, and CSV reports for success/failure

Usage examples:
  python tools/download_from_readme.py
  python tools/download_from_readme.py --workers 8 --email you@example.com

Dependencies:
  pip install requests beautifulsoup4 python-slugify
"""

import re
import csv
import time
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup
from slugify import slugify


# ------------------------- Config & Regex -------------------------

HEADERS = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 25
RETRY = 2
SLEEP_BETWEEN = 0.6  # small polite delay between network calls (per task)

SEC_RE = re.compile(r"^###\s+(\d+)\.\s+(.*)\s*$")
DOI_RE = re.compile(r"\[\*\(paper\)\*\]\((https?://doi\.org/[^\)]+)\)", re.IGNORECASE)

# ------------------------- Helpers -------------------------

def is_pdf_response(resp: requests.Response) -> bool:
    """Return True if the HTTP response likely contains a PDF."""
    ctype = (resp.headers.get("Content-Type") or "").lower()
    disp = (resp.headers.get("Content-Disposition") or "").lower()
    if "application/pdf" in ctype:
        return True
    if "attachment" in disp and ".pdf" in disp:
        return True
    return False


def clean_slug(s: str, max_len: int = 110) -> str:
    """Make a safe filename slug, keeping CJK and word boundaries."""
    s = s.replace(":", " ").replace("/", " ")
    return slugify(
        s,
        lowercase=False,
        max_length=max_len,
        word_boundary=True,
        regex_pattern=r"[^-\w\s\u4e00-\u9fff]"
    ) or "paper"


def filename_from_citation(line: str, doi: str) -> str:
    """
    Derive filename as: YEAR_JOURNALABBR_TITLE.pdf
    - YEAR: (YYYY) in the line
    - JOURNALABBR: the first italic segment *...*
    - TITLE: the text between the period after authors and the period before the first italic *...*
    """
    # Year
    year = ""
    ym = re.search(r"\((\d{4})\)", line)
    if ym:
        year = ym.group(1).strip()

    # Journal abbreviation (between *...*)
    journal = ""
    jm = re.search(r"\*([^\*]+)\*", line)
    if jm:
        journal = jm.group(1).strip()

    # Title: between ". " (after authors) and ". *" (before italic journal)
    # This is robust against dots in initials (e.g., "J.") and "et al."
    title = ""
    tm = re.search(r"\.\s+(?P<title>.+?)\.\s*\*", line)
    if tm:
        title = tm.group("title").strip()
    else:
        # Fallback: classic heuristic (author. Title. *Journal* ...)
        parts = [p.strip() for p in line.split(".")]
        if len(parts) >= 3:
            title = parts[1]

    # Build filename: YEAR_JOURNALABBR_TITLE.pdf
    pieces = [x for x in (year, journal, title) if x]
    base = "_".join(pieces) if pieces else doi.replace("/", "_")
    return f"{clean_slug(base)}.pdf"


def build_pdf_candidates(doi: str, landing_url: str, landing_html: str) -> List[str]:
    """
    Return candidate PDF URLs by publisher rules, based on DOI prefix and landing host.
    Order matters; first successful probe wins.
    """
    cands: List[str] = []
    host = requests.utils.urlparse(landing_url).netloc.lower()

    # Nature / npj / Nature Communications
    if doi.startswith("10.1038/"):
        art_id = doi.split("/")[-1]
        cands += [f"https://www.nature.com/articles/{art_id}.pdf"]

    # ACS
    if doi.startswith("10.1021/") or "pubs.acs.org" in host:
        cands += [
            f"https://pubs.acs.org/doi/pdf/{doi}",
            f"https://pubs.acs.org/doi/pdfdirect/{doi}?download=true",
        ]

    # Wiley
    if doi.startswith("10.1002/") or "onlinelibrary.wiley.com" in host:
        cands += [
            f"https://onlinelibrary.wiley.com/doi/pdf/{doi}",
            f"https://onlinelibrary.wiley.com/doi/pdfdirect/{doi}",
        ]

    # Optica/OSA
    if doi.startswith("10.1364/") or "opg.optica.org" in host:
        cands += [f"https://opg.optica.org/DirectPDFAccess/{doi}?download=true"]

    # De Gruyter
    if doi.startswith("10.1515/") or "degruyter" in host:
        cands += [
            f"https://www.degruyter.com/document/doi/{doi}/pdf",
            f"https://www.degruyterbrill.com/document/doi/{doi}/pdf",
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

    # Deduplicate while preserving order
    seen, uniq = set(), []
    for u in cands:
        if u and u not in seen:
            seen.add(u); uniq.append(u)
    return uniq


def extract_pii_from_html(html: str) -> Optional[str]:
    """
    Try to extract ScienceDirect PII from landing HTML.
    """
    try:
        soup = BeautifulSoup(html, "html.parser")
        m = soup.find("meta", attrs={"name": "citation_pii"})
        if m and m.get("content"):
            return m["content"].strip()
        txt = soup.get_text(" ", strip=True)
        m2 = re.search(r"\bpii[:\s]+([A-Za-z0-9\.]+)\b", txt)
        if m2:
            return m2.group(1).strip()
    except Exception:
        pass
    return None


def probe_pdf_head(url: str, session: requests.Session, referer: Optional[str] = None) -> bool:
    """
    Quick probe: try HEAD then tiny GET to see if the URL is a PDF,
    carrying Referer to satisfy publisher checks.
    """
    hdrs = dict(HEADERS)
    if referer:
        hdrs["Referer"] = referer

    try:
        r = session.head(url, headers=hdrs, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code == 200 and is_pdf_response(r):
            return True
    except Exception:
        pass

    try:
        r = session.get(url, headers=hdrs, timeout=TIMEOUT, allow_redirects=True, stream=True)
        return r.status_code == 200 and is_pdf_response(r)
    except Exception:
        return False




def parse_readme_sections(readme_path: Path) -> Dict[str, List[str]]:
    """
    Parse README.md and return:
      { "1. Chromatic Aberration Correction": [full_citation_line, ...], ... }
    Only lines containing [*(paper)*](https://doi.org/...) are kept.
    """
    sections: Dict[str, List[str]] = {}
    current = None
    for raw in readme_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = SEC_RE.match(raw)
        if m:
            current = f"{m.group(1)}. {m.group(2).strip()}"
            sections.setdefault(current, [])
            continue
        if current and DOI_RE.search(raw):
            sections[current].append(raw.strip())
    return sections


def unpaywall_pdf(doi: str, email: Optional[str], session: requests.Session) -> Optional[str]:
    """
    Query Unpaywall for an OA PDF if email provided; otherwise return None.
    """
    if not email:
        return None
    try:
        url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
        r = session.get(url, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        data = r.json()
        loc = data.get("best_oa_location") or {}
        for key in ("url_for_pdf", "url"):
            val = loc.get(key)
            if val and val.lower().endswith(".pdf"):
                return val
        for x in data.get("oa_locations", []):
            for key in ("url_for_pdf", "url"):
                val = x.get(key)
                if val and val.lower().endswith(".pdf"):
                    return val
        return None
    except Exception:
        return None


def find_pdf_in_html(base_url: str, html: str) -> Optional[str]:
    """
    Parse publisher page HTML to find a PDF URL via common hints.
    """
    soup = BeautifulSoup(html, "html.parser")

    # <meta name="citation_pdf_url" content="...">
    meta = soup.find("meta", attrs={"name": "citation_pdf_url"})
    if meta and meta.get("content"):
        return meta["content"]

    # <link rel="alternate" type="application/pdf" href="...">
    for link in soup.find_all("link", href=True):
        if (link.get("rel") and "alternate" in [x.lower() for x in link.get("rel")]) and \
           (link.get("type") and "application/pdf" in link.get("type").lower()):
            return requests.compat.urljoin(base_url, link["href"])

    # Any <a> that has ".pdf"
    anchors = soup.find_all("a", href=True)
    for a in anchors:
        href = a["href"]
        if ".pdf" in href.lower():
            return requests.compat.urljoin(base_url, href)

    return None


def follow_doi_for_pdf(doi_url: str, session: requests.Session) -> Optional[str]:
    """
    Resolve DOI to landing page (keep cookies), try publisher-specific candidates
    with Referer, then fall back to parsing HTML.
    """
    try:
        # Resolve landing page (keep session/cookies)
        r = session.get(doi_url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        landing_url = r.url
        landing_html = r.text

        if r.status_code == 200 and is_pdf_response(r):
            return r.url

        doi = doi_url.split("doi.org/")[-1]
        candidates = build_pdf_candidates(doi, landing_url, landing_html)

        # Try candidates with Referer
        for pdf_url in candidates:
            if probe_pdf_head(pdf_url, session, referer=landing_url):
                return pdf_url

        # Fallback: parse HTML for meta/link/a
        return find_pdf_in_html(landing_url, landing_html)

    except Exception as e:
        logging.warning(f"DOI follow failed: {doi_url} | {e}")
        return None



def download_pdf(pdf_url: str, dest: Path, session: requests.Session, referer: Optional[str] = None) -> bool:
    """
    Stream download only if the response is a PDF. Carry Referer to satisfy checks.
    """
    hdrs = dict(HEADERS)
    if referer:
        hdrs["Referer"] = referer

    for attempt in range(1, RETRY + 1):
        try:
            with session.get(pdf_url, headers=hdrs, timeout=TIMEOUT, stream=True, allow_redirects=True) as r:
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
            logging.warning(f"Download error ({attempt}/{RETRY}) {pdf_url} | {e}")
            time.sleep(SLEEP_BETWEEN * attempt)
    return False



# ------------------------- Worker Task -------------------------

def process_entry(section: str, line: str, out_root: Path, email: Optional[str], session: requests.Session) -> Tuple[str, str, str, str]:
    """
    Return a tuple report:
      (status, section, doi_url, saved_path or reason)
    status: "OK" or "FAIL"
    """
    doi_url = DOI_RE.search(line).group(1).strip()
    doi = doi_url.split("doi.org/")[-1]
    filename = filename_from_citation(line, doi)

    save_dir = out_root / section
    save_dir.mkdir(parents=True, exist_ok=True)
    dest = save_dir / filename

    # Skip if already exists
    if dest.exists() and dest.stat().st_size > 0:
        return ("OK", section, doi_url, str(dest))

    # 1) Unpaywall
    pdf_url = unpaywall_pdf(doi, email, session) if email else None

    # 2) DOI follow
    # 2) DOI follow with landing page + Referer
    landing_res = session.get(doi_url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
    landing_url = landing_res.url
    landing_html = landing_res.text

    if not pdf_url:
        # reuse the same logic as follow_doi_for_pdf but we already have landing page
        doi = doi_url.split("doi.org/")[-1]
        candidates = build_pdf_candidates(doi, landing_url, landing_html)
        for cand in candidates:
            if probe_pdf_head(cand, session, referer=landing_url):
                pdf_url = cand
                break
        if not pdf_url:
            pdf_url = find_pdf_in_html(landing_url, landing_html)

    if not pdf_url:
        return ("FAIL", section, doi_url, "No PDF link found (may require institutional access).")

    ok = download_pdf(pdf_url, dest, session, referer=landing_url)

    if ok:
        return ("OK", section, doi_url, str(dest))
    else:
        # Fallback: save by DOI name, in case filename has unexpected chars
        fallback = save_dir / (doi.replace("/", "_") + ".pdf")
        if fallback != dest and download_pdf(pdf_url, fallback, session, referer=landing_url):
            return ("OK", section, doi_url, str(fallback))
        return ("FAIL", section, doi_url, f"Download failed: {pdf_url}")


# ------------------------- Main -------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch download PDFs from README.md (designed for your structure).")
    parser.add_argument(
    "--readme",
    type=str,
    default=str(Path(__file__).resolve().parent.parent / "README.md"),
    help="Path to README.md (default: ../README.md)"
)
    parser.add_argument("--outdir", type=str, default="downloaded_papers", help="Output directory (default: downloaded_papers)")
    parser.add_argument("--workers", type=int, default=6, help="Number of concurrent workers (default: 6)")
    parser.add_argument("--email", type=str, default="", help="Email for Unpaywall (optional)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

    readme_path = Path(args.readme).resolve()
    out_root = Path(args.outdir).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    reports_dir = out_root / "_reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    succ_csv = reports_dir / "success.csv"
    fail_csv = reports_dir / "failures.csv"

    # Parse sections and entries
    if not readme_path.exists():
        logging.error(f"README not found: {readme_path}")
        return

    sec_map = parse_readme_sections(readme_path)
    total = sum(len(v) for v in sec_map.values())
    if total == 0:
        logging.warning("No [*(paper)*](https://doi.org/...) links found in README.md.")
        return

    logging.info(f"Found {len(sec_map)} sections, {total} entries.")

    success_rows = []
    failure_rows = []

    with requests.Session() as session:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futures = []
            for sec, lines in sec_map.items():
                for line in lines:
                    futures.append(
                        ex.submit(process_entry, sec, line, out_root, args.email or None, session)
                    )
            for fut in as_completed(futures):
                status, section, doi_url, info = fut.result()
                if status == "OK":
                    logging.info(f"[OK] {doi_url} -> {info}")
                    success_rows.append((section, doi_url, info))
                else:
                    logging.info(f"[FAIL] {doi_url} | {info}")
                    failure_rows.append((section, doi_url, info))

    # Write CSV reports
    if success_rows:
        with open(succ_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["section", "doi_url", "saved_path"])
            w.writerows(success_rows)
    if failure_rows:
        with open(fail_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["section", "doi_url", "reason"])
            w.writerows(failure_rows)

    logging.info(f"Done. Success: {len(success_rows)}, Failures: {len(failure_rows)}.")
    logging.info(f"Reports: {succ_csv} | {fail_csv if failure_rows else 'None'}")


if __name__ == "__main__":
    main()
