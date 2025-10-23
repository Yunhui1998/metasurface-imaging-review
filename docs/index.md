
<h1 align="center">
  <strong>From Performance to Structure: A Comprehensive Survey of Advanced Metasurface Design for Next-Generation Imaging</strong>
</h1>

<h3 align="center">
  <em>npj Nanophotonics 2, 39 (2025)</em>
</h3>
<p align="center">
  <a href="https://github.com/Yunhui1998/metasurface-imaging-review">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?logo=github&style=flat-square" alt="GitHub Repo">
  </a>
  <a href="https://www.nature.com/articles/s44310-025-00081-6">
    <img src="https://img.shields.io/badge/npj-Nanophotonics-blue?style=flat-square" alt="npj Nanophotonics">
  </a>
</p>

<p align="center">
  <a href="https://github.com/Yunhui1998">Yunhui Zeng</a>,
  <a href="https://github.com/andyou233">Haopeng Zhong</a>,
  <a href="#">Zhenwei Long</a>,
  <a href="#">Hongkun Cao</a>,
  <a href="https://www.sigs.tsinghua.edu.cn/jx/main.htm">Xin Jin*</a>
</p>


<p align="center">
  <img alt="Stars" src="https://img.shields.io/github/stars/Yunhui1998/metasurface-imaging-review?style=social">
  <img alt="Forks" src="https://img.shields.io/github/forks/Yunhui1998/metasurface-imaging-review">
  <img alt="Issues" src="https://img.shields.io/github/issues/Yunhui1998/metasurface-imaging-review">
</p>

---

![Overview](assets/Overview.jpg)

---

## 📖 Abstract
This review introduces a ‘from performance to structure’ imaging metasurface design paradigm, which starts with essential imaging specifications and translates them into corresponding electromagnetic requirements. These requirements are then mapped onto specialized metasurface microstructures, ensuring precise electromagnetic response control. Artificial intelligence (AI) serves as a unifying thread by accelerating inverse design through efficient navigation of high-dimensional parameter spaces and by enhancing imaging performance via AI-driven computational reconstruction algorithms. We synthesize the remarkable performance of metasurfaces across six electromagnetic response control methods in nine imaging domains and categorize three main design approaches—physically-driven, meta-heuristic, and AI-driven methods—while providing a detailed analysis of six primary encoding and decoding strategies and eight common AI techniques. Additionally, nine prospective research directions are highlighted. The review emphasizes that future metasurface imaging systems will leverage electromagnetic response control to link performance with metasurface structure, with AI technology playing a central role in this process.

---

## 📂 Batch Download of References

Our **[GitHub repository](https://github.com/Yunhui1998/metasurface-imaging-review)**provides a method for **batch downloading the referenced papers**. The utility script **`Tools/download.py`** automatically parses all reference entries in the `README.md` file and downloads the corresponding PDF files (subject to network access permissions).

Detailed instructions and usage examples are available in the GitHub repository:

👉 https://github.com/Yunhui1998/metasurface-imaging-review

## 📂 Research Domains Covered

We categorize the role of metasurfaces in **nine key imaging domains**:

### 1. Chromatic Aberration Correction

![](assets/chromatic_aberration_correction.png)  

1. Chen, J. et al. 3d-printed aberration-free terahertz metalens for ultra-broadband achromatic super-resolution wide-angle imaging with high numerical aperture. *Nat. Commun.* **16**, 363 (2025). [*(paper)*](https://doi.org/10.1038/s41467-024-55624-w)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/3d-printed aberration-free terahertz metalens for ultra-broadband achromatic super-resolution wide-angle imaging with high numerical aperture.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
       Terahertz (THz) lens constitutes a vital component in the THz system. Metasurfaces-based THz metalenses and classical bulky lenses are severely constrained by chromatic/ spherical aberration and the diffraction limit. Consequently, achromatic super-resolution THz lenses are urgently needed. In this study, through translating the required phase distribution into a refractive index (RI) profile with a specific thickness, an innovative approach to designing THz metalenses is proposed and achieved by dielectric gradient metamaterials. The samples fabricated by 3D printing can realize achromatic super focusing with a numerical aperture (NA) of 0.555 from 0.2 to 0.9 THz. Submillimeter features separated by approximately 0.2 mm can be resolved with high precision, such as glass fabric patterns within FR4 panels and fibrous tissue on leaves, with a field of view (FOV) of 90°. Our approach offers a feasible and cost-effective means to implement THz super-resolution imaging, which holds great potential in non-destructive testing and biomedical imaging.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       在太赫兹成像系统中，传统透镜往往面临色差大、像差重、体积庞大的难题。介质透镜虽然可实现聚焦，但其分辨率受限且难以在高频下保持稳定成像；超表面金属透镜虽具备紧凑结构，却常常只能在窄频段内工作，无法同时消除色差与离轴像差。如何在宽频范围内实现高分辨率、超宽视场且无像差的太赫兹聚焦，一直是该领域面临的核心挑战。针对这一问题，香港城市大学太赫兹与毫米波国家重点实验室 Chi Hou Chan 团队提出了一种全新的设计理念：将金属透镜中所需的相位分布转化为等效的折射率分布，并通过径向渐变的介质超材料来实现对光线传播路径的连续调控。可以将这一思路理解为“为光波绘制一条在折射率中渐变的理想轨迹”，使其像在连续变化密度的介质中一样自然弯曲、无畸变地汇聚在同一焦点。研究团队利用高精度 3D 打印技术制备了这种渐变折射率超构透镜，实验证实其在 0.2–0.9 THz 的超宽频段内可实现数值孔径为 0.555 的消色差超聚焦，焦斑宽度仅约为 0.8 倍波长，聚焦效率稳定在 80% 左右。在 ±45° 的入射角下仍能保持清晰成像，视场角达到 90°，并成功解析出 FR4 电路板内部约 0.2 毫米的玻纤纹理和叶片的纤维组织，展现出优异的超分辨无像差成像能力。该成果以 <i>3D-printed aberration-free terahertz metalens for ultra-broadband achromatic super-resolution wide-angle imaging with high numerical aperture</i> 为题，于 2025 年 1 月 3 日发表于《Nature Communications》。
     </p>

2. You, X., Ako, R. T., Sriram, S. & Withayachumanakul, W. 3d terahertz confocal imaging with chromatic metasurface. *Laser Photonics Rev.* **19**, 2401011 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202401011)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/3D Terahertz Confocal Imaging with Chromatic Metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Terahertz confocal imaging allows 3D see-through of a non-metallic object with high resolution. Conventional methods acquiring 3D images of thick objects suffer from limited depth-of-field, constrained depth resolution, and/or inconsistent spatial resolution at different depths. To address these limitations, the intrinsic chromatic aberration of a typical focusing metasurface is exploited to achieve frequency-dependent focal lengths. An object located within this extended focal range can be readily 3D inspected by performing 2D raster scans. A rigorous analysis reveals that the focal spot maintains a constant waist diameter of 2.4 mm (equivalent to 2.2
        at 275 GHz) and migrates 68.1 mm (equivalent to 62.4
        , or 16.4 times of Rayleigh length, or 1.4-fold of the designed focal length at 275 GHz) from 175 to 525 GHz, and thus achieving a consistent spatial resolution and a large depth-of-field for 3D imaging. Importantly, this large depth-of-field is achieved with a relatively high numerical aperture of around 0.42. Measurements conducted between 220 and 330 GHz exhibit close agreement with the calculation. To demonstrate its imaging functionality, two stacked papers with different texts, a mobile phone, and earphones concealed in a charging case are imaged, where a short-time Fourier transform is implemented in the time-domain terahertz images to enhance image contrast. The presented metasurface is technologically significant for imaging systems to rapidly inspect objects in 3D with exceptional resolutions. Its potential applications include in-situ defect detection and object identification in security screening.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
3. Liu, M. et al. Achromatic and coma-corrected hybrid meta-optics for high-performance thermal imaging. *Nano Lett.* **24**, 7609–7615 (2024). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c01218)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Achromatic and coma-corrected hybrid meta-optics for high-performance thermal imaging..gif" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Long-wave infrared (LWIR) imaging, or thermal imaging, is widely applied in night vision and security monitoring. However, the widespread use of LWIR imagers is impeded by their bulky size, considerable weight, and high cost. While flat meta-optics present a potential solution to these limitations, existing pure LWIR meta-optics face constraints such as severe chromatic or coma aberrations. Here, we introduce an approach utilizing large-scale hybrid meta-optics to address these challenges and demonstrate the achromatic, coma-corrected, and polarization-insensitive thermal imaging. The hybrid metalens doublet is composed of a metasurface corrector and a refractive lens, featuring a full field-of-view angle surpassing 20° within the 8–12 μm wavelength range. Employing this hybrid metalens doublet, we showcase high-performance thermal imaging capabilities both indoors and outdoors, effectively capturing ambient thermal radiation. The proposed hybrid metalens doublet holds considerable promise for advancing miniaturized, lightweight, and cost-effective LWIR optical imaging systems.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
4. Dong, Y. et al. Achromatic single metalens imaging via deep neural network. *ACS Photonics* **11**, 1645–1656 (2024). [*(paper)*](https://doi.org/10.1021/acsphotonics.3c01870)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Achromatic Single Metalens Imaging via Deep Neural Network.jpeg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Meta-optics are attracting intensive interest as alternatives to traditional optical systems comprising multiple lenses and diffractive elements. Among applications, single metalens imaging is highly attractive due to the potential for achieving significant size reduction and simplified design. However, single metalenses exhibit severe chromatic performance degradation arising from material dispersion and the nature of singlet optics, making them unsuitable for full-color imaging requiring achromatic performance. In this work, we propose and validate a deep learning-based approach to enhance full-color imaging quality in single metalens systems. Our developed deep learning networks computationally reconstruct raw imaging captures by effectively refocusing the red, green, and blue primary channels, eliminating chromatic aberration and vignetting, and enhancing resolution. Importantly, these improvements are achieved without requiring any hardware modifications to the metalens itself. Through comprehensive evaluations on diverse synthetic and real-world data sets captured under various environmental conditions and focusing distances, our approach consistently demonstrates significant enhancements in image quality. By providing a practical and simplified implementation, our method overcomes the inherent limitations of meta-optics and enables the realization of achromatic metalenses without complex engineering. By addressing key challenges in full-color imaging for single metalenses, this research enables new practical applications in photography, videography, and micrography via the easy integration of metalenses with commercial cameras.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
5. He, H. et al. Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface. *Adv. Mater.* **36**, 2313357 (2024). [*(paper)*](https://doi.org/10.1002/adma.202313357)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
6. Hsu, W.-L. et al. High-resolution metalens imaging with sequential artificial intelligence models. *Nano Lett.* **23**, 11614–11620 (2023). [*(paper)*](https://doi.org/10.1021/acs.nanolett.3c03416)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/High-resolution metalens imaging with sequential artificial intelligence models.jpeg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        An analysis of the optical response of a GaN-based metalens was conducted alongside the utilization of two sequential artificial intelligence (AI) models in addressing the occasional issues of blurriness and color cast in captured images. The optical loss of the metalens in the blue spectral range was found to have resulted in the color cast of images. Autoencoder and CodeFormer sequential models were employed in order to correct the color cast and reconstruct image details, respectively. Said sequential models successfully addressed the color cast and reconstructed details for all of the allocated face image categories. Subsequently, the CIE 1931 chromaticity diagrams and peak signal-to-noise ratio analysis provided numerical evidence of the AI models’ effectiveness in image reconstruction. Furthermore, the AI models can still repair the image without blue information. Overall, the integration of metalens and artificial intelligence models marks a breakthrough in enhancing the performance of full-color metalens-based imaging systems.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
7. Wang, F., Zhao, S., Wen, Y., Sun, J. & Zhou, J. High efficiency visible achromatic metalens design via deep learning. *Adv. Opt. Mater.* **11**, 2300394 (2023). [*(paper)*](https://doi.org/10.1002/adom.202300394)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/High efficiency visible achromatic metalens design via deep learning.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Metalenses with both achromatic performance and high focusing efficiency are always challenging, especially in visible range. In this work, a deep learning model is developed to accelerate the design of achromatic metalenses based on the geometric phase theory. During the building process of the phase response library and selection of the nano-structures, converted transmission coefficients including both phase and amplitude are considered in order to ensure the achromatic focusing, as well as a high focusing efficiency. To test the performance of the design developed from the deep learning model, numerical simulations are performed in the visible wavelengths from 428 to 652 nm, which show a focal length of 266 µm with the deviation under 5%, and the average focusing efficiency reaches 52%.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
8. Xiao, X. et al. Large-scale achromatic flat lens by light frequency-domain coherence optimization. *Light Sci. Appl.* **11**, 323 (2022). [*(paper)*](https://doi.org/10.1038/s41377-022-01024-y)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Large-scale achromatic flat lens by light frequency-domain coherence optimization.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Flat lenses, including metalens and diffractive lens, have attracted increasing attention due to their ability to miniaturize the imaging devices. However, realizing a large scale achromatic flat lens with high performance still remains a big challenge. Here, we developed a new framework in designing achromatic multi-level diffractive lenses by light coherence optimization, which enables the implementation of large-scale flat lenses under non-ideal conditions. As results, a series achromatic polymer lenses with diameter from 1 to 10 mm are successfully designed and fabricated. The subsequent optical characterizations substantially validate our theoretical framework and show relatively good performance of the centimeter-scale achromatic multi-level diffractive lenses with a super broad bandwidth in optical wavelengths (400–1100 nm). After comparing with conventional refractive lens, this achromatic lens shows significant advantages in white-light imaging performance, implying a new strategy in developing practical planar optical devices.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
9. Heiden, J. T. & Jang, M. S. Design framework for polarization-insensitive multifunctional achromatic metalenses. *Nanophotonics* **11**, 583–591 (2021). [*(paper)*](https://doi.org/10.1515/nanoph-2021-0638)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Design framework for polarization-insensitive multifunctional achromatic metalenses.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Controlling the wavefront of light, especially on a subwavelength scale, is pivotal in modern optics. Metasurfaces present a unique platform for realizing flat lenses, called metalenses, with thicknesses on the order of the wavelength. Despite substantial effort, however, suppressing the chromatic aberrations over large operational bandwidths of metalenses still remains a challenge. Here, we develop a systematic design method enabling a simultaneous, polarization-insensitive control of the phase and the group delay of a light beam based on libraries of transmission-mode dielectric meta-elements. Mid-infrared achromatic metalenses are designed and theoretically analyzed to have diffraction-limited focal spots with vanishing chromatic aberrations in the operating wavelength range of 6–8.5 μm, while maintaining high focusing efficiencies of 41% on average. The proposed methodology, which can be used as a general design rule for all spectra, also provides a versatile design scheme for ultrashort pulse focusing and achromatic vortex-beam generation (orbital angular momentum), representing a major advance toward practical implementations of functional metalenses.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
10. Bayati, E. et al. Inverse designed extended depth of focus meta-optics for broadband imaging in the visible. *Nanophotonics* **11**, 2531–2540 (2021). [*(paper)*](https://doi.org/10.1515/nanoph-2021-0431)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Inverse designed extended depth of focus meta-optics for broadband imaging in the visible.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        We report an inverse-designed, high numerical aperture (∼0.44), extended depth of focus (EDOF) meta-optic, which exhibits a lens-like point spread function (PSF). The EDOF meta-optic maintains a focusing efficiency comparable to that of a hyperboloid metalens throughout its depth of focus. Exploiting the extended depth of focus and computational post processing, we demonstrate broadband imaging across the full visible spectrum using a 1 mm, f/1 meta-optic. Unlike other canonical EDOF meta-optics, characterized by phase masks such as a log-asphere or cubic function, our design exhibits a highly invariant PSF across ∼290 nm optical bandwidth, which leads to significantly improved image quality, as quantified by structural similarity metrics.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
11. Wang, F. et al. Visible achromatic metalens design based on artificial neural network. *Adv. Opt. Mater.* **10**, 2101842 (2021). [*(paper)*](https://doi.org/10.1002/adom.202101842)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Visible achromatic metalens design based on artificial neural network.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Metasurfaces, known as ultra-thin and planar structures, are widely used in optical components with their excellent ability to manipulate the wavefront of the light. The key function of the metasurfaces is the spatial phase modulation, originated from the meta-atoms. Thus, to find the relation between the phase modulation and the parameters of an individual meta-atom, including the sizes, shapes, and material's optical properties, is the most important but also time-consuming part in the metasurface design. Here by developing a backpropagation neural network based machine learning tool, the design process of a high performance achromatic metalens can be greatly simplified and accelerated. A library of the phase modulation data from 15 753 meta-atoms can be generated in less than 1 s by our backpropagation neural network. In the experiment, it is demonstrated that the designed metalens shows an excellent achromatic focusing and imaging ability in the visible wavelengths from 420 to 640 nm without the polarization dependence.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
12. Wang, Y. et al. High-efficiency broadband achromatic metalens for near-IR biological imaging window. *Nat. Commun.* **12**, 5560 (2021). [*(paper)*](https://doi.org/10.1038/s41467-021-25797-9)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/High-efficiency broadband achromatic metalens for near-IR biological imaging window.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Over the past years, broadband achromatic metalenses have been intensively studied due to their great potential for applications in consumer and industry products. Even though significant progress has been made, the efficiency of technologically relevant silicon metalenses is limited by the intrinsic material loss above the bandgap. In turn, the recently proposed achromatic metalens utilizing transparent, high-index materials such as titanium dioxide has been restricted by the small thickness and showed relatively low focusing efficiency at longer wavelengths. Consequently, metalens-based optical imaging in the biological transparency window has so far been severely limited. Herein, we experimentally demonstrate a polarization-insensitive, broadband titanium dioxide achromatic metalens for applications in the near-infrared biological imaging. A large-scale fabrication technology has been developed to produce titanium dioxide nanopillars with record-high aspect ratios featuring pillar heights of 1.5 µm and ~90° vertical sidewalls. The demonstrated metalens exhibits dramatically increased group delay range, and the spectral range of achromatism is substantially extended to the wavelength range of 650–1000 nm with an average efficiency of 77.1%–88.5% and a numerical aperture of 0.24–0.1. This research paves a solid step towards practical applications of flat photonics.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
13. Ou, K. et al. Broadband achromatic metalens in mid-wavelength infrared. *Laser Photon. Rev.* **15**, 2100020 (2021). [*(paper)*](https://doi.org/10.1002/lpor.202100020)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Broadband achromatic metalens in mid-wavelength infrared.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Metasurface provides a powerful platform to correct the chromatic aberration of conventional lenses in a flexible, integratable, and ultra-compact manner. Mid-wavelength infrared has promised many exciting applications ranged from molecular fingerprint detection to low-light-level night vision. Developing broadband achromatic metalens in mid-wavelength infrared becomes necessary to meet the increasingly urgent demands on high performance photonic devices. Here, we demonstrate the broadband achromatic metalenses from 3.5 to 5 µm with all-silicon metasurfaces. Large phase dispersion control range is achieved to realize metalenses with both large numerical apertures and sample sizes while maintaining high focusing efficiency. The experimental results verify the diffraction-limited achromatic focusing and imaging of the metalenses in mid-wavelength infrared. Additionally, we also demonstrate the versatility by successfully implementing the generation of the broadband achromatic focusing optical vortex (L = 2). This work represents a solid step toward practical implementation of metalens and may find applications in mid-wavelength infrared imaging and detections.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
14. Zang, W. et al. Chromatic dispersion manipulation based on metalenses. *Adv. Mater.* **32**, 1904935 (2020). [*(paper)*](https://doi.org/10.1002/adma.201904935)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Chromatic dispersion manipulation based on metalenses.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Metasurfaces are 2D metamaterials composed of subwavelength nanoantennas according to specific design. They have been utilized to precisely manipulate various parameters of light fields, such as phase, polarization, amplitude, etc., showing promising functionalities. Among all meta-devices, the metalens can be considered as the most basic and important application, given its significant advantage in integration and miniaturization compared with traditional lenses. However, the resonant dispersion of each nanoantenna in a metalens and the intrinsic chromatic dispersion of planar devices and optical materials result in a large chromatic aberration in metalenses that severely reduces the quality of their focusing and imaging. Consequently, how to effectively suppress or manipulate the chromatic aberration of metalenses has attracted worldwide attention in the last few years, leading to variety of excellent achievements promoting the development of this field. Herein, recent progress in chromatic dispersion control based on metalenses is reviewed.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
15. McClung, A., Mansouree, M. & Arbabi, A. At-will chromatic dispersion by prescribing light trajectories with cascaded metasurfaces. *Light Sci. Appl.* **9**, 93 (2020). [*(paper)*](https://doi.org/10.1038/s41377-020-0335-7)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/At-will chromatic dispersion by prescribing light trajectories with cascaded metasurfaces.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Chromatic dispersion spatially separates white light into colours, producing rainbows and similar effects. Detrimental to imaging but essential to spectroscopy, chromatic dispersion is the result of material properties in refractive optics and is considered an inherent characteristic of diffractive devices such as gratings and flat lenses. Here, we present a fundamental relation connecting an optical system’s dispersion to the trajectories light takes through it and show that arbitrary control over dispersion may be achieved by prescribing specific trajectories, even in diffractive systems. Using cascaded metasurfaces (2D arrays of sub-micron scatterers) to direct light along predetermined trajectories, we present an achromatic twisted metalens and experimentally demonstrate beam deflectors with arbitrary dispersion. This new insight and design approach usher in a new class of optical systems with wide-ranging applications.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
16. Ndao, A. et al. Octave bandwidth photonic fishnet-achromatic-metalens. *Nat. Commun.* **11**, 3205 (2020). [*(paper)*](https://doi.org/10.1038/s41467-020-17015-9)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Octave bandwidth photonic fishnet-achromatic-metalens.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Planar structured interfaces, also known as metasurfaces, are continuously attracting interest owing to their ability to manipulate fundamental attributes of light, including angular momentum, phase, or polarization. However, chromatic aberration, limiting broadband operation, has remained a challenge for metasurfaces-based optical components and imagers. The limitation stems from the intrinsic dispersion of existing materials and design principles. Here we report and experimentally demonstrate polarization-independent fishnet-achromatic-metalenses with measured average efficiencies over 70% in the continuous band from the visible (640 nm) to the infrared (1200 nm). Results of the scalable platform are enabling for applications requiring broad bandwidth and high efficiency including energy harvesting, virtual reality and information processing devices, or medical imaging.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
17. Huang, L., Whitehead, J., Colburn, S. & Majumdar, A. Design and analysis of extended depth of focus metalenses for achromatic computational imaging. *Photonics Res.* **8**, 1613–1623 (2020). [*(paper)*](https://doi.org/10.1364/PRJ.396839)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Design and analysis of extended depth of focus metalenses for achromatic computational imaging.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Metasurface optics have demonstrated vast potential for implementing traditional optical components in an ultracompact and lightweight form factor. Metasurfaces, however, suffer from severe chromatic aberrations, posing serious limitations on their practical use. Existing approaches for circumventing this involving dispersion engineering are limited to small apertures and often entail multiple scatterers per unit cell with small feature sizes. Here, we present an alternative technique to mitigate chromatic aberration and demonstrate high-quality, full-color imaging using extended depth of focus (EDOF) metalenses and computational reconstruction. Previous EDOF metalenses have relied on cubic phase masks, where the image quality suffers from asymmetric artefacts. Here we demonstrate the use of rotationally symmetric masks, including logarithmic-aspherical, and shifted axicon masks, to mitigate this problem. Our work will inspire further development in achromatic metalenses beyond dispersion engineering and hybrid optical–digital metasurface systems.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
18. Presutti, F. & Monticone, F. Focusing on bandwidth: achromatic metalens limits. *Optica* **7**, 624–631 (2020). [*(paper)*](https://doi.org/10.1364/OPTICA.389404)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Focusing on bandwidth achromatic metalens limits.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Metalenses have shown great promise in their ability to function as ultracompact optical systems for focusing and imaging. Remarkably, several designs have been recently demonstrated that operate over a large range of frequencies with minimized chromatic aberrations, potentially paving the way for ultrathin achromatic optics. Here, we derive fundamental bandwidth limits that apply to broadband optical metalenses regardless of their implementation. Specifically, we discuss how the product between achievable time delay and bandwidth is limited in any time-invariant system, and we apply well-established bounds on this product to a general focusing system. We then show that all metalenses designed thus far obey the appropriate bandwidth limit. The derived physical bounds provide a useful metric to compare and assess the performance of different devices, and they offer fundamental insight into how to design better broadband metalenses.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
19. Zhang, C. et al. Low-loss metasurface optics down to the deep ultraviolet region. *Light Sci. Appl.* **9**, 55 (2020). [*(paper)*](https://doi.org/10.1038/s41377-020-0287-y)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Low-loss metasurface optics down to the deep ultraviolet region.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Shrinking conventional optical systems to chip-scale dimensions will benefit custom applications in imaging, displaying, sensing, spectroscopy, and metrology. Towards this goal, metasurfaces—planar arrays of subwavelength electromagnetic structures that collectively mimic the functionality of thicker conventional optical elements—have been exploited at frequencies ranging from the microwave range up to the visible range. Here, we demonstrate high-performance metasurface optical components that operate at ultraviolet wavelengths, including wavelengths down to the record-short deep ultraviolet range, and perform representative wavefront shaping functions, namely, high-numerical-aperture lensing, accelerating beam generation, and hologram projection. The constituent nanostructured elements of the metasurfaces are formed of hafnium oxide—a loss-less, high-refractive-index dielectric material deposited using low-temperature atomic layer deposition and patterned using high-aspect-ratio Damascene lithography. This study opens the way towards low-form factor, multifunctional ultraviolet nanophotonic platforms based on flat optical components, enabling diverse applications including lithography, imaging, spectroscopy, and quantum information processing.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
20. Chen, W. T., Zhu, A. Y., Sisler, J., Bharwani, Z. & Capasso, F. A broadband achromatic polarization-insensitive metalens consisting of anisotropic nanostructures. *Nat. Commun.* **10**, 355 (2019). [*(paper)*](https://doi.org/10.1038/s41467-019-08305-y)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A broadband achromatic polarization-insensitive metalens consisting of anisotropic nanostructures.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Metasurfaces have attracted widespread attention due to an increasing demand of compact and wearable optical devices. For many applications, polarization-insensitive metasurfaces are highly desirable, and appear to limit the choice of their constituent elements to isotropic nanostructures. This greatly restricts the number of geometric parameters available in design. Here, we demonstrate a polarization-insensitive metalens using otherwise anisotropic nanofins which offer additional control over the dispersion and phase of the output light. As a result, we can render a metalens achromatic and polarization-insensitive across nearly the entire visible spectrum from wavelength λ = 460 nm to 700 nm, while maintaining diffraction-limited performance. The metalens is comprised of just a single layer of TiO2 nanofins and has a numerical aperture of 0.2 with a diameter of 26.4 µm. The generality of our polarization-insensitive design allows it to be implemented in a plethora of other metasurface devices with applications ranging from imaging to virtual/augmented reality.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
21. Chen, W. T. et al. A broadband achromatic metalens for focusing and imaging in the visible. *Nat. Nanotechnol.* **13**, 220–226 (2018). [*(paper)*](https://doi.org/10.1038/s41565-017-0034-6)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A broadband achromatic metalens for focusing and imaging in the visible.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
       A key goal of metalens research is to achieve wavefront shaping of light using optical elements with thicknesses on the order of the wavelength. Such miniaturization is expected to lead to compact, nanoscale optical devices with applications in cameras, lighting, displays and wearable optics. However, retaining functionality while reducing device size has proven particularly challenging. For example, so far there has been no demonstration of broadband achromatic metalenses covering the entire visible spectrum. Here, we show that by judicious design of nanofins on a surface, it is possible to simultaneously control the phase, group delay and group delay dispersion of light, thereby achieving a transmissive achromatic metalens with large bandwidth. We demonstrate diffraction-limited achromatic focusing and achromatic imaging from 470 to 670 nm. Our metalens comprises only a single layer of nanostructures whose thickness is on the order of the wavelength, and does not involve spatial multiplexing or cascading. While this initial design (numerical aperture of 0.2) has an efficiency of about 20% at 500 nm, we discuss ways in which our approach may be further optimized to meet the demand of future applications.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
22. Wang, S. et al. Broadband achromatic optical metasurface devices. *Nat. Commun.* **8**, 187 (2017). [*(paper)*](https://doi.org/10.1038/s41467-017-00166-7)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Broadband achromatic optical metasurface devices.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Among various flat optical devices, metasurfaces have presented their great ability in efficient manipulation of light fields and have been proposed for variety of devices with specific functionalities. However, due to the high phase dispersion of their building blocks, metasurfaces significantly suffer from large chromatic aberration. Here we propose a design principle to realize achromatic metasurface devices which successfully eliminate the chromatic aberration over a continuous wavelength region from 1200 to 1680 nm for circularly-polarized incidences in a reflection scheme. For this proof-of-concept, we demonstrate broadband achromatic metalenses (with the efficiency on the order of ∼12%) which are capable of focusing light with arbitrary wavelength at the same focal plane. A broadband achromatic gradient metasurface is also implemented, which is able to deflect wide-band light by the same angle. Through this approach, various flat achromatic devices that were previously impossible can be realized, which will allow innovation in full-color detection and imaging.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
23. Khorasaninejad, M. et al. Achromatic metalens over 60 nm bandwidth in the visible and metalens with reverse chromatic dispersion. *Nano Lett.* **17**, 1819–1824 (2017). [*(paper)*](https://doi.org/10.1021/acs.nanolett.6b05137)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Achromatic metalens over 60 nm bandwidth in the visible and metalens with reverse chromatic dispersion.jpeg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        In this Letter, we experimentally report an achromatic metalens (AML) operating over a continuous bandwidth in the visible. This is accomplished via dispersion engineering of dielectric phase shifters: titanium dioxide nanopillars tiled on a dielectric spacer layer above a metallic mirror. The AML works in reflection mode with a focal length independent of wavelength from λ = 490 to 550 nm. We also design a metalens with reverse chromatic dispersion, where the focal length increases as the wavelength increases, contrary to conventional diffractive lenses. The ability to engineer the chromatic dispersion of metalenses at will enables a wide variety of applications that were not previously possible. In particular, for the AML design, we envision applications such as imaging under LED illumination, fluorescence, and photoluminescence spectroscopy.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
24. Avayu, O., Almeida, E., Prior, Y. & Ellenbogen, T. Composite functional metasurfaces for multispectral achromatic optics. *Nat. Commun.* **8**, 14992 (2017). [*(paper)*](https://doi.org/10.1038/ncomms14992)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Composite functional metasurfaces for multispectral achromatic optics.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Nanostructured metasurfaces offer unique capabilities for subwavelength control of optical waves. Based on this potential, a large number of metasurfaces have been proposed recently as alternatives to standard optical elements. In most cases, however, these elements suffer from large chromatic aberrations, thus limiting their usefulness for multiwavelength or broadband applications. Here, in order to alleviate the chromatic aberrations of individual diffractive elements, we introduce dense vertical stacking of independent metasurfaces, where each layer is made from a different material, and is optimally designed for a different spectral band. Using this approach, we demonstrate a triply red, green and blue achromatic metalens in the visible range. We further demonstrate functional beam shaping by a self-aligned integrated element for stimulated emission depletion microscopy and a lens that provides anomalous dispersive focusing. These demonstrations lead the way to the realization of ultra-thin superachromatic optical elements showing multiple functionalities—all in a single nanostructured ultra-thin element.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
25. Khorasaninejad, M. et al. Achromatic metasurface lens at telecommunication wavelengths. *Nano Lett.* **15**, 5358–5362 (2015). [*(paper)*](https://doi.org/10.1021/acs.nanolett.5b01727)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Achromatic metasurface lens at telecommunication wavelengths.jpeg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Nanoscale optical resonators enable a new class of flat optical components called metasurfaces. This approach has been used to demonstrate functionalities such as focusing free of monochromatic aberrations (i.e., spherical and coma), anomalous reflection, and large circular dichroism. Recently, dielectric metasurfaces that compensate the phase dispersion responsible for chromatic aberrations have been demonstrated. Here, we utilize an aperiodic array of coupled dielectric nanoresonators to demonstrate a multiwavelength achromatic lens. The focal length remains unchanged for three wavelengths in the near-infrared region (1300, 1550, and 1800 nm). Experimental results are in agreement with full-wave simulations. Our findings are an essential step toward a realization of broadband flat optical elements.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
26. Akselrod, G. M. et al. Large-area metasurface perfect absorbers from visible to near-infrared. *Adv. Mater.* **27**, 8028–8024 (2015). [*(paper)*](https://doi.org/10.1002/adma.201503281)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Large-area metasurface perfect absorbers from visible to near-infrared.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        An absorptive metasurface based on film-coupled colloidal silver nanocubes is demonstrated. The metasurfaces are fabricated using simple dip-coating methods and can be deposited over large areas and on arbitrarily shaped objects. The surfaces show nearly complete absorption, good off-angle performance, and the resonance can be tuned from the visible to the near-infrared.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
27. Aieta, F. et al. Aberration-free ultrathin flat lenses and axicons at telecom wavelengths based on plasmonic metasurfaces. *Nano Lett.* **12**, 4932–4936 (2012). [*(paper)*](https://doi.org/10.1021/nl302516v)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Aberration-free ultrathin flat lenses and axicons at telecom wavelengths based on plasmonic metasurfaces.gif" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        The concept of optical phase discontinuities is applied to the design and demonstration of aberration-free planar lenses and axicons, comprising a phased array of ultrathin subwavelength-spaced optical antennas. The lenses and axicons consist of V-shaped nanoantennas that introduce a radial distribution of phase discontinuities, thereby generating respectively spherical wavefronts and nondiffracting Bessel beams at telecom wavelengths. Simulations are also presented to show that our aberration-free designs are applicable to high-numerical aperture lenses such as flat microscope objectives.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
---

### 2. Field of View Expansion

![](assets/view_expansion.png)  

1.  Wirth-Singh, A. et al. Wide field of view large aperture meta-doublet eyepiece. *Light Sci. Appl.* **14**, 17 (2025). [*(paper)*](https://doi.org/10.1038/s41377-024-01674-0)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Wide field of view large aperture meta-doublet eyepiece.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Wide field of view and light weight optics are critical for advanced eyewear, with applications in augmented/virtual reality and night vision. Conventional refractive lenses are often stacked to correct aberrations at a wide field of view, leading to limited performance and increased size and weight. In particular, simultaneously achieving a wide field of view and large aperture for light collection is desirable but challenging to realize in a compact form-factor. Here, we demonstrate a wide field of view (greater than 60∘) meta-optic doublet eyepiece with an entrance aperture of 2.1 cm. At the design wavelength of 633 nm, the meta-optic doublet achieves comparable performance to a refractive lens-based eyepiece system. This meta-doublet eyepiece illustrates the potential for meta-optics to play an important role in the development of high-quality monochrome near-eye displays and night vision systems.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
2.  Liu, Y. et al. Ultra-wide for meta-camera with transformer-neural-network color imaging methodology. *Adv. Photonics* **6**, 056001 (2024). [*(paper)*](https://doi.org/10.1117/1.AP.6.5.056001)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Ultra-wide for meta-camera with transformer-neural-network color imaging methodology.png" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Planar cameras with high performance and wide field of view (FOV) are critical in various fields, requiring highly compact and integrated technology. Existing wide FOV metalenses show great potential for ultrathin optical components, but there is a set of tricky challenges, such as chromatic aberrations correction, central bright speckle removal, and image quality improvement of wide FOV. We design a neural meta-camera by introducing a knowledge-fused data-driven paradigm equipped with transformer-based network. Such a paradigm enables the network to sequentially assimilate the physical prior and experimental data of the metalens, and thus can effectively mitigate the aforementioned challenges. An ultra-wide FOV meta-camera, integrating an off-axis monochromatic aberration-corrected metalens with a neural CMOS image sensor without any relay lenses, is employed to demonstrate the availability. High-quality reconstructed results of color images and real scene images at different distances validate that the proposed meta-camera can achieve an ultra-wide FOV (>100deg) and full-color images with the correction of chromatic aberration, distortion, and central bright speckle, and the contrast increase up to 13.5 times. Notably, coupled with its compact size (<0.13cm<sup>3</sup>), portability, and full-color imaging capacity, the neural meta-camera emerges as a compelling alternative for applications, such as micro-navigation, micro-endoscopes, and various on-chip devices.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
3.  Wang, Y. et al. Compact meta-optics infrared camera based on a polarization-insensitive metalens with a large field of view. *Opt. Lett.* **48**, 4709–4712 (2023). [*(paper)*](https://doi.org/10.1364/OL.499942)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Compact meta-optics infrared camera based on a polarization-insensitive metalens with a large field of view.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
       Metasurfaces have recently emerged as a crucial tool because they achieve spherical-aberration-free focusing when exposed to normal incident light. Nevertheless, these metasurfaces often exhibit considerable coma when subjected to oblique incident light, thereby limiting their imaging field of view. In light of this, our study presents the design and an experimental demonstration of a polarization-insensitive, large-field-of-view metalens that uses a silicon metasurface. The metalens is specifically tailored to the long-wavelength infrared region and possesses a numerical aperture of 0.81, which is capable of focusing light at incident angles up to ±80°. Moreover, we successfully build a meta-optics camera by integrating the large field-of-view metalens on top of an image sensor, thus enabling wide-angle thermal imaging of practical scenes. This research provides new, to the best of our knowledge, insights for designing and realizing large-field-of-view optical systems and holds promise for applications in night vision imaging and security monitoring.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
4.  Liu, J., Chu, J., Zhang, R., Liu, R. & Fu, J. Wide field of view and full strokes polarization imaging using metasurfaces inspired by the stomatopod eye. *Nanophotonics* **12**, 1137–1146 (2023). [*(paper)*](https://doi.org/10.1515/nanoph-2022-0712)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Wide field of view and full strokes polarization imaging using metasurfaces inspired by the stomatopod eye.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Wide field of view and polarization imaging capabilities are crucial for implementation of advanced imaging devices. However, there are still great challenges in the integration of such optical systems. Here, we report a bionic compound eye metasurface that can realize full Stokes polarization imaging in a wide field of view. The bionic compound eye metasurface consists of a bifocal metalens array in which every three bifocal metalenses form a subeye. The phase of the bifocal metalens is composed of gradient phase and hyperbolic phase. Numerical simulations show that the bifocal metalens can not only improve the focusing efficiency in the oblique light but also correct the aberration caused by the oblique incident light. And the field of view of the bionic compound eye metasurface can reach 120° × 120°. We fabricated a bionic compound eye metasurface which consists of three subeyes. Experiments show that the bionic compound eye metasurface can perform near diffraction-limited polarization focusing and imaging in a large field of view. The design method is generic and can be used to design metasurfaces with different materials and wavelengths. It has great potential in the field of robot polarization vision and polarization detection.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
5.  Chen, J. et al. Planar wide-angle-imaging camera enabled by metalens array. *Optica* **9**, 431–437 (2022). [*(paper)*](https://doi.org/10.1364/OPTICA.446063)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
6.  Li, S. & Hsu, C. W. Thickness bound for nonlocal wide-field-of-view metalenses. *Light Sci. Appl.* **11**, 338 (2022). [*(paper)*](https://doi.org/10.1038/s41377-022-01038-6)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
7.  Lassalle, E. et al. Imaging properties of large field-of-view quadratic metalenses and their applications to fingerprint detection. *Acs Photonics* **8**, 1457–1468 (2021). [*(paper)*](https://doi.org/10.1021/acsphotonics.1c00237)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
8.  Shalaginov, M. Y. et al. Single-element diffraction-limited fisheye metalens. *Nano Lett.* **20**, 7429–7437 (2020). [*(paper)*](https://doi.org/10.1021/acs.nanolett.0c02783)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
9.  Hao, C. et al. Single-layer aberration-compensated flat lens for robust wide-angle imaging. *Laser Photonics Rev.* **14**, 2000017 (2020). [*(paper)*](https://doi.org/10.1002/lpor.202000017)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
10.  Martins, A. et al. On metalenses with arbitrarily wide field of view. *Acs Photonics* **7**, 2073–2079 (2020). [*(paper)*](https://doi.org/10.1021/acsphotonics.0c00479)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
11.  Xu, B. et al. Metalens-integrated compact imaging devices for wide-field microscopy. *Adv. Photonics* **2**, 066004 (2020). [*(paper)*](https://doi.org/10.1117/1.AP.2.6.066004)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
12.  Engelberg, J. et al. Near-IR wide-field-of-view huygens metalens for outdoor imaging applications. *Nanophotonics* **9**, 361–370 (2020). [*(paper)*](https://doi.org/10.1515/nanoph-2019-0177)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
13.  Fan, C.-Y., Lin, C.-P. & Su, G.-D. J. Ultrawide-angle and high-efficiency metalens in hexagonal arrangement. *Sci. Rep.* **10**, 15677 (2020). [*(paper)*](https://doi.org/10.1038/s41598-020-72668-2)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
14.  Groever, B., Chen, W. T. & Capasso, F. Meta-lens doublet in the visible region. *Nano Lett.* **17**, 4902–4907 (2017). [*(paper)*](https://doi.org/10.1021/acs.nanolett.7b01888)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
15.  Arbabi, A. et al. Miniature optical planar camera based on a wide-angle metasurface doublet corrected for monochromatic aberrations. *Nat. Commun.* **7**, 13682 (2016). [*(paper)*](https://doi.org/10.1038/ncomms13682)

     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
---

### 3. Depth of Field Extension

![](assets/depth_of_field.png)  

1.  Ansari, M. A. et al. Multifaceted control of focal points along an arbitrary 3d curved trajectory. *Light Sci. Appl.* **13**, 224 (2024). [*(paper)*](https://doi.org/10.1038/s41377-024-01565-4)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
2.  Liu, X. et al. Underwater binocular meta-lens. *ACS Photonics* **10**, 2382–2389 (2023). [*(paper)*](https://doi.org/10.1021/acsphotonics.2c01667)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-attention network based spectral reconstruction with snapshot near-infrared metasurface.jpg" 
         alt="Graphical abstract"
         style="width:85%; max-width:650px; border-radius:8px;"
       >
     </div>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:16px;
     ">
       <b>Abstract (English):</b><br>
        Near-infrared (NIR) spectral information is important for detecting and analyzing material compositions. However, snapshot NIR spectral imaging systems still pose significant challenges owing to the lack of high-performance NIR filters and bulky setups, preventing effective encoding and integration with mobile devices. This study introduces a snapshot spectral imaging system that employs a compact NIR metasurface featuring 25 distinct C4 symmetry structures. Benefitting from the sufficient spectral variety and low correlation coefficient among these structures, center-wavelength accuracy of 0.05 nm and full width at half maximum accuracy of 0.13 nm are realized. The system maintains good performance within an incident angle of 1°. A novel meta-attention network prior iterative denoising reconstruction (MAN-IDR) algorithm is developed to achieve high-quality NIR spectral imaging. By leveraging the designed metasurface and MAN-IDR, the NIR spectral images, exhibiting precise textures, minimal artifacts in the spatial dimension, and little crosstalk between spectral channels, are reconstructed from a single grayscale recording image. The proposed NIR metasurface and MAN-IDR hold great promise for further integration with smartphones and drones, guaranteeing the adoption of NIR spectral imaging in real-world scenarios such as aerospace, health diagnostics, and machine vision.
     </p>
     <p style="
       color:#333333;
       text-align: justify;
       text-justify: inter-ideograph;
       line-height:1.65;
       margin-bottom:0;
     ">
       <b>摘要（中文）:</b><br>
       
     </p>
3.  Yin, B. & Wang, S. Research and design of a metasurface with an extended depth of focus in the near field. *Appl. Opt.* **62**, 7621–7627 (2023). [*(paper)*](https://doi.org/10.1364/AO.500686)
   
4.  Zhao, J. et al. Rapid cellular-resolution skin imaging with optical coherence tomography using all-glass multifocal metasurfaces. *ACS nano* **17**, 3442–3451 (2023). [*(paper)*](https://doi.org/10.1021/acsnano.2c09542)
   
5.  Shen, Z. et al. Monocular metasurface camera for passive single-shot 4d imaging. *Nat. Commun.* **14**, 1035 (2023). [*(paper)*](https://doi.org/10.1038/s41467-023-36812-6)
   
6.  Zheng, Y. et al. Designing high-efficiency extended depth-of-focus metalens via topology-shape optimization. *Nanophotonics* **11**, 2967–2975 (2022). [*(paper)*](https://doi.org/10.1515/nanoph-2022-0183)
   
7.  Zheng, R. et al. Active multiband varifocal metalens based on orbital angular momentum division multiplexing. *Nat. Commun.* **13**, 4292 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-32044-2)
   
8.  Fan, Q. et al. Triholite-inspired neural nanophotonic light-field camera with extreme depth-of-field. *Nat. Commun.* **13**, 2130 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-29568-y)
   
9.  Zhao, F. et al. Metalens-assisted system for underwater imaging. *Laser Photonics Rev.* **15**, 2100097 (2021). [*(paper)*](https://doi.org/10.1002/lpor.202100097)
    
10.  Tan, S., Yang, F., Boominathan, V., Veeraraghavan, A. & Naik, G. V. 3d imaging using extreme dispersion in optical metasurfaces. *ACS Photonics* **8**, 1421–1429 (2021). [*(paper)*](https://doi.org/10.1021/acsphotonics.1c00110)
    
11.  Bayati, E. et al. Inverse designed metalenses with extended depth of focus. *ACS Photonics* **7**, 873–878 (2020). [*(paper)*](https://doi.org/10.1021/acsphotonics.9b01703)
    
12.  Zhang, Z., Yang, Q., Gong, M., Chen, M. & Long, Z. Metasurface lens with angular modulation for extended depth of focus imaging. *Opt. Lett.* **45**, 611–614 (2020). [*(paper)*](https://doi.org/10.1364/OL.382812)
    
13.  Colburn, S. & Majumdar, A. Single-shot three-dimensional imaging with a metasurface depth camera. *arXiv preprint arXiv:1910.12111* (2019). [*(paper)*](https://arxiv.org/abs/1910.12111)

---

### 4. Resolution Enhancement

![](assets/resolution_enhancement.png)  

1.  Basak, S. et al. Super-resolution optical fluctuation imaging. *Nat. Photonics* **19**, 229–237 (2025). [*(paper)*](https://doi.org/10.1038/s41566-024-01571-3)
   
2.  Zhou, Q. et al. Far-field phase-shifting structured light illumination enabled by polarization multiplexing metasurface for super-resolution imaging. *Nano Lett.* **24**, 11036–11042 (2024). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c03142)
   
3.  Wang, J. et al. Quantitative phase imaging with a compact metamicroscope. *npj Nanophotonics* **1**, 4 (2024). [*(paper)*](https://doi.org/10.1038/s44310-024-00007-8)
   
4.  Li, W., Qi, J. & Mu, A. Single-pixel super-resolution with a space-time modulated computational metasurface imager. *Photonics Res.* **12**, 2311–2322 (2024). [*(paper)*](https://doi.org/10.1364/PRJ.532222)
   
5.  Akbari-Chelaresi, H., Salami, P. & Yousefi, L. Far-field sub-wavelength imaging using high-order dielectric continuous metasurfaces. *Opt. Express* **30**, 39025–39039 (2022). [*(paper)*](https://doi.org/10.1364/OE.470221)
   
6.  Ye, X. et al. Chip-scale metalens microscope for wide-field and depth-of-field imaging. *Adv. Photonics* **4**, 046006 (2022). [*(paper)*](https://doi.org/10.1117/1.AP.4.4.046006)
   
7.  Sawant, R. et al. Aberration-corrected large-scale hybrid metalenses. *Optica* **8**, 1405–1411 (2021). [*(paper)*](https://doi.org/10.1364/OPTICA.434040)
   
8.  Hampson, K. M. et al. Adaptive optics for high-resolution imaging. *Nat. Rev. Methods Prim.* **1**, 68 (2021). [*(paper)*](https://doi.org/10.1038/s43586-021-00066-7)
   
9.  Hajahmadi, M. J., Faraji-Dana, R. & Skrivenvik, A. K. Far field superlensing inside biological media through a nanorod lens using spatiotemporal information. *Sci. Rep.* **11**, 1953 (2021). [*(paper)*](https://doi.org/10.1038/s41598-021-81091-0)
  
10.  Chen, M.-H., Chou, W.-N., Su, V.-C., Kuan, C.-H. & Lin, H. Y. High-performance gallium nitride dielectric metalenses for imaging in the visible. *Sci. Rep.* **11**, 6500 (2021). [*(paper)*](https://doi.org/10.1038/s41598-021-86057-w)
    
11.  Conteduca, D. et al. Dielectric nanohole array metasurface for high-resolution near-field sensing and imaging. *Nat. Commun.* **12**, 3293 (2021). [*(paper)*](https://doi.org/10.1038/s41467-021-23357-9)
    
12.  Zhu, A. Y. et al. Compact aberration-corrected spectrometers in the visible using dispersion-tailored metasurfaces. *Adv. Opt. Mater.* **7**, 1801144 (2019). [*(paper)*](https://doi.org/10.1002/adom.201801144)
    
13.  Holsteen, A. L., Lin, D., Kauvar, I., Wetzstein, G. & Brongersma, M. L. A light-field metasurface for high-resolution single-particle tracking. *Nano Lett.* **19**, 2267–2271 (2019). [*(paper)*](https://doi.org/10.1021/acs.nanolett.8b04673)
    
14.  Hall, C. U., Poulikakos, D. & Eghlidi, H. High-efficiency, extreme-numerical-aperture metasurfaces based on partial control of the phase of light. *Adv. Opt. Mater.* **6**, 1800852 (2018). [*(paper)*](https://doi.org/10.1002/adom.201800852)
    
15.  Paniagua-Dominguez, R. et al. A metalens with a near-unity numerical aperture. *Nano Lett.* **18**, 2124–2132 (2018). [*(paper)*](https://doi.org/10.1021/acs.nanolett.8b00368)
    
16.  Zuo, R., Liu, W., Cheng, H., Chen, S. & Tian, J. Breaking the diffraction limit with radially polarized light based on dielectric metalenses. *Adv. Opt. Mater.* **6**, 1800795 (2018). [*(paper)*](https://doi.org/10.1002/adom.201800795)
    
17.  Chen, W. T. et al. Immersion meta-lenses at visible wavelengths for nanoscale imaging. *Nano Lett.* **17**, 3188–3194 (2017). [*(paper)*](https://doi.org/10.1021/acs.nanolett.7b00717)
    
18.  Gao, H. et al. Super-resolution imaging with a beesel lens realized by a geometric metasurface. *Opt. Express* **25**, 13933–13943 (2017). [*(paper)*](https://doi.org/10.1364/OE.25.013933)
    
19.  Yang, H. et al. Reflective metalens with sub-diffraction-limited and multifunctional focusing. *Sci. Rep.* **7**, 12632 (2017). [*(paper)*](https://doi.org/10.1038/s41598-017-13004-z)
    
20.  Khorasaninejad, M. et al. Metalenses at visible wavelengths: diffraction-limited focusing and subwavelength resolution imaging. *Science* **352**, 1190–1194 (2016). [*(paper)*](https://doi.org/10.1126/science.aaf6644)
    
21.  Lu, D. & Liu, Z. Hyperlenses and metalenses for far-field super-resolution imaging. *Nat. Commun.* **3**, 1205 (2012). [*(paper)*](https://doi.org/10.1038/ncomms2176)
    
22.  Fang, N., Lee, H., Sun, C. & Zhang, X. Sub-diffraction-limited optical imaging with a silver superlens. *Science* **308**, 534–537 (2005). [*(paper)*](https://doi.org/10.1126/science.1108759)

---

### 5. Multidimensional Data Capture

![](assets/multidimensional_data_capture.png)  

1. Fu, B. et al. Miniaturized high-efficiency snapshot polarimetric stereoscopic imaging. *Optica* **12**, 391–398 (2025). [*(paper)*](https://doi.org/10.1364/OPTICA.549864)
  
2. Zhao, Z. et al. Hyperspectral metachip-based 3d spatial map for cancer cell screening and quantification. *Adv. Mater.* **37**, 2412738 (2025). [*(paper)*](https://doi.org/10.1002/adma.202412738)
  
3. Zhang, Z. et al. Single-shot on-chip diffractive speckle spectrometer with high spectral channel density. *Laser Photonics Rev.* **19**, 2401987 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202401987)
   
4. Liu, Z. et al. Dual jones matrices empowered six phase channels modulation with single-layer monoatomic metasurfaces. *Laser Photonics Rev.* **19**, 2401526 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202401526)
   
5. Tang, F. et al. Metasurface spectrometers beyond resolution-sensitivity constraints. *Sci. Adv.* **10**, eadr7155 (2024). [*(paper)*](https://doi.org/10.1126/sciadv.adr7155)
   
6. Hao, H. et al. Single-shot 3d imaging meta-microscope. *Nano Lett.* **24**, 13364–13373 (2024). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c03952)
   
7. Yang, J. et al. Reconfigurable snapshot hyperspectral imaging sensor based on monochromatic pattern match of gradient geometry metasurface. *ACS Photonics* **11**, 3841–3851 (2024). [*(paper)*](https://doi.org/10.1021/acsphotonics.4c01136)
   
8. Cai, G. et al. Compact angle-resolved metasurface spectrometer. *Nat. Mater.* **23**, 71–78 (2024). [*(paper)*](https://doi.org/10.1038/s41563-023-01710-1)
   
9.  Zuo, J. et al. Metasurface-based mueller matrix microscope. *Adv. Funct. Mater.* **34**, 2405412 (2024). [*(paper)*](https://doi.org/10.1002/adfm.202405412)
    
10. Hu, Y. et al. Achromatic full stokes polarimetry metasurface for full-color polarization imaging in the visible range. *Nano Lett.* **24**, 13018–13026 (2024). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c03785)
    
11. Zaidi, A. et al. Metasurface-enabled single-shot and complete mueller matrix imaging. *Nat. Photonics* **18**, 704–712 (2024). [*(paper)*](https://doi.org/10.1038/s41566-024-01426-x)
    
12. Fan, Y. et al. Dispersion-assisted high-dimensional photodetector. *Nature* **630**, 70–83 (2024). [*(paper)*](https://doi.org/10.1038/s41586-024-07398-w)
    
13. Chakravarthula, P. et al. Thin on-sensor nanophotonic array cameras. *ACM Trans. Graph.* **42**, 1–18 (2023). [*(paper)*](https://doi.org/10.1145/3618398)
    
14. Fan, Q. et al. Disordered metasurface enabled single-shot full-Stokes polarization imaging leveraging weak dichroism. *Nat. Commun.* **14**, 7180 (2023). [*(paper)*](https://doi.org/10.1038/s41467-023-42944-6)
    
15. Zuo, J. et al. Chip-integrated metasurface full-Stokes polarimetric imaging sensor. *Light Sci. Appl.* **12**, 218 (2023). [*(paper)*](https://doi.org/10.1038/s41377-023-01260-w)
    
16. Kim, G. et al. Metasurface-driven full-space structured light for three-dimensional imaging. *Nat. Commun.* **13**, 5920 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-32117-2)
    
17. Jing, X. et al. Single-shot 3d imaging with point cloud projection based on metadevice. *Nat. Commun.* **13**, 7842 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-35483-z)
    
18. Xiong, J. et al. Dynamic brain spectrum acquired by a real-time ultraspectral imaging chip with reconfigurable metasurfaces. *Optica* **9**, 461–468 (2022). [*(paper)*](https://doi.org/10.1364/OPTICA.440013)
    
19. Makarenko, M. et al. Real-time hyperspectral imaging in hardware via trained metasurface encoders. In *Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 12692–12702 (IEEE, 2022). [*(paper)*](https://doi.org/10.1109/CVPR52688.2022.01236)
    
20. Bao, Y. et al. Observation of full-parameter jones matrix in bilayer metasurface. *Nat. Commun.* **13**, 7550 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-35313-2)
    
21. Ren, Y. et al. Full-stokes polarimetry for visible light enabled by an all-dielectric metasurface. *Adv. Photonics Res.* **3**, 2100373 (2022). [*(paper)*](https://doi.org/10.1002/adpr.202100373)
    
22. Hua, X. et al. Ultra-compact snapshot spectral light-field imaging. *Nat. Commun.* **13**, 2732 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-30439-9)
    
23. Zhang, C. et al. High efficiency all-dielectric pixelated metasurface for near-infrared full-stokes polarization detection. *Photonics Res.* **9**, 583–589 (2021). [*(paper)*](https://doi.org/10.1364/PRJ.415342)
    
24. Diebold, A. V. et al. Passive microwave spectral imaging with dynamic metasurface apertures. *Optica* **7**, 527–536 (2020). [*(paper)*](https://doi.org/10.1364/OPTICA.386516)
    
25. McClung, A. et al. Snapshot spectral imaging with parallel metasystems. *Sci. Adv.* **6**, eabc7646 (2020). [*(paper)*](https://doi.org/10.1126/sciadv.abc7646)
    
26. Lin, R. J. et al. Achromatic metalens array for full-colour light-field imaging. *Nat. Nanotechnol.* **14**, 227–231 (2019). [*(paper)*](https://doi.org/10.1038/s41565-018-0347-0)
    
27. Faraji-Dana, M. et al. Hyperspectral imager with folded metasurface optics. *Acs Photonics* **6**, 2161–2167 (2019). [*(paper)*](https://doi.org/10.1021/acsphotonics.9b00744)
    
28. Yesilkov, F. et al. Ultrasensitive hyperspectral imaging and biodetection enabled by dielectric metasurfaces. *Nat. Photonics* **13**, 390–396 (2019). [*(paper)*](https://doi.org/10.1038/s41566-019-0394-6)
    
29. Rubin, N. A. et al. Matrix fourier optics enables a compact full-Stokes polarization camera. *Science* **365**, eaax1839 (2019). [*(paper)*](https://doi.org/10.1126/science.aax1839)
    
30. Arbabi, E. et al. Full-stokes imaging polarimetry using dielectric metasurfaces. *Acs Photonics* **5**, 3132–3140 (2018). [*(paper)*](https://doi.org/10.1021/acsphotonics.8b00362)
    
31. Stewart, J. W. et al. Toward multispectral imaging with colloidal metasurface pixels. *Adv. Mater.* **29**, 1602971 (2017). [*(paper)*](https://doi.org/10.1002/adma.201602971)

---

### 6. Optical Feature Enhancement

![](assets/feature_enhancement.png)

1. Bi, X. et al. Concurrent image differentiation and integration processings enabled by polarization-multiplexed metasurface. *Laser Photonics Rev.* **19**, 2400718 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202400718)
   
2. Zhu, Y. et al. On-site quantitative detection of fentanyl in heroin by machine learning-enabled sensors on super absorbing metasurfaces. *npj Nanophotonics* **2**, 7 (2025). [*(paper)*](https://doi.org/10.1038/s44310-025-00055-8)
   
3. Swartz, B. T., Zheng, H., Forcherio, G. T. & Valentine, J. Broadband and large-aperture metasurface edge encoders for incoherent infrared radiation. *Sci. Adv.* **10**, eadk0024 (2024). [*(paper)*](https://doi.org/10.1126/sciadv.adk0024)
   
4. Meng, J., Balendhran, S., Sabri, Y., Bhargava, S. K. & Crozier, K. B. Smart mid-infrared metasurface microspectrometer gas sensing system. *Microsyst. Nanoeng.* **10**, 74 (2024). [*(paper)*](https://doi.org/10.1038/s41378-024-00697-2)
   
5. Tan, H., Meng, J. & Crozier, K. B. Multianalyte detection with metasurface-based midinfrared microspectrometer. *ACS Sens.* **9**, 5839–5847 (2024). [*(paper)*](https://doi.org/10.1021/acssensors.4c01220)
   
6. He, C. et al. Pluggable multitask diffractive neural networks based on cascaded metasurfaces. *Opto-Electron. Adv.* **7**, 230005 (2024). [*(paper)*](https://doi.org/10.29026/oea.2024.230005)
   
7. Tanriover, I., Dereshgi, S. A. & Aydin, K. Metasurface enabled broadband all optical edge detection in visible frequencies. *Nat. Commun.* **14**, 6484 (2023). [*(paper)*](https://doi.org/10.1038/s41467-023-42271-w)
   
8. Wang, S. et al. Metalens for accelerated optoelectronic edge detection under ambient illumination. *Nano Lett.* **24**, 356–361 (2023). [*(paper)*](https://doi.org/10.1021/acs.nanolett.3c04112)
   
9.  Xu, D. et al. All-optical object identification and three-dimensional reconstruction based on optical computing metasurface. *Opto-Electron. Adv.* **6**, 230120 (2023). [*(paper)*](https://doi.org/10.29026/oea.2023.230120)
    
10. Yang, S. et al. Realizing depth measurement and edge detection based on a single metasurface. *Nanophotonics* **12**, 3385–3393 (2023). [*(paper)*](https://doi.org/10.1515/nanoph-2023-0308)
    
11. Qu, G. et al. All-dielectric metasurface empowered optical-electronic hybrid neural networks. *Laser Photonics Rev.* **16**, 2100732 (2022). [*(paper)*](https://doi.org/10.1002/lpor.202100732)
    
12. Wang, H. P. et al. Noncontact electromagnetic wireless recognition for prosthesis based on intelligent metasurface. *Adv. Sci.* **9**, 2105056 (2022). [*(paper)*](https://doi.org/10.1002/advs.202105056)
    
13. Zhou, Y., Zheng, H., Kravchenko, I. I. & Valentine, J. Flat optics for image differentiation. *Nat. Photonics* **14**, 316–323 (2020). [*(paper)*](https://doi.org/10.1038/s41566-020-0591-3)
    
14. Weng, J. et al. Meta-neural-network for real-time and passive deep-learning-based object recognition. *Nat. Commun.* **11**, 6309 (2020). [*(paper)*](https://doi.org/10.1038/s41467-020-19693-x)
    
15. Zhou, J. et al. Optical edge detection based on high-efficiency dielectric metasurface. *Proc. Natl. Acad. Sci. USA* **116**, 11137–11140 (2019). [*(paper)*](https://doi.org/10.1073/pnas.1820636116)
    
16. Li, L. et al. Intelligent metasurface imager and recognizer. *Light Sci. Appl.* **8**, 97 (2019). [*(paper)*](https://doi.org/10.1038/s41377-019-0209-z)
    
17. Li, L. et al. Machine-learning reprogrammable metasurface imager. *Nat. Commun.* **10**, 1082 (2019). [*(paper)*](https://doi.org/10.1038/s41467-019-09103-2)
    
18. Miyazaki, H. et al. Dual-band infrared metasurface thermal emitter for CO2 sensing. *Appl. Phys. Lett.* **105**, 121107 (2014). [*(paper)*](https://doi.org/10.1063/1.4896545)

---

### 7. Holographic Field Reconstruction

![](assets/holographic_field_reconstruction.png)

1. Aththanayake, A. et al. Tunable holographic metasurfaces for augmented and virtual reality. *Nanophotonics* (2025). [*(paper)*](https://doi.org/10.1515/nanoph-2024-0734)
   
2. Jue, J. et al. Three-photon direct laser writing of the qd-polymer metasurface for large field-of-view optical holography. *ACS Appl. Mater. Interfaces* **17**, 14520–14526 (2025). [*(paper)*](https://doi.org/10.1021/acsami.4c21233)
   
3. Meng, W. et al. Ultranarrow-linewidth wavelength-vortex metasurface holography. *Sci. Adv.* **11**, eadl9159 (2025). [*(paper)*](https://doi.org/10.1126/sciadv.adt9159)
   
4. Yin, Y. et al. Color holographic display based on complex-amplitude metasurface. *Laser Photonics Rev.* **19**, 2400884 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202400884)
   
5. Sun, J. & Li, T. Cascaded metalenses boost applications in near-eye display. *Light Sci. Appl.* **14**, 58 (2025). [*(paper)*](https://doi.org/10.1038/s41377-024-01699-5)
   
6. Rao, R., Shi, Y., Wang, Z., Wan, S. & Li, Z. On-chip cascaded metasurfaces for visible wavelength division multiplexing and color-routing meta-display. *Nano Lett.* **25**, 2452–2458 (2025). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c05946)
   
7. Gopakumar, M. et al. Full-colour 3d holographic augmented-reality displays with metasurface waveguides. *Nature* **629**, 791–797 (2024). [*(paper)*](https://doi.org/10.1038/s41586-024-07386-0)
   
8. Sun, S. et al. High-efficiency, broadband, and low-crosstalk 3d holography by multi-layer holographic-lens integrated metasurface. *APL Photonics* **9**, 086102 (2024). [*(paper)*](https://doi.org/10.1063/5.0218862)
   
9.  Yin, Y. et al. Multi-dimensional multiplexed metasurface holography by inverse design. *Adv. Mater.* **36**, 2312303 (2024). [*(paper)*](https://doi.org/10.1002/adma.202312303)
    
10. Wang, D. et al. Decimeter-depth and polarization addressable color 3d meta-holography. *Nat. Commun.* **15**, 8242 (2024). [*(paper)*](https://doi.org/10.1038/s41467-024-52267-9)
    
11. Zhang, J. C. et al. Programmable optical meta-holograms. *Nanophotonics* **13**, 1201–1217 (2024). [*(paper)*](https://doi.org/10.1515/nanoph-2023-0544)
    
12. Li, Z., Shi, Y., Dai, C. & Li, Z. On-chip-driven multicolor 3d meta-display. *Laser Photonics Rev.* **18**, 2301240 (2024). [*(paper)*](https://doi.org/10.1002/lpor.202301240)
    
13. Fan, Z.-B. et al. Integral imaging near-eye 3d display using a nanoimprint metalens array. *eLight* **4**, 3 (2024). [*(paper)*](https://doi.org/10.1186/s43593-023-00055-1)
    
14. Liu, Z. et al. Metasurface-enabled augmented reality display: a review. *Adv. Photonics* **5**, 034001 (2023). [*(paper)*](https://doi.org/10.1117/1.AP.5.3.034001)
    
15. Li, Z. et al. Inverse design enables large-scale high-performance meta-optics reshaping virtual reality. *Nat. Commun.* **13**, 2409 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-29973-3)
    
16. Li, Y. et al. Ultracompact multifunctional metalens visor for augmented reality displays. *PhotonIX* **3**, 29 (2022). [*(paper)*](https://doi.org/10.1186/s43074-022-00075-z)
    
17. Kim, J. et al. Tunable metasurfaces towards versatile metalenses and metabolograms: a review. *Adv. Photonics* **4**, 024001 (2022). [*(paper)*](https://doi.org/10.1117/1.AP.4.2.024001)
    
18. Boo, H. et al. Metasurface wavefront control for high-performance user-natural augmented reality waveguide glasses. *Sci. Rep.* **12**, 5832 (2022). [*(paper)*](https://doi.org/10.1038/s41598-022-09680-1)
    
19. Li, Z. et al. Meta-optics achieves rgb-achromatic focusing for virtual reality. *Sci. Adv.* **7**, eabe4458 (2021). [*(paper)*](https://doi.org/10.1126/sciadv.abe4458)
    
20. Xiong, J., Hsiang, E.-L., He, Z., Zhan, T. & Wu, S.-T. Augmented reality and virtual reality displays: emerging technologies and future perspectives. *Light Sci. Appl.* **10**, 216 (2021). [*(paper)*](https://doi.org/10.1038/s41377-021-00658-8)
    
21. Georgi, P. et al. Optical secret sharing with cascaded metasurface holography. *Sci. Adv.* **7**, eabf9718 (2021). [*(paper)*](https://doi.org/10.1126/sciadv.abf9718)
    
22. Kim, I. et al. Pixelated bifunctional metasurface-driven dynamic vectorial holographic color prints for photonic security platform. *Nat. Commun.* **12**, 3614 (2021). [*(paper)*](https://doi.org/10.1038/s41467-021-23814-5)
    
23. Kim, J. et al. Geometric and physical configurations of meta-atoms for advanced metasurface holography. *InfoMat* **3**, 739–754 (2021). [*(paper)*](https://doi.org/10.1002/inf2.12191)
    
24. Xiong, B. et al. Realizing colorful holographic mimicry by metasurfaces. *Adv. Mater.* **33**, 2005864 (2021). [*(paper)*](https://doi.org/10.1002/adma.202005864)
    
25. Mu, Y., Zheng, M., Qi, J., Li, H. & Qiu, J. A large field-of-view metasurface for complex-amplitude hologram breaking numerical aperture limitation. *Nanophotonics* **9**, 4749–4759 (2020). [*(paper)*](https://doi.org/10.1515/nanoph-2020-0448)
    
26. Deng, Z.-L. et al. Full-color complex-amplitude vectorial holograms based on multi-freedom metasurfaces. *Adv. Funct. Mater.* **30**, 1910610 (2020). [*(paper)*](https://doi.org/10.1002/adfm.201910610)
    
27. Qu, G. et al. Reprogrammable meta-hologram for optical encryption. *Nat. Commun.* **11**, 5484 (2020). [*(paper)*](https://doi.org/10.1038/s41467-020-19312-9)
    
28. Jiang, Q., Jin, G. & Cao, L. When metasurface meets hologram: principle and advances. *Adv. Opt. Photonics* **11**, 518–576 (2019). [*(paper)*](https://doi.org/10.1364/AOP.11.000518)
    
29. Ren, H. et al. Metasurface orbital angular momentum holography. *Nat. Commun.* **10**, 2986 (2019). [*(paper)*](https://doi.org/10.1038/s41467-019-11030-1)
    
30. Hu, Y. et al. 3d-integrated metasurfaces for full-colour holography. *Light Sci. Appl.* **8**, 86 (2019). [*(paper)*](https://doi.org/10.1038/s41377-019-0198-y)
    
31. Lee, G.-Y. et al. Metasurface eyepiece for augmented reality. *Nat. Commun.* **9**, 4562 (2018). [*(paper)*](https://doi.org/10.1038/s41467-018-07011-5)
    
32. Li, J. et al. Addressing metasurfaces for dynamic holography and optical information encryption. *Sci. Adv.* **4**, eaaq6768 (2018). [*(paper)*](https://doi.org/10.1126/sciadv.aar6768)
    
33. Deng, Z.-L. & Li, G. Metasurface optical holography. *Mater. Today Phys.* **3**, 16–32 (2017). [*(paper)*](https://doi.org/10.1016/j.mtphys.2017.11.001)
    
34. Li, L. et al. Electromagnetic reprogrammable coding-metasurface holograms. *Nat. Commun.* **8**, 197 (2017). [*(paper)*](https://doi.org/10.1038/s41467-017-00164-9)
    
35. Wan, W., Gao, J. & Yang, X. Full-color plasmonic metasurface holograms. *ACS Nano* **10**, 10671–10680 (2016). [*(paper)*](https://doi.org/10.1021/acsnano.6b05453)
    
36. Wang, B. et al. Wavelength de-multiplexing metasurface hologram. *Sci. Rep.* **6**, 35657 (2016). [*(paper)*](https://doi.org/10.1038/srep35657)

---

### 8. Functional Integration

![](assets/functional_integration.png)

1. Li, F. et al. Flexible intelligent microwave metasurface with shape-guided adaptive programming. *Nat. Commun.* **16**, 3161 (2025). [*(paper)*](https://doi.org/10.1038/s41467-025-58249-9)
   
2. Yang, G. et al. Nonlocal phase-change meta-optics for reconfigurable nonvolatile image processing. *Light Sci. Appl.* **14**, 1–10 (2025). [*(paper)*](https://doi.org/10.1038/s41377-025-01841-x)
   
3. Xing, Z. et al. Monolithic spin-multiplexing metalens for dual-functional imaging. *Laser Photonics Rev.* **19**, 2401993 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202401993)

4. Sulejman, S. B. et al. Metasurfaces for infrared multimodal microscopy: phase contrast and bright field. *ACS Photonics* **12**, 1494–1506 (2025). [*(paper)*](https://doi.org/10.1021/acsphotonics.4c02097)
   
5. Li, N., Zhang, J., Neshev, D. N. & Sukhorukov, A. A. Angle multifunctional dichroism in metasurfaces. *ACS Photonics* **12**, 1441–1447 (2025). [*(paper)*](https://doi.org/10.1021/acsphotonics.4c01999)
   
6. Zhou, Y. et al. Flexible metasurfaces for multifunctional interfaces. *ACS Nano* **18**, 2685–2707 (2024). [*(paper)*](https://doi.org/10.1021/acsnano.3c09310)
   
7. Guo, S. et al. Multifunctional metasurface: Holography and spot cloud projection. *Adv. Opt. Mater.* **12**, 2401235 (2024). [*(paper)*](https://doi.org/10.1002/adom.202401235)
   
8. Wang, Y. et al. Detection and anti-detection with microwave-infrared compatible camouflage using asymmetric composite metasurface. *Adv. Sci.* **11**, 2410364 (2024). [*(paper)*](https://doi.org/10.1002/advs.202410364)
   
9.  Armghan, A. et al. A high-performance ultra-wideband metasurface absorber and thermal emitter for solar energy harvesting and thermal applications. *Phys. Chem. Chem. Phys.* **26**, 25469–25479 (2024). [*(paper)*](https://doi.org/10.1039/D4CP03336A)
    
10. Zhang, Z. et al. Multifunctional ultrathin metasurface with a low radar cross section and variable infrared emissivity. *ACS Appl. Mater. Interfaces* **16**, 21109–21117 (2024). [*(paper)*](https://doi.org/10.1021/acsami.4c01798)
    
11. Yang, X., Wen, E., Bharadia, D. & Sievenpiper, D. F. Multifunctional metasurface: simultaneous beam steering, polarization conversion and phase offset. *IEEE Trans. Antennas Propag.* **72**, 4589–4593 (2024). [*(paper)*](https://doi.org/10.1109/TAP.2024.3371697)
    
12. Dong, L. et al. Metasurface-enhanced multifunctional flag nanogenerator for efficient wind energy harvesting and environmental sensing. *Nano Energy* **124**, 109508 (2024). [*(paper)*](https://doi.org/10.1016/j.nanoen.2024.109508)
    
13. Ji, J. et al. On-chip multifunctional metasurfaces with full-parametric multiplexed jones matrix. *Nat. Commun.* **15**, 8271 (2024). [*(paper)*](https://doi.org/10.1038/s41467-024-52476-2)[*(data)*](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-52476-2/MediaObjects/41467_2024_52476_MOESM3_ESM.rar)
    
14. Dai, C., Liu, T., Wang, D. & Zhou, L. Multiplexing near-and far-field functionalities with high-efficiency bi-channel metasurfaces. *PhotonIX* **5**, 11 (2024). [*(paper)*](https://doi.org/10.1186/s43074-024-00128-5)
    
15. Yu, S. et al. Dynamic nonlocal metasurface for multifunctional integration via phase-change materials. *Nanophotonics* **13**, 4317–4325 (2024). [*(paper)*](https://doi.org/10.1515/nanoph-2024-0357)
    
16. Chen, M. K. et al. A meta-device for intelligent depth perception. *Adv. Mater.* **35**, 2107465 (2023). [*(paper)*](https://doi.org/10.1002/adma.202107465)
    
17. Lan, F. et al. Real-time programmable metasurface for terahertz multifunctional wave front engineering. *Light Sci. Appl.* **12**, 191 (2023). [*(paper)*](https://doi.org/10.1038/s41377-023-01228-w)
    
18. Intaravanne, Y. et al. Metasurface-enabled 3-in-1 microscopy. *ACS photonics* **10**, 544–551 (2023). [*(paper)*](https://doi.org/10.1021/acsphotonics.2c01971)
    
19. Abdollahramezani, S. et al. Reconfigurable multifunctional metasurfaces employing hybrid phase-change plasmonic architecture. *Nanophotonics* **11**, 3883–3893 (2022). [*(paper)*](https://doi.org/10.1515/nanoph-2022-0271)
    
20. Du, K. et al. Optical metasurfaces towards multifunctionality and tunability. *Nanophotonics* **11**, 1761–1781 (2022). [*(paper)*](https://doi.org/10.1515/nanoph-2021-0684)
    
21. Tonkaev, P. et al. Multifunctional and transformative metaphotonics with emerging materials. *Chem. Rev.* **122**, 15414–15449 (2022). [*(paper)*](https://doi.org/10.1021/acs.chemrev.1c01029)
    
22. Xu, X. et al. Multifunctional metamaterials for energy harvesting and vibration control. *Adv. Funct. Mater.* **32**, 2107896 (2022). [*(paper)*](https://doi.org/10.1002/adfm.202107896)
    
23. Zhang, J., Shao, L., Li, Z., Zhang, C. & Zhu, W. Graphene-based optically transparent metasurface capable of dual-polarized modulation for electromagnetic stealth. *ACS Appl. Mater. Interfaces* **14**, 31075–31084 (2022). [*(paper)*](https://doi.org/10.1021/acsami.2c04414)
    
24. Liu, M. et al. Multifunctional metasurfaces enabled by simultaneous and independent control of phase and amplitude for orthogonal polarization states. *Light Sci. Appl.* **10**, 107 (2021). [*(paper)*](https://doi.org/10.1038/s41377-021-00552-3)
    
25. Shirmanesh, G. K., Sokhoyan, R., Wu, P. C. & Atwater, H. A. Electro-optically tunable multifunctional metasurfaces. *ACS Nano* **14**, 6912–6920 (2020). [*(paper)*](https://doi.org/10.1021/acsnano.0c01269)
    
26. Chen, S., Liu, W., Li, Z., Cheng, H. & Tian, J. Metasurface-empowered optical multiplexing and multifunction. *Adv. Mater.* **32**, 1805912 (2020). [*(paper)*](https://doi.org/10.1002/adma.201805912)
    
27. Shabanpour, J., Beyraghi, S. & Cheldavi, A. Ultrafast reprogrammable multifunctional vanadium-dioxide-assisted metasurface for dynamic thz wavefront engineering. *Sci. Rep.* **10**, 8950 (2020). [*(paper)*](https://doi.org/10.1038/s41598-020-65533-9)
    
28. Kwon, H. et al. Single-shot quantitative phase gradient microscopy using a system of multifunctional metasurfaces. *Nat. Photonics* **14**, 109–114 (2020). [*(paper)*](https://doi.org/10.1038/s41566-019-0536-x)
    
29. Chu, H. et al. A hybrid invisibility cloak based on integration of transparent metasurfaces and zero-index materials. *Light Sci. Appl.* **7**, 50 (2018). [*(paper)*](https://doi.org/10.1038/s41377-018-0052-7)
    
30. Ee, H.-S. & Agarwal, R. Tunable metasurface and flat optical zoom lens on a stretchable substrate. *Nano Lett.* **16**, 2818–2823 (2016). [*(paper)*](https://doi.org/10.1021/acs.nanolett.6b00618)
    

---

### 9. Compact Device Integration

![](assets/compact_device_integration.png) 

1.  Bao, Y. & Li, B. Single-shot simultaneous intensity, phase, and polarization imaging with metasurface. *Natl. Sci. Rev.* **12**, nwae418 (2025). [*(paper)*](https://doi.org/10.1093/nsr/nwae418)
   
2.  Chi, H. et al. Neural network-assisted end-to-end design for full light field control of meta-optics. *Adv. Mater.* **37**, 2419621 (2025). [*(paper)*](https://doi.org/10.1002/adma.202419621)
   
3.  Wen, S. et al. Metasurface array for single-shot spectroscopic ellipsometry. *Light Sci. Appl.* **13**, 88 (2024). [*(paper)*](https://doi.org/10.1038/s41377-024-01396-3)
   
4.  Yin, Y. et al. Multi-dimensional multiplexed metasurface holography by inverse design. *Adv. Mater.* **36**, 2312303 (2024). [*(paper)*](https://doi.org/10.1002/adma.202312303)
   
5.  Seo, J. et al. Deep-learning-driven end-to-end metalens imaging. *Adv. Photonics* **6**, 066002 (2024). [*(paper)*](https://doi.org/10.1117/1.AP.6.6.066002) [*(data)*](https://github.com/yhy258/EIDL_DRMI) [*(code)*](https://github.com/yhy258/EIDL_DRMI)
   
6.  Zuo, J. et al. Chip-integrated metasurface full-Stokes polarimetric imaging sensor. *Light Sci. Appl.* **12**, 218 (2023). [*(paper)*](https://doi.org/10.1038/s41377-023-01260-w)
   
7.  Cao, G. et al. Infrared metasurface-enabled compact polarization nanodevices. *Mater. Today* **50**, 499–515 (2023). [*(paper)*](https://doi.org/10.1016/j.mattod.2021.06.014)
   
8.  Chen, M. K. et al. A meta-device for intelligent depth perception. *Adv. Mater.* **35**, 2107465 (2023). [*(paper)*](https://doi.org/10.1002/adma.202107465)
   
9.  Xiong, J. et al. Dynamic brain spectrum acquired by a real-time ultraspectral imaging chip with reconfigurable metasurfaces. *Optica* **9**, 461–468 (2022). [*(paper)*](https://doi.org/10.1364/OPTICA.440013)
    
10.  Luo, X. et al. Metasurface-enabled on-chip multiplexed diffractive neural networks in the visible. *Light Sci. Appl.* **11**, 158 (2022). [*(paper)*](https://doi.org/10.1038/s41377-022-00844-2)
    
11.  Hua, X. et al. Ultra-compact snapshot spectral light-field imaging. *Nat. Commun.* **13**, 2732 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-30439-9)
    
12.  Reshef, O. et al. An optic to replace space and its application towards ultra-thin imaging systems. *Nat. Commun.* **12**, 3512 (2021). [*(paper)*](https://doi.org/10.1038/s41467-021-23358-8)
    
13.  Xu, B. et al. Metalens-integrated compact imaging devices for wide-field microscopy. *Adv. Photonics* **2**, 066004 (2020). [*(paper)*](https://doi.org/10.1117/1.AP.2.6.066004)
    
14.  Joo, W.-J. et al. Metasurface-driven OLED displays beyond 10,000 pixels per inch. *Science* **370**, 459–463 (2020). [*(paper)*](https://doi.org/10.1126/science.abc8530)
    
15.  Pahlevaninezhad, H. et al. Nano-optic endoscope for high-resolution optical coherence tomography in vivo. *Nat. Photonics* **12**, 540–547 (2018). [*(paper)*](https://doi.org/10.1038/s41566-018-0224-2)
    
16.  Colburn, S., Zhan, A. & Majumdar, A. Metasurface optics for full-color computational imaging. *Sci. Adv.* **4**, eaar2114 (2018). [*(paper)*](https://doi.org/10.1126/sciadv.aar2114)

## 📖 How to Cite

If you find this repository useful, please leave a star⭐️⭐️⭐️ and cite our paper:

> Zeng, Y., Zhong, H., Long, Z. *et al.* From performance to structure: a comprehensive survey of advanced metasurface design for next-generation imaging. *npj Nanophoton.* **2**, 39 (2025). https://doi.org/10.1038/s44310-025-00081-6

If you are preparing a manuscript or report in **LaTeX**, you can add the following **BibTeX** entry to your bibliography file:

#### BibTeX

```bibtex
@article{Zeng2025_PerformanceToStructure,
  author    = {Yunhui Zeng and Haopeng Zhong and Zhenwei Long and Hongkun Cao and Xin Jin},
  title     = {From performance to structure: a comprehensive survey of advanced metasurface design for next-generation imaging},
  journal   = {npj Nanophotonics},
  year      = {2025},
  volume    = {2},
  pages     = {39},        
  doi       = {10.1038/s44310-025-00081-6},
  url       = {https://doi.org/10.1038/s44310-025-00081-6},
  publisher = {Nature Publishing Group}
}

```

---

<!-- 🌍 Global Visitors Map -->
<h2>🌍 Global Visitors Map</h2>
<p align="center">
  <script type="text/javascript" id="mapmyvisitors"
          src="//mapmyvisitors.com/map.js?d=PzyEtwqPyPFjmE0owZKvAmJsED72r2KZTHHmqZp9NBQ&cl=ffffff&w=a">
  </script>
</p>
