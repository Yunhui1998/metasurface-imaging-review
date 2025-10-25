
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
         src="abstract image/Planar wide-angle-imaging camera enabled by metalens array.jpg" 
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
        Wide-angle imaging is an important function in photography and projection, but it also places high demands on the design of the imaging components of a camera. To eliminate the coma caused by the focusing of large-angle incident light, traditional wide-angle camera lenses are composed of complex optical components. Here, we propose a planar camera for wide-angle imaging with a silicon nitride metalens array mounted on a CMOS image sensor. By carefully designing proper phase profiles for metalenses with intentionally introduced shifted phase terms, the whole lens array is capable of capturing a scene with a large viewing angle and negligible distortion or aberrations. After a stitching process, we obtained a large viewing angle image with a range of >120°using a compact planar camera. Our device demonstrates the advantages of metalenses in flexible phase design and compact integration, and the prospects for future imaging technology.
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
         src="abstract image/Thickness bound for nonlocal wide-field-of-view metalenses.png" 
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
        Metalenses—flat lenses made with optical metasurfaces—promise to enable thinner, cheaper, and better imaging systems. Achieving a sufficient angular field of view (FOV) is crucial toward that goal and requires a tailored incident-angle-dependent response. Here, we show that there is an intrinsic trade-off between achieving a desired broad-angle response and reducing the thickness of the device. Like the memory effect in disordered media, this thickness bound originates from the Fourier transform duality between space and angle. One can write down the transmission matrix describing the desired angle-dependent response, convert it to the spatial basis where its degree of nonlocality can be quantified through a lateral spreading, and determine the minimal device thickness based on such a required lateral spreading. This approach is general. When applied to wide-FOV lenses, it predicts the minimal thickness as a function of the FOV, lens diameter, and numerical aperture. The bound is tight, as some inverse-designed multi-layer metasurfaces can approach the minimal thickness we found. This work offers guidance for the design of nonlocal metasurfaces, proposes a new framework for establishing bounds, and reveals the relation between angular diversity and spatial footprint in multi-channel systems.
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
         src="abstract image/Imaging properties of large field-of-view quadratic metalenses and their applications to fingerprint detection.gif" 
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
        NDielectric metasurfaces, extremely thin nanostructured dielectric surfaces, hold promise to replace conventional refractive optics, such as lenses, due to their high performance and compactness. However, designing large field-of-view (FOV) metalenses, which are of particular importance when imaging relatively big objects at short distances, remains one of the most critical challenges. Recently, metalenses implementing a quadratic phase profile have been put forward to solve this problem with a single element, but despite their theoretical ability to provide 180° FOV, imaging over very large FOV has not been demonstrated yet. In this work, we provide an in-depth analysis of the imaging properties of quadratic metalenses and, in particular, show that due to their intrinsic barrel distortion or fish-eye effect, there is a fundamental trade-off between the FOV achievable in a given imaging configuration and the optical resolution of the metalens and/or the detector resolution. To illustrate how to harness the full potential of quadratic metalenses, we apply these considerations to the fingerprint detection problem and demonstrate experimentally the full imaging of a 5 mm fingerprint with features of the order of 100 μm, with a metalens ten times smaller in size and located at a distance of only 2.5 mm away from the object. This constitutes the most compact imaging system reported so far for fingerprint detection.
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
         src="abstract image/Single-element diffraction-limited fisheye metalens.jpeg" 
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
        Wide field-of-view (FOV) optical functionality is crucial for implementation of advanced imaging and image projection devices. Conventionally, wide FOV operation is attained with complicated assembly of multiple optical elements known as “fisheye lenses”. Here we present a novel metalens design capable of performing diffraction-limited focusing and imaging over an unprecedented near 180° angular FOV. The lens is monolithically integrated on a one-piece flat substrate and involves only a single layer of metasurface that corrects third-order Seidel aberrations including coma, astigmatism, and field curvature. The metalens further features a planar focal surface, which enables considerably simplified system architectures for applications in imaging and projection. We fabricated the metalens using Huygens meta-atoms operating at 5.2 μm wavelength and experimentally demonstrated aberration-free focusing and imaging over the entire FOV. The design concept is generic and can be readily adapted to different meta-atom geometries and wavelength ranges to meet diverse application demands.
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
         src="abstract image/Single-layer aberration-compensated flat lens for robust wide-angle imaging.jpg" 
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
        Metasurfaces are planarized and miniaturized versions of conventional optical elements. Subwavelength-thick single-layer metalenses have diffraction limited resolution for on-axis imaging but relatively low resolution for off-axis imaging due to off-axial aberrations. The aberrations of planar single-layer metalenses have been corrected by patterning two metasurfaces on both sides of a substrate to form metalens doublets with a thickness of hundreds of micrometers to millimeters. The multilevel diffractive lenses are demonstrated to achieve wide angle imaging with a thickness of several micrometers, however, the off-axial aberrations are not compensated. Here, an epsilon-greedy algorithm-based scheme for achieving a planar wavelength-thick single-layer aberration-compensated (SLAC) flat lens consisting of dielectric nanoring structures fabricated by 3D printing are proposed. The scheme is experimentally validated via a SLAC flat lens. This SLAC flat lens has a thickness of 1 µm, a numerical aperture of 0.45, a focal length of 1 mm, a full field of view (FOV) of 32° that enables aberration-compensated imaging along the focal plane and monochromatic microscopic imaging with resolution better than 2.2 µm at a wavelength of 633 nm. This scheme can lead to ultrathin wide-FOV flat lens designs as well as low-cost mass production, which has various applications in miniscopes, mobile camera modules, and machine vision.
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
         src="abstract image/On metalenses with arbitrarily wide field of view.jpeg" 
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
        Metalenses are nanostructured surfaces that mimic the functionality of optical elements. Many exciting demonstrations have already been made, for example, focusing into diffraction-limited spots or achromatic operation over a wide wavelength range. The key functionality that is yet missing, however, and that is most important for applications such as smartphones or virtual reality, is the ability to perform the imaging function with a single element over a wide field of view. Here, by relaxing the constraint on diffraction-limited resolution, we demonstrate the ability of single-layer metalenses to perform wide field of view (WFOV) imaging while maintaining high resolution suitable for most applications. We also discuss the WFOV physical properties and, in particular, we show that such a WFOV metalens mimics a spherical lens in the limit of infinite radius and infinite refractive index. Finally, we use Fourier analysis to explain the dependence of the FOV on the numerical aperture.
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
         src="abstract image/Metalens-integrated compact imaging devices for wide-field microscopy.png" 
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
        Metasurfaces have demonstrated unprecedented capabilities in manipulating light with ultrathin and flat architectures. Although great progress has been made in the metasurface designs and function demonstrations, most metalenses still only work as a substitution of conventional lenses in optical settings, whose integration advantage is rarely manifested. We propose a highly integrated imaging device with silicon metalenses directly mounted on a complementary metal oxide semiconductor image sensor, whose working distance is in hundreds of micrometers. The imaging performances including resolution, signal-to-noise ratio, and field of view (FOV) are investigated. Moreover, we develop a metalens array with polarization-multiplexed dual-phase design for a wide-field microscopic imaging. This approach remarkably expands the FOV without reducing the resolution, which promises a non-limited space-bandwidth product imaging for wide-field microscopy. As a result, we demonstrate a centimeter-scale prototype for microscopic imaging, showing uniqueness of meta-design for compact integration.
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
         src="abstract image/Near-IR wide-field-of-view huygens metalens for outdoor imaging applications.jpg" 
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
        The ongoing effort to implement compact and cheap optical systems is the main driving force for the recent flourishing research in the field of optical metalenses. Metalenses are a type of metasurface, used for focusing and imaging applications, and are implemented based on the nanopatterning of an optical surface. The challenge faced by metalens research is to reach high levels of performance using simple fabrication methods suitable for mass production. In this paper, we present a Huygens nanoantenna-based metalens, designed for outdoor photographic/surveillance applications in the near infrared. We show that good imaging quality can be obtained over a field of view as large as ±15°. This first successful implementation of metalenses for outdoor imaging applications is expected to provide insight and inspiration for future metalens imaging applications.
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
         src="abstract image/Ultrawide-angle and high-efficiency metalens in hexagonal arrangement.png" 
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
        Wide-angle optical systems play a vital role in imaging applications and have been researched for many years. In traditional lenses, attaining a wide field of view (FOV) by using a single optical component is difficult because these lenses have crucial aberrations. In this study, we developed a wide-angle metalens with a numerical aperture of 0.25 that provided a diffraction-limited FOV of over 170° for a wavelength of 532 nm without the need for image stitching or multiple lenses. The designed wide-angle metalens is free of aberration and polarization, and its full width of half maximum is close to the diffraction limit at all angles. Moreover, the metalens which is designed through a hexagonal arrangement exhibits higher focusing efficiency at all angles than most-seen square arrangement. The focusing efficiencies are as high as 82% at a normal incident and 45% at an incident of 85°. Compared with traditional optical components, the proposed metalens exhibits higher FOV and provides a more satisfactory image quality because of aberration correction. Because of the advantages of the proposed metalens, which are difficult to achieve for a traditional single lens, it has the potential to be applied in camera systems and virtual and augmented reality.
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
         src="abstract image/Meta-lens doublet in the visible region.jpeg" 
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
        Recently, developments in meta-surfaces have allowed for the possibility of a fundamental shift in lens manufacturing—from the century-old grinding technology to nanofabrication—opening a way toward mass producible high-end meta-lenses. Inspired by early camera lenses and to overcome the aberrations of planar single-layered meta-lenses, we demonstrate a compact meta-lens doublet by patterning two metasurfaces on both sides of a substrate. This meta-lens doublet has a numerical aperture of 0.44, a focal length of 342.5 μm, and a field of view of 50° that enables diffraction-limited monochromatic imaging along the focal plane at a wavelength of 532 nm. The compact design has various imaging applications in microscopy, machine vision, and computer vision.
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
         src="abstract image/Miniature optical planar camera based on a wide-angle metasurface doublet corrected for monochromatic aberrations.png" 
         alt="Graphical abstract"s
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
        Optical metasurfaces are two-dimensional arrays of nano-scatterers that modify optical wavefronts at subwavelength spatial resolution. They are poised to revolutionize optics by enabling complex low-cost systems where multiple metasurfaces are lithographically stacked and integrated with electronics. For imaging applications, metasurface stacks can perform sophisticated image corrections and can be directly integrated with image sensors. Here we demonstrate this concept with a miniature flat camera integrating a monolithic metasurface lens doublet corrected for monochromatic aberrations, and an image sensor. The doublet lens, which acts as a fisheye photographic objective, has a small f-number of 0.9, an angle-of-view larger than 60° × 60°, and operates at 850 nm wavelength with 70% focusing efficiency. The camera exhibits nearly diffraction-limited image quality, which indicates the potential of this technology in the development of optical systems for microscopy, photography, and computer vision.
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
         src="abstract image/ultifaceted control of focal points along an arbitrary 3d curved trajectory.png" 
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
       Metalenses can integrate the functionalities of multiple optical components thanks to the unprecedented capability of optical metasurfaces in light control. With the rapid development of optical metasurfaces, metalenses continue to evolve. Polarization and color play a very important role in understanding optics and serve as valuable tools for gaining insights into our world. Benefiting from the design flexibility of metasurfaces, we propose and experimentally demonstrate a super metalens that can realize multifaceted control of focal points along any 3D curved trajectory. The wavelengths and polarization states of all focal points are engineered in a desirable manner. The super metalens can simultaneously realize customized 3D positioning, polarization states, and wavelengths of focal points, which are experimentally demonstrated with incident wavelengths ranging from 501 to 700 nm. We further showcase the application of the developed super metalenses in 3D optical distance measurement. The compact nature of metasurfaces and unique properties of the proposed super metalenses hold promise to dramatically miniaturize and simplify the optical architecture for applications in optical metrology, imaging, detection, and security.
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
         src="abstract image/Underwater binocular meta-lens.gif" 
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
       Underwater optics in all-aquatic environments is vital for environmental management, biogeochemistry, phytoplankton ecology, benthic processes, global change, etc. Many optical techniques of observational systems for underwater sensing, imaging, and applications have been developed. For the demands of compact, miniaturized, portable, lightweight, and low-energy consumption, a novel underwater binocular depth-sensing and imaging meta-optic device is developed and reported here. A GaN binocular meta-lens is specifically designed and fabricated to demonstrate underwater stereo vision and depth sensing. The diameter of each meta-lens is 2.6 mm, and the measured distance between the two meta-lens centers is 4.04 mm. The advantage of our binocular meta-lens is no need of distortion correction or camera calibration, which is necessary for traditional two-camera stereo vision systems. Based on the experimental results, we developed the generalized depth calculation formula for all-size binocular vision systems. With deep-learning support, this stereo vision system can realize the fast underwater object’s depth and image computation for real-time processing capability. Our artificial intelligent imaging results show that depth measurement accuracy is down to 50 μm. Besides the aberration-free advantage of flat meta-optic components, the intrinsic superhydrophobicity properties of our nanostructured GaN meta-lens enable an antiadhesion, stain-resistant, and self-cleaning novel underwater imaging device. This stereo vision binocular meta-lens will significantly benefit underwater micro/nanorobots, autonomous submarines, machine vision in the ocean, marine ecological surveys, etc.
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
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Research and design of a metasurface with an extended depth of focus in the near field.jpg" 
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
       A metasurface with an extended depth of focus has broad application prospects in security detection. However, in the near field, the simulation results obtained by using traditional methods to achieve an extended depth of focus have a significant deviation from the preset value. This paper discusses the relationship between the depth of focus and focusing position, and the reason why the simulation results deviate from the preset focus position in the radial modulation method.  The angle modulation method is found by a simulation. A more accurate method for an extended depth of focus was proposed by combining the radial modulation method with the quasi-optical path principle. Finally, a polarization-insensitive reflective metasurface element was designed, and elements were arranged to form a polarization-insensitive focus between 150 and 400 mm based on the focusing effect settings. The simulation results indicate that the metasurface achieves the same focusing effect between 175 and 425 mm when different linear-polarization waves are incident. This focus is greater and more accurate than the radial modulation method under the same conditions, which indicates that the method is superior to the radial modulation method in the near-field region. The simulation verifies the accuracy of the method and shows potential application prospects in fields such as microwave imaging.
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
4.  Zhao, J. et al. Rapid cellular-resolution skin imaging with optical coherence tomography using all-glass multifocal metasurfaces. *ACS nano* **17**, 3442–3451 (2023). [*(paper)*](https://doi.org/10.1021/acsnano.2c09542)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Rapid cellular-resolution skin imaging with optical coherence tomography using all-glass multifocal metasurfaces.gif" 
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
       Cellular-resolution optical coherence tomography (OCT) is a powerful tool offering noninvasive histology-like imaging. However, like other optical microscopy tools, a high numerical aperture (N.A.) lens is required to generate a tight focus, generating a narrow depth of field, which necessitates dynamic focusing and limiting the imaging speed. To overcome this limitation, we developed a metasurface platform that generates multiple axial foci, which multiplies the volumetric OCT imaging speed by offering several focal planes. This platform offers accurate and flexible control over the number, positions, and intensities of axial foci generated. All-glass metasurface optical elements 8 mm in diameter are fabricated from fused-silica wafers and implemented into our scanning OCT system. With a constant lateral resolution of 1.1 μm over all depths, the multifocal OCT triples the volumetric acquisition speed for dermatological imaging, while still clearly revealing features of stratum corneum, epidermal cells, and dermal-epidermal junctions and offering morphological information as diagnostic criteria for basal cell carcinoma. The imaging speed can be further improved in a sparse sample, e.g., 7-fold with a seven-foci beam. In summary, this work demonstrates the concept of metasurface-based multifocal OCT for rapid virtual biopsy, further providing insights for developing rapid volumetric imaging systems with high resolution and compact volume.
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
5.  Shen, Z. et al. Monocular metasurface camera for passive single-shot 4d imaging. *Nat. Commun.* **14**, 1035 (2023). [*(paper)*](https://doi.org/10.1038/s41467-023-36812-6)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Monocular metasurface camera for passive single-shot 4d imaging.png" 
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
       It is a grand challenge for an imaging system to simultaneously obtain multi-dimensional light field information, such as depth and polarization, of a scene for the accurate perception of the physical world. However, such a task would conventionally require bulky optical components, time-domain multiplexing, and active laser illumination. Here, we experimentally demonstrate a compact monocular camera equipped with a single-layer metalens that can capture a 4D image, including 2D all-in-focus intensity, depth, and polarization of a target scene in a single shot under ambient illumination conditions. The metalens is optimized to have a conjugate pair of polarization-decoupled rotating single-helix point-spread functions that are strongly dependent on the depth of the target object. Combined with a straightforward, physically interpretable image retrieval algorithm, the camera can simultaneously perform high-accuracy depth sensing and high-fidelity polarization imaging over an extended depth of field for both static and dynamic scenes in both indoor and outdoor environments. Such a compact multi-dimensional imaging system could enable new applications in diverse areas ranging from machine vision to microscopy.
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
6.  Zheng, Y. et al. Designing high-efficiency extended depth-of-focus metalens via topology-shape optimization. *Nanophotonics* **11**, 2967–2975 (2022). [*(paper)*](https://doi.org/10.1515/nanoph-2022-0183)
   
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Designing high-efficiency extended depth-of-focus metalens via topology-shape optimization.jpg" 
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
       Longitudinal optical field modulation is of critical importance in a wide range of applications, including optical imaging, spectroscopy, and optical manipulation. However, it remains a considerable challenge to realize a uniformly distributed light field with extended depth-of-focus. Here, a high-efficiency extended depth-of-focus metalens is proposed by adjoint-based topology-shape optimization approach, wherein the theoretical electric field intensity corresponding to a variable focal-length phase is utilized as the figure of merit. Using a dozen of metalens with random structure parameters as initial structures, the average focal depth of topology-shape optimized metalens is greatly improved up to 18.80 μm (about 29.7λ), which is 1.54 times higher than the diffraction-limited focal depth. Moreover, all the topology-shape optimized metalens exhibit high diffraction efficiency exceeding 0.7 over the whole focal depth range, which is approximately three times greater than that of the forward design. Our results offer a new insight into the design of extended depth-of-focus metalens and may find potential applications in imaging, holography, and optical fabrication.
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
7.  Zheng, R. et al. Active multiband varifocal metalens based on orbital angular momentum division multiplexing. *Nat. Commun.* **13**, 4292 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-32044-2)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Active multiband varifocal metalens based on orbital angular momentum division multiplexing.png" 
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
       Metalenses as miniature flat lenses exhibit a substantial potential in replacing traditional optical component. Although the metalenses have been intensively explored, their functions are limited by poor active ability, narrow operating band and small depth of field (DOF). Here, we show a dielectric metalens consisting of TiO2 nanofins array with ultrahigh aspect ratio to realize active multiband varifocal function. Regulating the orbital angular momentum (OAM) by the phase assignment covering the 2π range, its focal lengths can be switched from 5 mm to 35 mm. This active optical multiplexing uses the physical properties of OAM channels to selectively address and decode the vortex beams. The multiband capability and large DOFs with conversion efficiency of 49% for this metalens are validated for both 532 nm and 633 nm, and the incidence wavelength can further change the focal lengths. This non-mechanical tunable metalens demonstrates the possibility of active varifocal metalenses.
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
8.  Fan, Q. et al. Triholite-inspired neural nanophotonic light-field camera with extreme depth-of-field. *Nat. Commun.* **13**, 2130 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-29568-y)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Triholite-inspired neural nanophotonic light-field camera with extreme depth-of-field.png" 
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
       A unique bifocal compound eye visual system found in the now extinct trilobite, Dalmanitina socialis, may enable them to be sensitive to the light-field information and simultaneously perceive both close and distant objects in the environment. Here, inspired by the optical structure of their eyes, we demonstrate a nanophotonic light-field camera incorporating a spin-multiplexed bifocal metalens array capable of capturing high-resolution light-field images over a record depth-of-field ranging from centimeter to kilometer scale, simultaneously enabling macro and telephoto modes in a snapshot imaging. By leveraging a multi-scale convolutional neural network-based reconstruction algorithm, optical aberrations induced by the metalens are eliminated, thereby significantly relaxing the design and performance limitations on metasurface optics. The elegant integration of nanophotonic technology with computational photography achieved here is expected to aid development of future high-performance imaging systems.
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
9.  Zhao, F. et al. Metalens-assisted system for underwater imaging. *Laser Photonics Rev.* **15**, 2100097 (2021). [*(paper)*](https://doi.org/10.1002/lpor.202100097)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metalens-assisted system for underwater imaging.jpg" 
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
       The ability to image under water is highly desirable for a variety of applications including biological monitoring and seafloor survey, yet the image quality is usually hampered by the presence of scattering medium in water. Polarization imaging has proven to be an effective method for image enhancement; however, conventional systems require mechanically rotating polarizers which compromises the system's footprint or a set of polarization filters which limits the system's efficiency. Here, a compact polarization imaging apparatus that leverages a multifunctional planar dielectric metalens to simultaneously capture two orthogonally polarized images of an underwater scene is presented. Using a metalens to image target objects through milky water in a single shot, large enhancement of image contrast and depth estimation of target objects in real-time are demonstrated. This work shows the effectiveness of metalens for tackling challenging imaging tasks in complex environments.
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
10.  Tan, S., Yang, F., Boominathan, V., Veeraraghavan, A. & Naik, G. V. 3d imaging using extreme dispersion in optical metasurfaces. *ACS Photonics* **8**, 1421–1429 (2021). [*(paper)*](https://doi.org/10.1021/acsphotonics.1c00110)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/3d imaging using extreme dispersion in optical metasurfaces.jpeg" 
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
       Metasurfaces have the potential to revolutionize imaging technologies due to their extreme control of phase, polarization, and amplitude of the incident light. They rely upon enhanced local interaction of light to achieve the desired phase profile. As a consequence of the enhanced local interaction of light, metasurfaces are highly dispersive. This strong dispersion has been recognized as a primary limitation as it relates to realizing conventional imaging with metasurfaces. Here, we argue that this strong dispersion is an added degree of design freedom for computational imaging, potentially opening up novel applications. In particular, we exploit this strongly dispersive property of metasurfaces to propose a compact, single-shot, and passive 3D imaging camera. Our device consists of a metalens engineered to focus different wavelengths at different depths and two deep networks to recover depth and RGB texture information from chromatic, defocused images acquired by the system. In contrast with other metasurface-based 3D sensors, our design can operate in the full visible range with a larger field-of-view (FOV) and can potentially generate dense depth maps of complicated 3D scenes. Our simulation results on a 1 mm diameter metalens demonstrate its ability to capture 3D depth and texture information ranging from 0.12 to 0.6 m.
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
11.  Bayati, E. et al. Inverse designed metalenses with extended depth of focus. *ACS Photonics* **7**, 873–878 (2020). [*(paper)*](https://doi.org/10.1021/acsphotonics.9b01703)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Inverse designed metalenses with extended depth of focus.jpeg" 
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
       Extended depth of focus (EDOF) lenses are important for various applications in computational imaging and microscopy. In addition to enabling novel functionalities, EDOF lenses can alleviate the need for stringent alignment requirements for imaging systems. Existing designs, however, are often inefficient or produce an asymmetric point spread function (PSF) that blurs images. Inverse design of nanophotonics, including metasurfaces, has generated strong interest in recent years owing to its potential for generating exotic and innovative optical elements, which are generally difficult to design based on intuition alone. Using adjoint optimization-based inverse electromagnetic design, in this paper, we designed a cylindrical metasurface lens operating at ∼625 nm with a depth of focus exceeding that of an ordinary lens. We validated our design by nanofabrication and optical characterization of silicon nitride metasurface lenses (with a lateral dimension of 66.66 μm) with three different focal lengths (66.66, 100, and 133.33 μm). The focusing efficiencies of the fabricated extended depth of focus metasurface lenses are similar to those of traditional metalenses.
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
12.  Zhang, Z., Yang, Q., Gong, M., Chen, M. & Long, Z. Metasurface lens with angular modulation for extended depth of focus imaging. *Opt. Lett.* **45**, 611–614 (2020). [*(paper)*](https://doi.org/10.1364/OL.382812)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface lens with angular modulation for extended depth of focus imaging1.jpg"
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
       The depth of focus (DOF) indicates the tolerance of the imaging displacement. The axial long-focal-depth is significant in practical applications, including optical imaging and communication. The importance of extending the DOF is rapidly growing with the advance of metasurface lenses. Angular modulation, as a promising way to extend the DOF, offers an additional degree of freedom to improve the imaging quality. Here we theoretically and experimentally demonstrate an angular modulated metasurface lens for extended DOF imaging by means of applying the geometrical phase. Unlike previous studies of the geometrical phase, which is sensitive to the polarity of circular polarization incidence, the polarity of circular polarization independence and broadband characteristic of angular modulation yield the potential of robust and efficient extension of the DOF imaging, thus providing novel opportunities for highly integrated optical circuits.
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
13.  Colburn, S. & Majumdar, A. Single-shot three-dimensional imaging with a metasurface depth camera. *arXiv preprint arXiv:1910.12111* (2019). [*(paper)*](https://arxiv.org/abs/1910.12111)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Single-shot three-dimensional imaging with a metasurface depth camera.png" 
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
       Depth imaging is vital for many emerging technologies with applications in augmented reality, robotics, gesture detection, and facial recognition. These applications, however, demand compact and low-power systems beyond the capabilities of state-of-the-art depth cameras. Here, we leverage ultrathin dielectric metasurfaces to demonstrate a solution that, with a single surface, replicates the functionality of a high-performance depth camera typically comprising a spatial light modulator, polarizer, and three lenses. Using cylindrical nano-scatterers that can arbitrarily modify the phase of an incident wavefront, our metasurface passively encodes two complementary optical responses to depth information in a scene with a single camera snapshot. By decoding the captured data in software, our system produces a fully reconstructed image and transverse depth map of three-dimensional scenes with a fractional ranging error of 1.7%. We demonstrate the first visible wavelength and polarization-insensitive metasurface depth camera, representing a significant form factor reduction for such systems.
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

### 4. Resolution Enhancement

![](assets/resolution_enhancement.png)  

1.  Basak, S. et al. Super-resolution optical fluctuation imaging. *Nat. Photonics* **19**, 229–237 (2025). [*(paper)*](https://doi.org/10.1038/s41566-024-01571-3)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Super-resolution optical fluctuation imaging.webp" 
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
       We present a comprehensive review of super-resolution optical fluctuation imaging (SOFI), a robust technique that leverages temporal fluctuations in fluorescence intensity to achieve super-resolution imaging without the need for single-molecule localization. The Review starts with a historical overview of super-resolution microscopy techniques, and then focuses on SOFI’s core principle—the analysis of intensity fluctuations using cumulants to improve spatial resolution. The paper discusses technical challenges, such as photobleaching, blinking kinetics and pixel size limitations, as well as proposing solutions like Fourier upsampling and balanced SOFI to mitigate these issues. Additionally, we discuss potential advancements in the field, including the integration of SOFI with other super-resolution modalities like structured illumination microscopy and image scanning microscopy, and the application of SOFI in cryo-fluorescence microscopy and quantum emitter-based imaging. This paper aims to serve as an essential resource for researchers interested in utilizing SOFI for high-resolution imaging in diverse biological applications.
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
2.  Zhou, Q. et al. Far-field phase-shifting structured light illumination enabled by polarization multiplexing metasurface for super-resolution imaging. *Nano Lett.* **24**, 11036–11042 (2024). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c03142)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Far-field phase-shifting structured light illumination enabled by polarization multiplexing metasurface for super-resolution imaging.jpeg" 
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
       The phase-shifting structured light illumination technique is widely used in imaging but often relies on mechanical translation stages or spatial light modulators, leading to system instability, low displacement accuracy, and limited integration feasibility. In response to these challenges, we propose and demonstrate an approach for generating far-field phase-shifting structured light using a polarization multiplexing metasurface. By controlling the polarization states of incident and transmitted light, the metasurface creates a three-step displacement of structured light, eliminating the need to move samples or illumination sources. As a proof of concept, we experimentally demonstrate microscopic imaging using structured light illumination generated by metasurfaces, extracting high-frequency information from objects, and surpassing the diffraction limit. The proposed metasurface platform offers a promising approach for developing compact and robust phase-shifting imaging systems, with broad prospects in quantitative detection, machine vision, and beyond.
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
3.  Wang, J. et al. Quantitative phase imaging with a compact metamicroscope. *npj Nanophotonics* **1**, 4 (2024). [*(paper)*](https://doi.org/10.1038/s44310-024-00007-8)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Quantitative phase imaging with a compact metamicroscope.webp" 
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
       Quantitative phase imaging (QPI) based on the transport-of-intensity equation (TIE) is a powerful technique in label-free microscopy. The image stack required for a successful TIE-QPI is traditionally obtained by translating the object or image plane, and the optical elements used in the conventional TIE-QPI systems are usually bulky and cumbersome. Stable and compact TIE-QPI methods capable of non-motion optical zooming can significantly facilitate applications that demand portability. Here, we propose a non-motion TIE-QPI method based on a dispersive metalens. The dispersive nature of the metalens is utilized to provide a spectral focal tuning. With fixed object and image planes, seven through-focus intensity images are captured by changing the illumination wavelength. The QPI performance is validated by retrieving the surface phase profiles of a microlens array and a phase resolution target, showing a high phase detection accuracy (deviation less than 0.03 wavelength). Subsequently, we established a compact meta-microscope by integrating the metalens with a commercially available CMOS image sensor, which shows good performance in microscopic imaging of unstained bio-samples. Our approach, based on the large-dispersive metalens, facilitates a compact and robust QPI system for optical metrology and label-free microscopy.
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
4.  Li, W., Qi, J. & Mu, A. Single-pixel super-resolution with a space-time modulated computational metasurface imager. *Photonics Res.* **12**, 2311–2322 (2024). [*(paper)*](https://doi.org/10.1364/PRJ.532222)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Single-pixel super-resolution with a space-time modulated computational metasurface imager.jpg" 
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
       Single-pixel imaging is a burgeoning computational imaging technique that utilizes a single detector devoid of spatial resolution to capture an image, offering great potential for creating cost-effective and simplified imaging systems. Nevertheless, achieving super-resolution with a single pixel remains a formidable challenge. Here, we introduce a single-pixel super-resolution imaging technique based on space–time modulation. The modulation parametrically mixes the incoming signals, enabling the space–time scattered signals of the object carrying finer details to be captured by the single-pixel imaging system. To validate our proposed technique, we designed and fabricated a computational metasurface imager that needs only a single transmitting port and a single receiving port. The achieved resolution surpasses the Abbe resolution limit. The principle of our proposed technique is well-suited for low-cost and compact imaging systems.
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
5.  Akbari-Chelaresi, H., Salami, P. & Yousefi, L. Far-field sub-wavelength imaging using high-order dielectric continuous metasurfaces. *Opt. Express* **30**, 39025–39039 (2022). [*(paper)*](https://doi.org/10.1364/OE.470221)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Far-field sub-wavelength imaging using high-order dielectric continuous metasurfaces.jpg" 
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
       Due to the wave nature of light, the resolution achieved in conventional imaging systems is limited to around half of the wavelength. The reason behind this limitation, called diffraction limit, is that part of the information of the object carried by the evanescent waves scattered from an abject. Although retrieving information from propagating waves is not difficult in the far-field region, it is very challenging in the case of evanescent waves, which decay exponentially as travel and lose their power in the far-field region. In this paper, we design a high-order continuous dielectric metasurface to convert evanescent waves into propagating modes and subsequently to reconstruct super-resolution images in the far field. The designed metasurface is characterized and its performance for sub-wavelength imaging is verified using full wave numerical simulations. Simulation results show that the designed continuous high-order metasurface can convert a large group of evanescent waves into propagating ones. The designed metasurface is then used to reconstruct the image of objects with sub-wavelength features, and an image with the resolution of λ/5.5 is achieved.
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
6.  Ye, X. et al. Chip-scale metalens microscope for wide-field and depth-of-field imaging. *Adv. Photonics* **4**, 046006 (2022). [*(paper)*](https://doi.org/10.1117/1.AP.4.4.046006)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Chip-scale metalens microscope for wide-field and depth-of-field imaging.png" 
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
        Microscopy is very important in research and industry, yet traditional optical microscopy suffers from the limited field-of-view (FOV) and depth-of-field (DOF) in high-resolution imaging. We demonstrate a simultaneous large FOV and DOF microscope imaging technology based on a chip-scale metalens device that is implemented by a SiNx metalens array with a co- and cross-polarization multiplexed dual-phase design and dispersive spectrum zoom effect. A 4-mm × 4-mm FOV is obtained with a resolution of 1.74 μm and DOF of 200 μm within a wavelength range of 450 to 510 nm, which definitely exceeds the performance of traditional microscopes with the same resolution. Moreover, it is realized in a miniaturized compact prototype, showing an overall advantage for portable and convenient microscope technology.
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
7.  Sawant, R. et al. Aberration-corrected large-scale hybrid metalenses. *Optica* **8**, 1405–1411 (2021). [*(paper)*](https://doi.org/10.1364/OPTICA.434040)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Aberration-corrected large-scale hybrid metalenses.jpg" 
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
       Hybrid components combining the optical power of a refractive and a diffractive optical system can form compact doublet lenses that correct various aberrations. Unfortunately, the diffraction efficiency of these devices decreases as a function of the deflection angle over the element aperture. Here, we address this issue, compensating for chromatic dispersion and correcting for monochromatic aberrations with centimeter-scale hybrid-metalenses. We demonstrate a correction of at least 80% for chromatic aberration and 70% for spherical aberration. We finally present monochromatic and achromatic images that clearly show how these hybrid systems outperform standard refractive lenses. The possibilities to adjust arbitrary spatial amplitude, phase, polarization, and dispersion profiles with hybrid metasurfaces offer unprecedented optical design opportunities for compact and broadband imaging, augmented reality/virtual reality, and holographic projection.


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
8.  Hampson, K. M. et al. Adaptive optics for high-resolution imaging. *Nat. Rev. Methods Prim.* **1**, 68 (2021). [*(paper)*](https://doi.org/10.1038/s43586-021-00066-7)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Adaptive optics for high-resolution imaging.webp" 
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
       Adaptive optics (AO) is a technique that corrects for optical aberrations. It was originally proposed to correct for the blurring effect of atmospheric turbulence on images in ground-based telescopes and was instrumental in the work that resulted in the Nobel prize-winning discovery of a supermassive compact object at the centre of our galaxy. When AO is used to correct for the eye’s imperfect optics, retinal changes at the cellular level can be detected, allowing us to study the operation of the visual system and to assess ocular health in the microscopic domain. By correcting for sample-induced blur in microscopy, AO has pushed the boundaries of imaging in thick tissue specimens, such as when observing neuronal processes in the brain. In this primer, we focus on the application of AO for high-resolution imaging in astronomy, vision science and microscopy. We begin with an overview of the general principles of AO and its main components, which include methods to measure the aberrations, devices for aberration correction, and how these components are linked in operation. We present results and applications from each field along with reproducibility considerations and limitations. Finally, we discuss future directions.
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
9.  Hajahmadi, M. J., Faraji-Dana, R. & Skrivenvik, A. K. Far field superlensing inside biological media through a nanorod lens using spatiotemporal information. *Sci. Rep.* **11**, 1953 (2021). [*(paper)*](https://doi.org/10.1038/s41598-021-81091-0)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Far field superlensing inside biological media through a nanorod lens using spatiotemporal information.webp" 
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
       Far field superlensing of light has generated great attention in optical focusing and imaging applications. The capability of metamaterials to convert evanescent waves to propagative waves has led to numerous proposals in this regard. The common drawback of these approaches is their poor performance inside strongly scattering media like biological samples. Here, we use a metamaterial structure made out of aluminum nanorods in conjunction with time-reversal technique to exploit all temporal and spatial degrees of freedom for superlensing. Using broadband optics, we numerically show that this structure can perform focusing inside biological tissues with a resolution of λ/10. Moreover, for the imaging scheme we propose the entropy criterion for the image reconstruction step to reduce the number of required optical transducers. We propose an imaging scenario to reconstruct the spreading pattern of a diffusive material inside a tissue. In this way super-resolution images are obtained.
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
10.  Chen, M.-H., Chou, W.-N., Su, V.-C., Kuan, C.-H. & Lin, H. Y. High-performance gallium nitride dielectric metalenses for imaging in the visible. *Sci. Rep.* **11**, 6500 (2021). [*(paper)*](https://doi.org/10.1038/s41598-021-86057-w)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/High-performance gallium nitride dielectric metalenses for imaging in the visible.webp" 
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
       Metalens is one of the most promising applications for the development of metasurfaces. A wide variety of materials have been applied to metalenses working at certain spectral bands in order to meet the requirements of high efficiency and low-cost fabrication. Among these materials, wide-bandgap gallium nitride (GaN) is one of the most promising materials considering its advantages especially in semiconductor manufacturing. In this work, GaN has been utilized to fabricate the high-performance metalenses operating at visible wavelengths of 405, 532, and 633 nm with efficiencies up to 79%, 84%, and 89%, respectively. The homemade 1951 United State Air Force (UASF) resolution test chart has also been fabricated in order to provide resolvable lines with widths as small as 870 nm. As shown in the experimental results for imaging, the metalens designed at 405 nm can provide extremely high resolution to clearly resolve the smallest lines with the nano-sized widths in the homemade resolution test chart. These extraordinary experimental results come from our successful development in design and fabrication for the metalenses composed of high-aspect-ratio GaN nanoposts with nearly vertical sidewalls.
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
11.  Conteduca, D. et al. Dielectric nanohole array metasurface for high-resolution near-field sensing and imaging. *Nat. Commun.* **12**, 3293 (2021). [*(paper)*](https://doi.org/10.1038/s41467-021-23357-9)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Dielectric nanohole array metasurface for high-resolution near-field sensing and imaging.webp" 
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
       Dielectric metasurfaces support resonances that are widely explored both for far-field wavefront shaping and for near-field sensing and imaging. Their design explores the interplay between localised and extended resonances, with a typical trade-off between Q-factor and light localisation; high Q-factors are desirable for refractive index sensing while localisation is desirable for imaging resolution. Here, we show that a dielectric metasurface consisting of a nanohole array in amorphous silicon provides a favourable trade-off between these requirements. We have designed and realised the metasurface to support two optical modes both with sharp Fano resonances that exhibit relatively high Q-factors and strong spatial confinement, thereby concurrently optimizing the device for both imaging and biochemical sensing. For the sensing application, we demonstrate a limit of detection (LOD) as low as 1 pg/ml for Immunoglobulin G (IgG); for resonant imaging, we demonstrate a spatial resolution below 1 µm and clearly resolve individual E. coli bacteria. The combined low LOD and high spatial resolution opens new opportunities for extending cellular studies into the realm of microbiology, e.g. for studying antimicrobial susceptibility.
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
12.  Zhu, A. Y. et al. Compact aberration-corrected spectrometers in the visible using dispersion-tailored metasurfaces. *Adv. Opt. Mater.* **7**, 1801144 (2019). [*(paper)*](https://doi.org/10.1002/adom.201801144)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Compact aberration-corrected spectrometers in the visible using dispersion-tailored metasurfaces.jpg" 
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
       The spectral resolution and range of conventional spectrometers are typically limited by optical aberrations of their focusing elements, mainly due to chromatically induced astigmatism and an intrinsically curved focal plane. Traditional approaches to overcome this challenge require additional optical components which introduce significant bulk and design complexity to the system and prevent easy integration with portable devices. Here a single planar off-axis focusing metalens consisting of subwavelength TiO2 nanofins whose focal spots lie along a plane and undergo minimal focal spot broadening for almost 200 nm across the visible spectrum is demonstrated. This allows us to achieve a miniature aberration-corrected spectrometer with nanometer spectral resolution, while having a beam propagation distance of only 4 cm to the camera plane. This is achieved by dispersion engineering: tailoring the phase, group delay (GD) and GD dispersion of the metalens. This approach is general and can also be used to introduce customized functionalities to the metalens such as a linear dispersion in the frequency domain with minimal additional overhead.
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
13.  Holsteen, A. L., Lin, D., Kauvar, I., Wetzstein, G. & Brongersma, M. L. A light-field metasurface for high-resolution single-particle tracking. *Nano Lett.* **19**, 2267–2271 (2019). [*(paper)*](https://doi.org/10.1021/acs.nanolett.8b04673)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A light-field metasurface for high-resolution single-particle tracking.gif" 
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
       Three-dimensional (3D) single-particle tracking (SPT) is a key tool for studying dynamic processes in the life sciences. However, conventional optical elements utilizing light fields impose an inherent trade-off between lateral and axial resolution, preventing SPT with high spatiotemporal resolution across an extended volume. We overcome the typical loss in spatial resolution that accompanies light-field-based approaches to obtain 3D information by placing a standard microscope coverslip patterned with a multifunctional, light-field metasurface on a specimen. This approach enables an otherwise unmodified microscope to gather 3D information at an enhanced spatial resolution. We demonstrate simultaneous tracking of multiple fluorescent particles within a large 0.5 × 0.5 × 0.3 mm3 volume using a standard epi-fluorescent microscope with submicron lateral and micron-level axial resolution.
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
14.  Hall, C. U., Poulikakos, D. & Eghlidi, H. High-efficiency, extreme-numerical-aperture metasurfaces based on partial control of the phase of light. *Adv. Opt. Mater.* **6**, 1800852 (2018). [*(paper)*](https://doi.org/10.1002/adom.201800852)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/High-efficiency, extreme-numerical-aperture metasurfaces based on partial control of the phase of light..jpg" 
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
       High-quality flat optical elements require efficient light deflection to large angles and over a wide wavelength spectrum. Although phase gradient metasurfaces achieve this by continuously adding phase shifts in the range of 0–2π to the electric field with subwavelength-sized scatterers, their performance is limited by the spatial resolution of phase modulation at the interface. Here, a new class of metasurfaces is introduced, where the phase shifts cover less than the full 0–2π range, offering significant advantages. This approach allows the realization of metasurfaces with more compact and less mutually-interacting scatterers, and thus more precise phase modulation, and advances the performance limits of metasurfaces to domains significantly beyond those of the full coverage phase gradient approach. Applying this concept to both plasmonic and dielectric surfaces, large phase gradients resulting in high-numerical-aperture immersion metalenses (NA = 1.4) with near diffraction-limited resolution (≈0.32λ) at visible wavelengths are demonstrated. This concept enables added functionalities such as broadband performance and wavelength de-multiplexing on a single layer, surpassing the theoretical cross-polarization transmission efficiency limit for single-layer plasmonic metasurfaces, and yields 67% efficiency for dielectric metasurfaces. This work paves the way toward realizing high-resolution flat optical elements and efficient plasmonic metadevices.
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
15.  Paniagua-Dominguez, R. et al. A metalens with a near-unity numerical aperture. *Nano Lett.* **18**, 2124–2132 (2018). [*(paper)*](https://doi.org/10.1021/acs.nanolett.8b00368)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A metalens with a near-unity numerical aperture.webp" 
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
       The numerical aperture (NA) of a lens determines its ability to focus light and its resolving capability. Having a large NA is a very desirable quality for applications requiring small light–matter interaction volumes or large angular collections. Traditionally, a large NA lens based on light refraction requires precision bulk optics that ends up being expensive and is thus also a specialty item. In contrast, metasurfaces allow the lens designer to circumvent those issues producing high-NA lenses in an ultraflat fashion. However, so far, these have been limited to numerical apertures on the same order of magnitude as traditional optical components, with experimentally reported NA values of <0.9. Here we demonstrate, both numerically and experimentally, a new approach that results in a diffraction-limited flat lens with a near-unity numerical aperture (NA > 0.99) and subwavelength thickness (∼λ/3), operating with unpolarized light at 715 nm. To demonstrate its imaging capability, the designed lens is applied in a confocal configuration to map color centers in subdiffractive diamond nanocrystals. This work, based on diffractive elements that can efficiently bend light at angles as large as 82°, represents a step beyond traditional optical elements and existing flat optics, circumventing the efficiency drop associated with the standard, phase mapping approach.
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
16.  Zuo, R., Liu, W., Cheng, H., Chen, S. & Tian, J. Breaking the diffraction limit with radially polarized light based on dielectric metalenses. *Adv. Opt. Mater.* **6**, 1800795 (2018). [*(paper)*](https://doi.org/10.1002/adom.201800795)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Breaking the diffraction limit with radially polarized light based on dielectric metalenses.jpg" 
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
       Dielectric metalenses with high efficiency and compact size have been widely investigated recently, but still suffer from Abbe diffraction limit. Herein, with linear polarization incidence, a dielectric metalens is demonstrated to efficiently generate and focus radially polarized light simultaneously. Two novel methods are proposed to achieve super-resolution. First, a circular high-pass aperture is utilized to enhance the longitudinal field component in the vicinity of focus with the focal spot size of 0.138λ2, much smaller than the theoretical limit of 0.212λ2. The key parameters that impact the focusing size are explored in detail, such as radius of the circular aperture and numerical aperture of the metalens. Second, an extra phase distribution is added on the metalens to filter the transversely polarized component, which leads to a focal spot size of 0.144λ2. The approach provides a wide platform for sub-resolution focusing and imaging, which offers the capability of subdiffraction techniques for microscopy systems and information processing with extensive channels.
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
17.  Chen, W. T. et al. Immersion meta-lenses at visible wavelengths for nanoscale imaging. *Nano Lett.* **17**, 3188–3194 (2017). [*(paper)*](https://doi.org/10.1021/acs.nanolett.7b00717)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Immersion meta-lenses at visible wavelengths for nanoscale imaging.webp" 
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
       Immersion objectives can focus light into a spot smaller than what is achievable in free space, thereby enhancing the spatial resolution for various applications such as microscopy, spectroscopy, and lithography. Despite the availability of advanced lens polishing techniques, hand-polishing is still required to manufacture the front lens of a high-end immersion objective, which poses major constraints for lens design. This limits the shape of the front lens to spherical. Therefore, several other lenses need to be cascaded to correct for spherical aberration, resulting in significant challenges for miniaturization and adding design complexity for different immersion liquids. Here, by using metasurfaces, we demonstrate liquid immersion meta-lenses free of spherical aberration at various design wavelengths in the visible spectrum. We report water and oil immersion meta-lenses of various numerical apertures (NA) up to 1.1 and show that their measured focal spot sizes are diffraction-limited with Strehl ratios of approximately 0.9 at 532 nm. By integrating the oil immersion meta-lens (NA = 1.1) into a commercial scanning confocal microscope, we achieve an imaging spatial resolution of approximately 200 nm. These meta-lenses can be easily adapted to focus light through multilayers of different refractive indices and mass-produced using modern industrial manufacturing or nanoimprint techniques, leading to cost-effective high-end optics.
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
18.  Gao, H. et al. Super-resolution imaging with a beesel lens realized by a geometric metasurface. *Opt. Express* **25**, 13933–13943 (2017). [*(paper)*](https://doi.org/10.1364/OE.25.013933)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Super-resolution imaging with a beesel lens realized by a geometric metasurface.jpg" 
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
       In the super resolution imaging system, a lens and an axicon that can generate spherical wavefronts and non-diffracting Bessel beams respectively are both essential yet difficult to integrate using the traditional approach. We propose a new concept of a “Bessel-lens” to indicate unique optical elements that merge the functionalities of lenses and axicons simultaneously. The Bessel-lens is a mission that is extremely difficult if not impossible for state-of-the-art technology because of the exotic phase profile. Via the geometric phases in space-variant nanoslits, planar Bessel-lenses are designed and experimentally characterized for the first time to generate subdiffraction beams. Compared with a planar lens and axicon with the same dimensions and numerical aperture, the proposed Bessel-lens possesses a higher imaging resolution, which may find applications in microscopy, nanofabrication and dense data storage.
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
19.  Yang, H. et al. Reflective metalens with sub-diffraction-limited and multifunctional focusing. *Sci. Rep.* **7**, 12632 (2017). [*(paper)*](https://doi.org/10.1038/s41598-017-13004-z)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Reflective metalens with sub-diffraction-limited and multifunctional focusing.webp" 
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
       We propose an ultra-thin planar reflective metalens with sub-diffraction-limited and multifunctional focusing. Based on the equal optical path principle, the specific phase distributions for multifunction focusing are derived. Following the formulas, on-center focusing with the characteristics of sub-diffraction-limited, high focusing efficiency (85%) and broadband focusing is investigated in detail. To demonstrate the flexibility of the reflective metalens, off-center and dual spots focusing (at the horizontal and longitudinal directions) are demonstrated. Note that all these focusings are sub-diffraction-limited due to the evanescent-filed enhancement mechanism in our elaborately designed structure. The designed reflective metalens will find important applications in super-resolution imaging, microscopes, and spectroscopic designs.
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
20.  Khorasaninejad, M. et al. Metalenses at visible wavelengths: diffraction-limited focusing and subwavelength resolution imaging. *Science* **352**, 1190–1194 (2016). [*(paper)*](https://doi.org/10.1126/science.aaf6644)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metalenses at visible wavelengths diffraction-limited focusing and subwavelength resolution imaging.jpeg" 
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
       Specially designed two-dimensional (2D) arrays of nanometer-scale metallic antennas, or metasurfaces, may allow bulky optical components to be shrunk down to a planar device structure. Khorasaninejad et al. show that arrays of nanoscale fins of TiO can function as high-end optical lenses. At just a fraction of the size of optical objectives, such planar devices could turn your phone camera or your contact lens into a compound microscope. Maguid et al. interleaved sparse 2D arrays of metal antennas to get multifunctional behavior from the one planar device structure (see the Perspective by Litchinitser). The enhanced functionality of such designed metasurfaces could be used in sensing applications or to increase the communication capacity of nanophotonic networks.
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
21.  Lu, D. & Liu, Z. Hyperlenses and metalenses for far-field super-resolution imaging. *Nat. Commun.* **3**, 1205 (2012). [*(paper)*](https://doi.org/10.1038/ncomms2176)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Hyperlenses and metalenses for far-field super-resolution imaging.webp" 
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
       The resolution of conventional optical lens systems is always hampered by the diffraction limit. Recent developments in artificial metamaterials provide new avenues to build hyperlenses and metalenses that are able to image beyond the diffraction limit. Hyperlenses project super-resolution information to the far field through a magnification mechanism, whereas metalenses not only super-resolve subwavelength details but also enable optical Fourier transforms. Recently, there have been numerous designs for hyperlenses and metalenses, bringing fresh theoretical and experimental advances, though future directions and challenges remain to be overcome.
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
22.  Fang, N., Lee, H., Sun, C. & Zhang, X. Sub-diffraction-limited optical imaging with a silver superlens. *Science* **308**, 534–537 (2005). [*(paper)*](https://doi.org/10.1126/science.1108759)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Sub-diffraction-limited optical imaging with a silver superlens.jpeg" 
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
       Recent theory has predicted a superlens that is capable of producing sub–diffraction-limited images. This superlens would allow the recovery of evanescent waves in an image via the excitation of surface plasmons. Using silver as a natural optical superlens, we demonstrated sub–diffraction-limited imaging with 60-nanometer half-pitch resolution, or one-sixth of the illumination wavelength. By proper design of the working wavelength and the thickness of silver that allows access to a broad spectrum of subwavelength features, we also showed that arbitrary nanostructures can be imaged with good fidelity. The optical superlens promises exciting avenues to nanoscale optical imaging and ultrasmall optoelectronic devices.
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

### 5. Multidimensional Data Capture

![](assets/multidimensional_data_capture.png)  

1. Fu, B. et al. Miniaturized high-efficiency snapshot polarimetric stereoscopic imaging. *Optica* **12**, 391–398 (2025). [*(paper)*](https://doi.org/10.1364/OPTICA.549864)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Miniaturized high-efficiency snapshot polarimetric stereoscopic imaging.jpg" 
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
       Stereoscopic imaging reveals the 3D morphology of objects by collecting dense optical data from multiple views. However, traditional active methods rely on structured light illumination, while passive methods require substantial bulky optical components, hindering the development of portable, real-time stereoimaging systems. Here, we demonstrate miniaturized passive snapshot polarimetric stereoscopic imaging (SPSIM) using a polarimetric metalens. This protocol outperforms commercial polarimetric cameras in efficiency and enables the separation of circular polarization (CP) components for full Stokes parameter acquisition. By incorporating polarimetric physical priors into the neural network, we significantly enhance the accuracy of the 3D reconstruction process, enabling instant stereoimaging from a single shot with low mean absolute error. The inclusion of CP information improves 3D surface detail reconstruction, achieving depth precision within 0.15 mm. Our SPSIM system is well suited for integration into miniaturized devices for use in extreme environments, while advancing next-generation high-resolution 3D imaging systems.
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
2. Zhao, Z. et al. Hyperspectral metachip-based 3d spatial map for cancer cell screening and quantification. *Adv. Mater.* **37**, 2412738 (2025). [*(paper)*](https://doi.org/10.1002/adma.202412738)
    
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Hyperspectral metachip-based 3d spatial map for cancer cell screening and quantification.jpg" 
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
       In this paper, compact terahertz (THz) metachips for hyperspectral screening and quantitative evaluation of human cancer cells is reported. This pixelated resonant metachips feature the resonance channel from 1 and 3 THz frequency with a record-high quality factor (up to 230). Through the interactions of various cancer cells of different concentrations, high-dimensional spectral signatures are obtained, which are further transformed into a spatial map for labelling and quantification purposes. The screening of up to 15 cancer cells is experimentally reported, with very high detecting accuracy of 93.33% and with attractive quantitative concentration sensitivity up to 1320 kHz cell mL−1. This hyperspectral metachips are low-cost, highly compact, and label-free for fast, high-throughput and high-sensitivity detections and evaluation of human cancer cells. This technology does not require clinical experience, representing an accessible technology for early diagnosis of cancer.
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
3. Zhang, Z. et al. Single-shot on-chip diffractive speckle spectrometer with high spectral channel density. *Laser Photonics Rev.* **19**, 2401987 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202401987)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Single-shot on-chip diffractive speckle spectrometer with high spectral channel density.jpg" 
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
       The research on chip-scale spectrometers is driven by the growing demand for miniaturized and integrated spectral sensors. The performance trade-off between spectral resolution and bandwidth is one of the primary challenges for the community. While substantial progress has been made toward a vast number of spectral channels to overcome this issue, they either relied on sophisticated tuning mechanisms or required huge chip areas. In this work, a single-shot spectrometer is demonstrated based on all passive on-chip diffractive metasurfaces which is able to create the speckle pattern with richness of spectral information. By scaling the diffractive structure to three layers of metasurfaces, the number of spectral channels resolved from the speckle can be significantly increased due to the cascaded diffraction behaviors. The device is fabricated via a standard silicon photonic foundry with CMOS compatible process. A measured resolution of 47 pm is achieved across the bandwidth of 40 nm, yielding up to 851 spectral channels within a compact footprint of 150 µm × 300 µm. The corresponding spectral channel density reaches 18911 ch mm−2. It provides a possible means to develop single-shot and compact on-chip spectrometers beyond the resolution-bandwidth limit.
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
4. Liu, Z. et al. Dual jones matrices empowered six phase channels modulation with single-layer monoatomic metasurfaces. *Laser Photonics Rev.* **19**, 2401526 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202401526)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Dual jones matrices empowered six phase channels modulation with single-layer monoatomic metasurfaces.jpg" 
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
       A comprehensive manipulation of the Jones matrix phase channels is crucial for enhancing the information capacity and security of the metasurface. However, a single-layer planar metasurface, without the incorporation of chirality, can only achieve a maximum of three independent phase channels for single Jones matrix under either linear or circular polarization bases. Here, an effective strategy is proposed that utilizes dual Jones matrices in different polarization bases with a single-layer monoatomic metasurface, thus extending the number of independent phase channels to six. To encode six holographic images into these six phase channels, a three-step gradient descent algorithm is introduced. As a proof of principle, a metasurface consisting of arrays of monoatomic dielectric structure is designed and fabricated in each unit cell, which exhibits six independent holographic images in the far field. The demonstrated metasurface platform is expected to open up new possibilities for the development of optical devices for applications in high-capacity information storage, high-security encrypted communication, and high-solution optical displays.
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
5. Tang, F. et al. Metasurface spectrometers beyond resolution-sensitivity constraints. *Sci. Adv.* **10**, eadr7155 (2024). [*(paper)*](https://doi.org/10.1126/sciadv.adr7155)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface spectrometers beyond resolution-sensitivity constraints.jpg" 
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
       Conventional spectrometer designs necessitate a compromise between their resolution and sensitivity, especially as device and detector dimensions are scaled down. Here, we report on a miniaturizable spectrometer platform where light throughput onto the detector is instead enhanced as the resolution is increased. This planar, CMOS-compatible platform is based around metasurface encoders designed to exhibit photonic bound states in the continuum, where operational range can be altered or extended simply through adjusting geometric parameters. This system can enhance photon collection efficiency by up to two orders of magnitude versus conventional designs; we demonstrate this sensitivity advantage through ultralow-intensity fluorescent and astrophotonic spectroscopy. This work represents a step forward for the practical utility of spectrometers, affording a route to integrated, chip-based devices that maintain high resolution and SNR without requiring prohibitively long integration times.
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
6. Hao, H. et al. Single-shot 3d imaging meta-microscope. *Nano Lett.* **24**, 13364–13373 (2024). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c03952)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Single-shot 3d imaging meta-microscope.webp" 
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
       Three-dimensional (3D) imaging enables high-precision and high-resolution axial positioning, which is crucial for biological imaging, semiconductor defect monitoring, and other applications. Conventional implementations rely on bulky optical elements or scanning mechanisms, resulting in low speed and complicated setups. Here, we generate the double-helix (DH) point spread function with an all-dielectric metasurface and thus innovate the 3D imaging microscope (hence dubbed meta-microscope), both in 4f and 2f imaging systems. The 4f-meta-microscope with a numerical aperture of 0.7 achieves an axial localization accuracy below 0.12 μm within a 15.47 μm detection range, while the 2f-DH meta-microscope with a numerical aperture of 0.3 shows a 1.12 μm accuracy within a 227.33 μm range. We also demonstrate single-shot and accurate 3D biological imaging of the mouse kidney tissue and peach anther, providing a comprehensive and efficient approach for 3D bioimaging and other applications through a single-shot 3D meta-microscope.
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
7. Yang, J. et al. Reconfigurable snapshot hyperspectral imaging sensor based on monochromatic pattern match of gradient geometry metasurface. *ACS Photonics* **11**, 3841–3851 (2024). [*(paper)*](https://doi.org/10.1021/acsphotonics.4c01136)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Reconfigurable snapshot hyperspectral imaging sensor based on monochromatic pattern match of gradient geometry metasurface.webp" 
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
       Metasurface-based hyperspectral imaging has profoundly impacted the field, with its easy integration and miniaturization advantages. Notably, metallic metasurfaces have been a research subject in sensing and imaging due to their strong capability of restraining light and supporting high-fidelity and cost-effective manufacturing processes. In this work, a novel metallic metasurface with gradient geometry was proposed for hyperspectral imaging, which highlights the advantages of defect tolerance and reconfigurability of imaging units with a spectral image resolution of 135 × 75 superpixels. An orthogonal matching algorithm with postcalibration based on monochromatic transmittance images of the metasurface was designed for spectral reconstruction. The proposed reconstruction algorithm simplifies calibration and can compensate for systematic losses. The operating bandwidth of the hyperspectral imaging sensor can be reconfigured, and the miniaturized nature makes it potentially integrated into smartphones and other instruments with lightweight computing and fast reconstruction. Moreover, the strategy has been validated in sensing and real-object surface imaging with a spectral resolution of approximately 1.99 nm under a 2 nm line width. Its efficacy is verified in the 400–800 nm band with a high fidelity of up to 86.7%.
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
8. Cai, G. et al. Compact angle-resolved metasurface spectrometer. *Nat. Mater.* **23**, 71–78 (2024). [*(paper)*](https://doi.org/10.1038/s41563-023-01710-1)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Compact angle-resolved metasurface spectrometer.webp" 
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
       Light scattered or radiated from a material carries valuable information on the said material. Such information can be uncovered by measuring the light field at different angles and frequencies. However, this technique typically requires a large optical apparatus, hampering the widespread use of angle-resolved spectroscopy beyond the lab. Here we demonstrate compact angle-resolved spectral imaging by combining a tunable metasurface-based spectrometer array and a metalens. With this approach, even with a miniaturized spectrometer footprint of only 4 × 4 μm2, we demonstrate a wavelength accuracy of 0.17 nm, spectral resolution of 0.4 nm and a linear dynamic range of 149 dB. Moreover, our spectrometer has a detection limit of 1.2 fJ, and can be patterned to an array for spectral imaging. Placing such a spectrometer array directly at the back focal plane of a metalens, we achieve an angular resolution of 4.88 × 10−3 rad. Our angle-resolved spectrometers empowered by metalenses can be employed towards enhancing advanced optical imaging and spectral analysis applications.
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
9.  Zuo, J. et al. Metasurface-based mueller matrix microscope. *Adv. Funct. Mater.* **34**, 2405412 (2024). [*(paper)*](https://doi.org/10.1002/adfm.202405412)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-based mueller matrix microscope.jpg" 
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
       In conventional optical microscopes, image contrast of objects mainly results from the differences in light intensity and/or color. Muller matrix optical microscopes (MMMs), on the other hand, can provide significantly enhanced image contrast and rich information about objects by analyzing their interactions with polarized light. However, state-of-the-art MMMs are fundamentally limited by bulky and slow polarization state generators and analyzers. Here, the study demonstrates a metasurface-based MMM, i.e., Meta-MMM, which is equipped with a chip-integrated, single-shot metasurface polarization state analyzer (Meta-PSA). The Meta-MMM is featured with high-speed measurement (≈2s per Muller matrix (MM) image), superior operation stability, dual-color operation, and high measurement accuracy (measurement error 1–2%) for MM imaging. The Meta-MMM is applied to nanostructure characterization, surface morphology analysis, and discovering birefringent structures in honeybee wings. The Meta-MMMs hold the promise to revolutionize various applications from biological imaging, medical diagnosis, and material characterization to industry inspection and space exploration.
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
10. Hu, Y. et al. Achromatic full stokes polarimetry metasurface for full-color polarization imaging in the visible range. *Nano Lett.* **24**, 13018–13026 (2024). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c03785)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Achromatic full stokes polarimetry metasurface for full-color polarization imaging in the visible range.webp" 
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
       Metasurfaces provide an ultrathin platform for compact, real-time polarimetry. However, their applications in polychromatic scenes are restricted by narrow operating bandwidths that causes spectral information loss. Here, we demonstrate full-color polarization imaging using an achromatic polarimeter consisting of four polarization-dependent metalenses. Leveraging an intelligent design scheme, we achieve effective arbitrary phase compensation and multiobjective matching with a limited database. This system provides broadband achromaticity across wavelengths from 450 to 650 nm, resulting in a relative bandwidth of approximately 0.364 for full Stokes imaging. Experimental reconstruction errors for wavelengths of 450, 550, and 650 nm are 7.5%, 5.9%, and 3.8%, respectively. Performance is evaluated based on both achromatic bandwidth and crosstalk, with our design achieving three times the performance of the current state-of-the-art. The full-color, full-polarization imaging capability of the device is further validated with a customized object. The proposed scheme advances polarization imaging for practical applications.
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
11. Zaidi, A. et al. Metasurface-enabled single-shot and complete mueller matrix imaging. *Nat. Photonics* **18**, 704–712 (2024). [*(paper)*](https://doi.org/10.1038/s41566-024-01426-x)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-enabled single-shot and complete mueller matrix imaging.webp" 
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
       When light scatters off an object, its polarization, in general, changes—a transformation described by the object’s Mueller matrix. Mueller matrix imaging is an important technique in science and technology to image the spatially varying polarization response of an object of interest, to reveal rich information otherwise invisible to traditional imaging. Here we conceptualize, implement and demonstrate a compact Mueller matrix imaging system—composed of a metasurface to produce structured polarization illumination and a metasurface for polarization analysis—that can, in a single shot, acquire all 16 components of an object’s spatially varying Mueller matrix over an image. Our implementation, which is free of any moving parts or bulk polarization optics, should enable and empower applications in real-time medical imaging, material characterization, machine vision, target detection and other important areas.
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
12. Fan, Y. et al. Dispersion-assisted high-dimensional photodetector. *Nature* **630**, 70–83 (2024). [*(paper)*](https://doi.org/10.1038/s41586-024-07398-w)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Dispersion-assisted high-dimensional photodetector.webp" 
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
       Intensity, polarization and wavelength are intrinsic characteristics of light. Characterizing light with arbitrarily mixed information on polarization and spectrum is in high demand1,2,3,4. Despite the extensive efforts in the design of polarimeters5,6,7,8,9,10,11,12,13,14,15,16,17,18 and spectrometers19,20,21,22,23,24,25,26,27, concurrently yielding high-dimensional signatures of intensity, polarization and spectrum of the light fields is challenging and typically requires complicated integration of polarization- and/or wavelength-sensitive elements in the space or time domains. Here we demonstrate that simple thin-film interfaces with spatial and frequency dispersion can project and tailor polarization and spectrum responses in the wavevector domain. By this means, high-dimensional light information can be encoded into single-shot imaging and deciphered with the assistance of a deep residual network. To the best of our knowledge, our work not only enables full characterization of light with arbitrarily mixed full-Stokes polarization states across a broadband spectrum with a single device and a single measurement but also presents comparable, if not better, performance than state-of-the-art single-purpose miniaturized polarimeters or spectrometers. Our approach can be readily used as an alignment-free retrofit for the existing imaging platforms, opening up new paths to ultra-compact and high-dimensional photodetection and imaging.
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
13. Chakravarthula, P. et al. Thin on-sensor nanophotonic array cameras. *ACM Trans. Graph.* **42**, 1–18 (2023). [*(paper)*](https://doi.org/10.1145/3618398)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Thin on-sensor nanophotonic array cameras.png" 
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
       Today's commodity camera systems rely on compound optics to map light originating from the scene to positions on the sensor where it gets recorded as an image. To record images without optical aberrations, i.e., deviations from Gauss' linear model of optics, typical lens systems introduce increasingly complex stacks of optical elements which are responsible for the height of existing commodity cameras. In this work, we investigate flat nanophotonic computational cameras as an alternative that employs an array of skewed lenslets and a learned reconstruction approach. The optical array is embedded on a metasurface that, at 700 nm height, is flat and sits on the sensor cover glass at 2.5 mm focal distance from the sensor. To tackle the highly chromatic response of a metasurface and design the array over the entire sensor, we propose a differentiable optimization method that continuously samples over the visible spectrum and factorizes the optical modulation for different incident fields into individual lenses. We reconstruct a megapixel image from our flat imager with a learned probabilistic reconstruction method that employs a generative diffusion model to sample an implicit prior. To tackle scene-dependent aberrations in broadband, we propose a method for acquiring paired captured training data in varying illumination conditions. We assess the proposed flat camera design in simulation and with an experimental prototype, validating that the method is capable of recovering images from diverse scenes in broadband with a single nanophotonic layer.
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
14. Fan, Q. et al. Disordered metasurface enabled single-shot full-Stokes polarization imaging leveraging weak dichroism. *Nat. Commun.* **14**, 7180 (2023). [*(paper)*](https://doi.org/10.1038/s41467-023-42944-6)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Disordered metasurface enabled single-shot full-Stokes polarization imaging leveraging weak dichroism.webp" 
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
       Polarization, one of the fundamental properties of light, is critical for certain imaging applications because it captures information from the scene that cannot directly be recorded by traditional intensity cameras. Currently, mainstream approaches for polarization imaging rely on strong dichroism of birefringent crystals or artificially fabricated structures that exhibit a high diattenuation typically exceeding 99%, which corresponds to a polarization extinction ratio (PER) >~100. This not only limits the transmission efficiency of light, but also makes them either offer narrow operational bandwidth or be non-responsive to the circular polarization. Here, we demonstrate a single-shot full-Stokes polarization camera incorporating a disordered metasurface array with weak dichroism. The diattenuation of the metasurface array is ~65%, which corresponds to a PER of ~2. Within the framework of compressed sensing, the proposed disordered metasurface array serves as an efficient sensing matrix. By incorporating a mask-aware reconstruction algorithm, the signal can be accurately recovered with a high probability. In our experiments, the proposed approach exhibits high-accuracy full-Stokes polarimetry and high-resolution real-time polarization imaging. Our demonstration highlights the potential of combining meta-optics with reconstruction algorithms as a promising approach for advanced imaging applications.
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
15. Zuo, J. et al. Chip-integrated metasurface full-Stokes polarimetric imaging sensor. *Light Sci. Appl.* **12**, 218 (2023). [*(paper)*](https://doi.org/10.1038/s41377-023-01260-w)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Chip-integrated metasurface full-Stokes polarimetric imaging sensor.webp" 
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
       Polarimetric imaging has a wide range of applications for uncovering features invisible to human eyes and conventional imaging sensors. Chip-integrated, fast, cost-effective, and accurate full-Stokes polarimetric imaging sensors are highly desirable in many applications, which, however, remain elusive due to fundamental material limitations. Here we present a chip-integrated Metasurface-based Full-Stokes Polarimetric Imaging sensor (MetaPolarIm) realized by integrating an ultrathin (~600 nm) metasurface polarization filter array (MPFA) onto a visible imaging sensor with CMOS compatible fabrication processes. The MPFA is featured with broadband dielectric-metal hybrid chiral metasurfaces and double-layer nanograting polarizers. This chip-integrated polarimetric imaging sensor enables single-shot full-Stokes imaging (speed limited by the CMOS imager) with the most compact form factor, records high measurement accuracy, dual-color operation (green and red) and a field of view up to 40 degrees. MetaPolarIm holds great promise to enable transformative applications in autonomous vision, industry inspection, space exploration, medical imaging and diagnosis.
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
16. Kim, G. et al. Metasurface-driven full-space structured light for three-dimensional imaging. *Nat. Commun.* **13**, 5920 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-32117-2)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-driven full-space structured light for three-dimensional imaging.webp" 
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
       Structured light (SL)-based depth-sensing technology illuminates the objects with an array of dots, and backscattered light is monitored to extract three-dimensional information. Conventionally, diffractive optical elements have been used to form laser dot array, however, the field-of-view (FOV) and diffraction efficiency are limited due to their micron-scale pixel size. Here, we propose a metasurface-enhanced SL-based depth-sensing platform that scatters high-density ~10 K dot array over the 180° FOV by manipulating light at subwavelength-scale. As a proof-of-concept, we place face masks one on the beam axis and the other 50° apart from axis within distance of 1 m and estimate the depth information using a stereo matching algorithm. Furthermore, we demonstrate the replication of the metasurface using the nanoparticle-embedded-resin (nano-PER) imprinting method which enables high-throughput manufacturing of the metasurfaces on any arbitrary substrates. Such a full-space diffractive metasurface may afford ultra-compact depth perception platform for face recognition and automotive robot vision applications.
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
17. Jing, X. et al. Single-shot 3d imaging with point cloud projection based on metadevice. *Nat. Commun.* **13**, 7842 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-35483-z)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Single-shot 3d imaging with point cloud projection based on metadevice.webp" 
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
       Three-dimensional (3D) imaging is a crucial information acquisition technology for light detection, autonomous vehicles, gesture recognition, machine vision, and other applications. Metasurface, as a subwavelength scale two-dimensional array, offers flexible control of optical wavefront owing to abundant design freedom. Metasurfaces are promising for use as optical devices because they have large field of view and powerful functionality. In this study, we propose a flat optical device based on a single-layer metasurface to project a coded point cloud in the Fourier space and explore a sophisticated matching algorithm to achieve 3D reconstruction, offering a complete technical roadmap for single-shot detection. We experimentally demonstrate that the depth accuracy of our system is smaller than 0.24 mm at a measurement distance of 300 mm, indicating the feasibility of the submillimetre measurement platform. Our method can pave the way for practical applications such as surface shape detection, gesture recognition, and personal authentication.
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
18. Xiong, J. et al. Dynamic brain spectrum acquired by a real-time ultraspectral imaging chip with reconfigurable metasurfaces. *Optica* **9**, 461–468 (2022). [*(paper)*](https://doi.org/10.1364/OPTICA.440013)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Dynamic brain spectrum acquired by a real-time ultraspectral imaging chip with reconfigurable metasurfaces.jpg" 
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
       Spectral imaging paves the way for various fields, particularly in biomedical research. However, spectral imaging, mainly depending on spatial or temporal scanning, cannot achieve high temporal, spatial, and spectral resolution simultaneously. In this study, we demonstrated a silicon real-time ultraspectral imaging chip based on reconfigurable metasurfaces, comprising 155,216 (356*436) image-adaptive microspectrometers with ultra-high center-wavelength accuracy of 0.04 nm and spectral resolution of 0.8 nm. It is employed for imaging brain hemodynamics, and the dynamic spectral absorption properties of deoxyhemoglobin and oxyhemoglobin in a rat barrel cortex were obtained, which enlighten spectroscopy in vivo studies and other real-time applications.
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
19. Makarenko, M. et al. Real-time hyperspectral imaging in hardware via trained metasurface encoders. In *Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 12692–12702 (IEEE, 2022). [*(paper)*](https://doi.org/10.1109/CVPR52688.2022.01236)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Real-time hyperspectral imaging in hardware via trained metasurface encoders.gif" 
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
       Hyperspectral imaging has attracted significant attention to identify spectral signatures for image classification and automated pattern recognition in computer vision. State-of-the-art implementations of snapshot hyperspectral imaging rely on bulky, non-integrated, and expensive optical elements, including lenses, spectrometers, and filters. These macroscopic components do not allow fast data processing for, e.g. real-time and high-resolution videos. This work introduces Hyplex™, a new integrated architecture addressing the limitations discussed above. Hyplex™ is a CMOS-compatible, fast hyperspectral camera that replaces bulk optics with nanoscale metasurfaces inversely designed through artificial intelligence. Hyplex™ does not require spectrometers but makes use of conventional monochrome cameras, opening up the possibility for real-time and high-resolution hyperspectral imaging at inexpensive costs. Hyplex™ exploits a model-driven optimization, which connects the physical metasurfaces layer with modern visual computing approaches based on end-to-end training. We design and implement a prototype version of Hyplex™ and compare its performance against the state-of-the-art for typical imaging tasks such as spectral reconstruction and semantic segmentation. In all benchmarks, Hyplex™ reports the smallest reconstruction error. We additionally present what is, to the best of our knowledge, the largest publicly available labeled hyperspectral dataset for semantic segmentation.11Dataset available on https://github.com/makamoa/hyplex.
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
20. Bao, Y. et al. Observation of full-parameter jones matrix in bilayer metasurface. *Nat. Commun.* **13**, 7550 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-35313-2)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Observation of full-parameter jones matrix in bilayer metasurface.webp" 
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
       Metasurfaces, artificial 2D structures, have been widely used for the design of various functionalities in optics. Jones matrix, a 2×2 matrix with eight parameters, provides the most complete characterization of the metasurface structures in linear optics, and the number of free parameters (i.e., degrees of freedom, DOFs) in the Jones matrix determines the limit to what functionalities we can realize. Great efforts have been made to continuously expand the number of DOFs, and a maximal number of six has been achieved recently. However, the realization of the ultimate goal with eight DOFs (full free parameters) has been proven as a great challenge so far. Here, we show that by cascading two layer metasurfaces and utilizing the gradient descent optimization algorithm, a spatially varying Jones matrix with eight DOFs is constructed and verified numerically and experimentally in optical frequencies. Such ultimate control unlocks opportunities to design optical functionalities that are unattainable with previously known methodologies and may find wide potential applications in optical fields.
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
21. Ren, Y. et al. Full-stokes polarimetry for visible light enabled by an all-dielectric metasurface. *Adv. Photonics Res.* **3**, 2100373 (2022). [*(paper)*](https://doi.org/10.1002/adpr.202100373)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Full-stokes polarimetry for visible light enabled by an all-dielectric metasurface.jpg" 
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
       Decoding arbitrary polarization information from an optical field has triggered unprecedented endeavors in polarization imaging, remote sensing, and information processing. Therefore, developing a polarization detection device with full on-chip integration and miniaturization holds tremendous potential for many areas of optical sciences. Herein, a full-Stokes polarimetry device for visible light based on an all-dielectric metasurface is proposed. By combining both geometric phase and propagation phase modulation, the metasurface to provide two uncorrelated phase profiles for the two orthogonal states of input polarization is designed, which is then used to spatially separate the various polarization states of incident light. Through the use of a millimeter-scale multiplexed metasurface array, successful characterization of the full polarization distribution of space-variant polarization fields is further achieved. This proof-of-concept ultracompact and ultrathin metasurface is expected to open new pathways in full-Stokes polarization detection, machine vision, and navigation.
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
22. Hua, X. et al. Ultra-compact snapshot spectral light-field imaging. *Nat. Commun.* **13**, 2732 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-30439-9)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Ultra-compact snapshot spectral light-field imaging..webp" 
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
       Ideal imaging, which is constantly pursued, requires the collection of all kinds of optical information of the objects in view, such as three-dimensional spatial information (3D) including the planar distribution and depth, and the colors, i.e., spectral information (1D). Although three-dimensional spatial imaging and spectral imaging have individually evolved rapidly, their straightforward combination is a cumbersome system, severely hindering the practical applications of four-dimensional (4D) imaging. Here, we demonstrate the ultra-compact spectral light-field imaging (SLIM) by using a transversely dispersive metalens array and a monochrome imaging sensor. With only one snapshot, the SLIM presents advanced imaging with a 4 nm spectral resolution and near-diffraction-limit spatial resolution. Consequently, visually indistinguishable objects and materials can be discriminated through SLIM, which promotes significant progress towards ideal plenoptic imaging.
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
23. Zhang, C. et al. High efficiency all-dielectric pixelated metasurface for near-infrared full-stokes polarization detection. *Photonics Res.* **9**, 583–589 (2021). [*(paper)*](https://doi.org/10.1364/PRJ.415342)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/High efficiency all-dielectric pixelated metasurface for near-infrared full-stokes polarization detection.jpg" 
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
       Pixelated metasurfaces integrating both the functions of linear polarization and circular polarization filters on a single platform can achieve full-Stokes polarization detection. At present, the pixelated full-Stokes metasurfaces mainly face the following problems: low transmission, low circular dichroism (CD) of circular polarization filters, and high requirements in fabrication and integration. Herein, we propose high performance ultracompact all-dielectric pixelated full-Stokes metasurfaces in the near-infrared band based on silicon-on-insulator, which is compatible with the available semiconductor industry technologies. Circular polarization filters with high CD are achieved by using simple two-dimensional chiral structures, which can be easily integrated with the linear polarization filters on a single chip. In addition, the dielectric materials have higher transmission than metal materials with intrinsic absorption. We experimentally demonstrated the circular polarization filter with maximum CD up to 70% at a wavelength of 1.6 μm and average transmission efficiency above 80% from 1.48 μm to 1.6 μm. Therefore, our design is highly desirable for many applications, such as target detection, clinical diagnosis, and polarimetric imaging and sensing.
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
24. Diebold, A. V. et al. Passive microwave spectral imaging with dynamic metasurface apertures. *Optica* **7**, 527–536 (2020). [*(paper)*](https://doi.org/10.1364/OPTICA.386516)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Passive microwave spectral imaging with dynamic metasurface apertures.jpg" 
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
       Passive microwave imaging of incoherent sources is often approached in a lensless configuration through array-based interferometric processing. We present an alternative route in the form of a coded aperture realized using a dynamic metasurface. We demonstrate that this device can achieve an estimate of the spectral source distribution from a series of single-port spectral magnitude measurements and complex characterization of the modulation patterns. The image estimation problem is formulated in this case as compressive inversion of a set of standard linear matrix equations. In addition, we demonstrate that a dispersive metasurface design can achieve spectral encoding directly, offering the potential for spectral imaging from frequency-integrated, multiplexed measurements. The microwave dynamic metasurface aperture as an encoding structure is shown to comprise a substantially simplified hardware architecture than that employed in common passive microwave imaging systems. Our proposed technique can facilitate large scale microwave imaging applications that exploit pervasive ambient sources, while similar principles can readily be applied at terahertz, infrared, and optical frequencies.
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
25. McClung, A. et al. Snapshot spectral imaging with parallel metasystems. *Sci. Adv.* **6**, eabc7646 (2020). [*(paper)*](https://doi.org/10.1126/sciadv.abc7646)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Snapshot spectral imaging with parallel metasystems.jpeg" 
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
       Spectral imagers divide scenes into quantitative and narrowband spectral channels. They have become important metrological tools in many areas of science, especially remote sensing. Here, we propose and experimentally demonstrate a snapshot spectral imager using a parallel optical processing paradigm based on arrays of metasystems. Our multi-aperture spectral imager weighs less than 20 mg and simultaneously acquires 20 image channels across the 795- to 980-nm spectral region. Each channel is formed by a metasurface-tuned filter and a metalens doublet. The doublets incorporate absorptive field stops, reducing cross-talk between image channels. We demonstrate our instrument’s capabilities with both still images and video. Narrowband filtering, necessary for the device’s operation, also mitigates chromatic aberration, a common problem in metasurface imagers. Similar instruments operating at visible wavelengths hold promise as compact, aberration-free color cameras. Parallel optical processing using metasystem arrays enables novel, compact instruments for scientific studies and consumer electronics.
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
26. Lin, R. J. et al. Achromatic metalens array for full-colour light-field imaging. *Nat. Nanotechnol.* **14**, 227–231 (2019). [*(paper)*](https://doi.org/10.1038/s41565-018-0347-0)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Achromatic metalens array for full-colour light-field imaging.webp" 
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
       A light-field camera captures both the intensity and the direction of incoming light1,2,3,4,5. This enables a user to refocus pictures and afterwards reconstruct information on the depth of field. Research on light-field imaging can be divided into two components: acquisition and rendering. Microlens arrays have been used for acquisition, but obtaining broadband achromatic images with no spherical aberration remains challenging. Here, we describe a metalens array made of gallium nitride (GaN) nanoantennas6 that can be used to capture light-field information and demonstrate a full-colour light-field camera devoid of chromatic aberration. The metalens array contains an array of 60 × 60 metalenses with diameters of 21.65 μm. The camera has a diffraction-limited resolution of 1.95 μm under white light illumination. The depth of every object in the scene can be reconstructed slice by slice from a series of rendered images with different depths of focus. Full-colour, achromatic light-field cameras could find applications in a variety of fields such as robotic vision, self-driving vehicles and virtual and augmented reality.
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
27. Faraji-Dana, M. et al. Hyperspectral imager with folded metasurface optics. *Acs Photonics* **6**, 2161–2167 (2019). [*(paper)*](https://doi.org/10.1021/acsphotonics.9b00744)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Hyperspectral imager with folded metasurface optics.webp" 
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
       Hyperspectral imaging is a key characterization technique used in various areas of science and technology. Almost all implementations of hyperspectral imagers rely on bulky optics including spectral filters and moving or tunable elements. Here, we propose and demonstrate a line-scanning folded metasurface hyperspectral imager (HSI) that is fabricated in a single lithographic step on a 1 mm thick glass substrate. The HSI is composed of four metasurfaces, three reflective and one transmissive, that are designed to collectively disperse and focus light of different wavelengths and incident angles on a focal plane parallel to the glass substrate. With a total volume of 8.5 mm3, the HSI has spectral and angular resolutions of ∼1.5 nm and 0.075°, over the 750–850 nm and −15° to +15° degree ranges, respectively. Being compact, light weight, and easy to fabricate and integrate with image sensors and electronics, the metasurface HSI opens up new opportunities for utilizing hyperspectral imaging where strict volume and weight constraints exist. In addition, the demonstrated HSI exemplifies the utilization of metasurfaces as high-performance diffractive optical elements for implementation of advanced optical systems.
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
28. Yesilkov, F. et al. Ultrasensitive hyperspectral imaging and biodetection enabled by dielectric metasurfaces. *Nat. Photonics* **13**, 390–396 (2019). [*(paper)*](https://doi.org/10.1038/s41566-019-0394-6)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Ultrasensitive hyperspectral imaging and biodetection enabled by dielectric metasurfaces.webp" 
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
       Metasurfaces based on resonant subwavelength photonic structures enable novel ways of wavefront control and light focusing, underpinning a new generation of flat-optics devices1. Recently emerged all-dielectric asymmetric metasurfaces, composed of arrays of metaunits with broken in-plane inversion symmetry2,3,4,5,6,7, exhibit high-quality resonances originating from the intriguing physics of bound states in the continuum. Here, we combine dielectric metasurfaces and hyperspectral imaging to develop an ultrasensitive label-free analytical platform for biosensing. Our technique can acquire spatially resolved spectra from millions of image pixels and use smart data-processing tools to extract high-throughput digital sensing information at the unprecedented level of less than three molecules per μm2. We further show spectral data retrieval from a single image without using spectrometers, enabled by our unique sensor design, paving the way for portable diagnostic applications. This combination of nanophotonics and imaging optics extends the capabilities of dielectric metasurfaces to analyse biological entities and atomic-layer-thick two-dimensional materials over large areas.
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
29. Rubin, N. A. et al. Matrix fourier optics enables a compact full-Stokes polarization camera. *Science* **365**, eaax1839 (2019). [*(paper)*](https://doi.org/10.1126/science.aax1839)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Matrix fourier optics enables a compact full-Stokes polarization camera.jpeg" 
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
       Imaging the polarization of light scattered from an object provides an additional degree of freedom for gaining information from a scene. Conventional polarimeters can be bulky and usually consist of mechanically moving parts (with a polarizer and analyzer setup rotating to reveal the degree of polarization). Rubin et al. designed a metasurface-based full-Stokes compact polarization camera without conventional polarization optics and without moving parts. The results provide a simplified route for polarization imaging.
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
30. Arbabi, E. et al. Full-stokes imaging polarimetry using dielectric metasurfaces. *Acs Photonics* **5**, 3132–3140 (2018). [*(paper)*](https://doi.org/10.1021/acsphotonics.8b00362)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Full-stokes imaging polarimetry using dielectric metasurfaces.webp" 
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
       Polarization is a degree of freedom of light carrying important information that is usually absent in intensity and spectral content. Imaging polarimetry is the process of determining the polarization state of light, either partially or fully, over an extended scene. It has found several applications in various fields, from remote sensing to biology. Among different devices for imaging polarimetry, division of focal plane polarization cameras (DoFP-PCs) are more compact, less complicated, and less expensive. In general, DoFP-PCs are based on an array of polarization filters in the focal plane. Here we demonstrate a new principle and design for DoFP-PCs based on dielectric metasurfaces with the ability to control polarization and phase. Instead of polarization filtering, the method is based on splitting and focusing light in three different polarization bases. Therefore, it enables full Stokes characterization of the state of polarization and overcomes the 50% theoretical efficiency limit of the polarization-filter-based DoFP-PCs.
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
31. Stewart, J. W. et al. Toward multispectral imaging with colloidal metasurface pixels. *Adv. Mater.* **29**, 1602971 (2017). [*(paper)*](https://doi.org/10.1002/adma.201602971)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Toward multispectral imaging with colloidal metasurface pixels.jpg" 
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
       Multispectral colloidal metasurfaces are fabricated that exhibit greater than 85% absorption and ≈100 nm linewidths by patterning film-coupled nanocubes in pixels using a fusion of bottom-up and top-down fabrication techniques over wafer-scale areas. With this technique, the authors realize a multispectral pixel array consisting of six resonances between 580 and 1125 nm and reconstruct an RGB image with 9261 color combinations.
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

### 6. Optical Feature Enhancement

![](assets/feature_enhancement.png)

1. Bi, X. et al. Concurrent image differentiation and integration processings enabled by polarization-multiplexed metasurface. *Laser Photonics Rev.* **19**, 2400718 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202400718)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Concurrent image differentiation and integration processings enabled by polarization-multiplexed metasurface.jpg" 
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
       Optical computing and image processing performed by sensor front-end metasurfaces is receiving increasing interest because of advantages such as significant reduction of latency time, energy consumption, and system complexity. Despite the rapid progress, concurrent processing, the most important feature of electronic computing, has not yet been well implemented in optical computing. Here, a metasurface-based optical image processor that can perform optical differentiation and integration tasks simultaneously is proposed. This optical front-end processor integrates two coherent transfer functions corresponding to differential and integral convolution kernels into a built-in metasurface by polarization encoding, allowing concurrent processing of multiple all-optical computational tasks. The simultaneous differentiation and integration operations on images for edge enhancement and denoising are demonstrated at multiple visible wavelengths. This concurrent processing architecture paves a promising pathway toward multifunctional and higher-speed image processing for machine vision and biomedical imaging and shows the potential to expedite and potentially supplant certain digital neural network algorithms.
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
2. Zhu, Y. et al. On-site quantitative detection of fentanyl in heroin by machine learning-enabled sensors on super absorbing metasurfaces. *npj Nanophotonics* **2**, 7 (2025). [*(paper)*](https://doi.org/10.1038/s44310-025-00055-8)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/On-site quantitative detection of fentanyl in heroin by machine learning-enabled sensors on super absorbing metasurfaces.webp" 
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
       The global surge in opioid misuse, particularly fentanyl, presents a formidable public health challenge, highlighted by increasing drug-related mortalities. Our study introduces a novel approach for on-site quantitative detection of fentanyl in heroin, employing machine learning-enabled surface-enhanced Raman spectroscopy (SERS) on superabsorbing metasurfaces. The metasurface enables superior light absorption (>90%) across a broad wavelength range (580–1100 nm). This architecture facilitates significant electromagnetic field enhancement, over 2.19 × 107, ensuring high sensitivity, uniformity, and reproducibility. Our method precisely captured SERS signals across a detection range of 1–100 μg/mL in fentanyl solutions, fentanyl-heroin mixtures, and fentanyl-spiked saliva, demonstrating its versatility and practical utility. Incorporation of partial least squares regression into our analysis achieved over 93% accuracy in concentration predictions, eliminating the need for pre-data processing or specialized personnel. This marks a key advancement in rapid, accurate fentanyl detection, aiding the fight against the opioid crisis and improving public health safety.
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
3. Swartz, B. T., Zheng, H., Forcherio, G. T. & Valentine, J. Broadband and large-aperture metasurface edge encoders for incoherent infrared radiation. *Sci. Adv.* **10**, eadk0024 (2024). [*(paper)*](https://doi.org/10.1126/sciadv.adk0024)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Broadband and large-aperture metasurface edge encoders for incoherent infrared radiation.jpg" 
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
       The prevalence of computer vision systems necessitates hardware-based approaches to relieve the high computational demand of deep neural networks in resource-limited applications. One solution would be to off-load low-level image feature extraction, such as edge detection, from the digital network to the analog imaging system. To that end, this work demonstrates incoherent, broadband, low-noise optical edge detection of real-world scenes by combining the wavefront shaping of a 24-mm aperture metasurface with a refractive lens. An inverse design approach is used to optimize the metasurface for Laplacian-based edge detection across the 7.5- to 13.5-μm LWIR imaging band, allowing for facile integration with uncooled microbolometer-based LWIR imagers to encode edge information. A polarization multiplexed approach leveraging a birefringent metasurface is also demonstrated as a single-aperture implementation. This work could be applied to improve computer vision capabilities of resource-constrained systems by leveraging optical preprocessing to alleviate the computational requirements for high-accuracy image segmentation and classification.
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
4. Meng, J., Balendhran, S., Sabri, Y., Bhargava, S. K. & Crozier, K. B. Smart mid-infrared metasurface microspectrometer gas sensing system. *Microsyst. Nanoeng.* **10**, 74 (2024). [*(paper)*](https://doi.org/10.1038/s41378-024-00697-2)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Smart mid-infrared metasurface microspectrometer gas sensing system.webp" 
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
       Smart, low-cost and portable gas sensors are highly desired due to the importance of air quality monitoring for environmental and defense-related applications. Traditionally, electrochemical and nondispersive infrared (IR) gas sensors are designed to detect a single specific analyte. Although IR spectroscopy-based sensors provide superior performance, their deployment is limited due to their large size and high cost. In this study, a smart, low-cost, multigas sensing system is demonstrated consisting of a mid-infrared microspectrometer and a machine learning algorithm. The microspectrometer is a metasurface filter array integrated with a commercial IR camera that is consumable-free, compact ( ~ 1 cm3) and lightweight ( ~ 1 g). The machine learning algorithm is trained to analyze the data from the microspectrometer and predict the gases present. The system detects the greenhouse gases carbon dioxide and methane at concentrations ranging from 10 to 100% with 100% accuracy. It also detects hazardous gases at low concentrations with an accuracy of 98.4%. Ammonia can be detected at a concentration of 100 ppm. Additionally, methyl-ethyl-ketone can be detected at its permissible exposure limit (200 ppm); this concentration is considered low and nonhazardous. This study demonstrates the viability of using machine learning with IR spectroscopy to provide a smart and low-cost multigas sensing platform.
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
5. Tan, H., Meng, J. & Crozier, K. B. Multianalyte detection with metasurface-based midinfrared microspectrometer. *ACS Sens.* **9**, 5839–5847 (2024). [*(paper)*](https://doi.org/10.1021/acssensors.4c01220)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multianalyte detection with metasurface-based midinfrared microspectrometer.webp" 
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
       Midinfrared (2.5–25 μm) spectroscopy is an ideal tool for identifying chemicals in a nondestructive manner. The traditional platform is a Fourier transform infrared (FTIR) spectrometer, but this is too bulky, expensive, and power-hungry for many applications. There is therefore a growing demand for small, lightweight, and cost-effective microspectrometers for use in the field. One emerging platform is the filter-array detector-array microspectrometer. It pairs a broadband detector array with a thin and rigid array of spectral filters to offer a robust, compact platform for real-time in situ sensing. However, most demonstrations have only focused on identifying a single chemical against a null sample, even though many applications would involve multianalyte detection. In this work, we show a rare attempt at simultaneously tracking multiple analytes with a metasurface filter-array microspectrometer. The metasurface consists of periodic lattices of subwavelength circular apertures in an aluminum layer to create an array of bandpass filters. The filter array is imaged with an off-the-shelf microbolometer via a reverse-lens imaging setup to simultaneously monitor the concentration of ethanol and methanol in gasoline. This represents an important application of fuel quality monitoring. Chemometric models (PLS and SVR) are trained and tested on gasoline blends with ethanol and methanol contents, both ranging from 0% to 20% v/v. A support vector machine regression (SVR) model with a cubic kernel was found to have the lowest combined prediction errors. The root-mean-square-error of prediction (RMSEP) for ethanol and methanol are 1.23% and 1.84% v/v; the corresponding pseudounivariate limit of detection is found to be 4.22% and 6.86% v/v, respectively. This work takes the emerging field of metasurface-based mid-infrared spectrometers from single- to multianalyte detection, thereby considerably expanding their range of potential applications.
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
6. He, C. et al. Pluggable multitask diffractive neural networks based on cascaded metasurfaces. *Opto-Electron. Adv.* **7**, 230005 (2024). [*(paper)*](https://doi.org/10.29026/oea.2024.230005)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Pluggable multitask diffractive neural networks based on cascaded metasurfaces.jpg" 
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
       Optical neural networks have significant advantages in terms of power consumption, parallelism, and high computing speed, which has intrigued extensive attention in both academic and engineering communities. It has been considered as one of the powerful tools in promoting the fields of imaging processing and object recognition. However, the existing optical system architecture cannot be reconstructed to the realization of multi-functional artificial intelligence systems simultaneously. To push the development of this issue, we propose the pluggable diffractive neural networks (P-DNN), a general paradigm resorting to the cascaded metasurfaces, which can be applied to recognize various tasks by switching internal plug-ins. As the proof-of-principle, the recognition functions of six types of handwritten digits and six types of fashions are numerical simulated and experimental demonstrated at near-infrared regimes. Encouragingly, the proposed paradigm not only improves the flexibility of the optical neural networks but paves the new route for achieving high-speed, low-power and versatile artificial intelligence systems.
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
7. Tanriover, I., Dereshgi, S. A. & Aydin, K. Metasurface enabled broadband all optical edge detection in visible frequencies. *Nat. Commun.* **14**, 6484 (2023). [*(paper)*](https://doi.org/10.1038/s41467-023-42271-w)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface enabled broadband all optical edge detection in visible frequencies.webp" 
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
       Image processing is of fundamental importance for numerous modern technologies. In recent years, due to increasing demand for real-time and continuous data processing, metamaterial and metasurface based all-optical computation techniques emerged as a promising alternative to digital computation. Most of the pioneer research focused on all-optical edge detection as a fundamental step of image processing. Metasurfaces have been shown to enable real time edge detection with low to no power consumption. However, the previous demonstrations were subjected to the several limitations such as need for oblique-incidence, polarization dependence, need for additional polarizers, narrow operation bandwidth, being limited with processing in 1D, operation with coherent light only, and requiring digital post-processing. Here, we propose and experimentally demonstrate 2D isotropic, polarization-independent, broadband edge detection with high transmission efficiency under both coherent and incoherent illumination along the visible frequency range using a metasurface based on Fourier optics principles.
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
8. Wang, S. et al. Metalens for accelerated optoelectronic edge detection under ambient illumination. *Nano Lett.* **24**, 356–361 (2023). [*(paper)*](https://doi.org/10.1021/acs.nanolett.3c04112)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/etalens for accelerated optoelectronic edge detection under ambient illumination.webp" 
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
       Analog systems may allow image processing, such as edge detection, with low computational power. However, most demonstrated analog systems, based on either conventional 4-f imaging systems or nanophotonic structures, rely on coherent laser sources for illumination, which significantly restricts their use in routine imaging tasks with ambient, incoherent illumination. Here, we demonstrated a metalens-assisted imaging system that can allow optoelectronic edge detection under ambient illumination conditions. The metalens was designed to generate polarization-dependent optical transfer functions (OTFs), resulting in a synthetic OTF with an isotropic high-pass frequency response after digital subtraction. We integrated the polarization-multiplexed metalens with a polarization camera and experimentally demonstrated single-shot edge detection of indoor and outdoor scenes, including a flying airplane, under ambient sunlight illumination. The proposed system showcased the potential of using polarization multiplexing for the construction of complex optical convolution kernels toward accelerated machine vision tasks such as object detection and classification under ambient illumination.
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
9.  Xu, D. et al. All-optical object identification and three-dimensional reconstruction based on optical computing metasurface. *Opto-Electron. Adv.* **6**, 230120 (2023). [*(paper)*](https://doi.org/10.29026/oea.2023.230120)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/All-optical object identification and three-dimensional reconstruction based on optical computing metasurface.jpg" 
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
       Object identification and three-dimensional reconstruction techniques are always attractive research interests in machine vision, virtual reality, augmented reality, and biomedical engineering. Optical computing metasurface, as a two-dimensional artificial design component, has displayed the supernormal character of controlling phase, amplitude, polarization, and frequency distributions of the light beam, capable of performing mathematical operations on the input light field. Here, we propose and demonstrate an all-optical object identification technique based on optical computing metasurface, and apply it to 3D reconstruction. Unlike traditional mechanisms, this scheme reduces memory consumption in the processing of the contour surface extraction. The identification and reconstruction of experimental results from high-contrast and low-contrast objects agree well with the real objects. The exploration of the all-optical object identification and 3D reconstruction techniques provides potential applications of high efficiencies, low consumption, and compact systems.
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
10. Yang, S. et al. Realizing depth measurement and edge detection based on a single metasurface. *Nanophotonics* **12**, 3385–3393 (2023). [*(paper)*](https://doi.org/10.1515/nanoph-2023-0308)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Realizing depth measurement and edge detection based on a single metasurface.jpg" 
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
       How to simultaneously obtain the depth, edge, and other light information of the scene to accurately perceive the physical world is an important issue for imaging systems. However, such tasks usually require bulky optical components and active illumination methods. Here, we design and experimentally validate a single geometric metasurface that can achieve depth measurement or edge detection under incoherent or coherent light respectively. Double helix point source function is utilized, and three verification experiments are carried out, including double-helix beam calibration, 2D object and 3D object detection, respectively. Additionally, two-dimensional edge detection can also be achieved. This compact imaging system can enable new applications in various fields, from machine vision to microscopy.
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
11. Qu, G. et al. All-dielectric metasurface empowered optical-electronic hybrid neural networks. *Laser Photonics Rev.* **16**, 2100732 (2022). [*(paper)*](https://doi.org/10.1002/lpor.202100732)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/All-dielectric metasurface empowered optical-electronic hybrid neural networks.jpg" 
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
       Optical computing has a series of advantages over its electronic counterpart, e.g., low energy consumption, high speed, and intrinsic parallelism. Diffraction deep neural networks (D2NNs) are a prominent example capable of processing images directly without addressing the spatial locations of each element. Despite the great successes, the D2NNs typically utilize the multilayer framework and face the severe challenge of misalignment in the optical region. Herein, a single metasurface-based optical-electronic hybrid neural network (OENN) is proposed and experimentally demonstrated. The OENN is composed of a titanium dioxide (TiO2) metasurface and a fully-connected electronic layer. The combination of nonlocal neural layer and nonlinear transformation has significantly expanded the neural network capacity. Consequently, the classification accuracy on handwritten digits recognition can still be as high as 98.05% without employing the architecture of cascaded metasurfaces. The OENN shall shed light on the practical applications of optical computing in the visible spectrum.
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
12. Wang, H. P. et al. Noncontact electromagnetic wireless recognition for prosthesis based on intelligent metasurface. *Adv. Sci.* **9**, 2105056 (2022). [*(paper)*](https://doi.org/10.1002/advs.202105056)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Noncontact electromagnetic wireless recognition for prosthesis based on intelligent metasurface.jpg" 
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
       With the development of artificial intelligence and Internet of Things, hand gesture recognition techniques have attracted great attention owing to their excellent applications in developing human-machine interaction (HMI). Here, the authors propose a non-contact hand gesture recognition method based on intelligent metasurface. Owing to the advantage of dynamically controlling the electromagnetic (EM) focusing in the wavefront engineering, a transmissive programmable metasurface is presented to illuminate the forearm with more focusing spots and obtain comprehensive echo data, which can be processed under the machine learning technology to reach the non-contact gesture recognition with high accuracy. Compared with the traditional passive antennas, unique variations of echo coefficients resulted from near fields perturbed by finger and wrist agonist muscles can be aquired through the programmable metasurface by switching the positions of EM focusing. The authors realize the gesture recognition using support vector machine algorithm based on five individual focusing spots data and all-five-spot data. The influences of the focusing spots on the gesture recognition are analyzed through linear discriminant analysis algorithm and Fisher score. Experimental verifications prove that the proposed metasurface-based non-contact wireless design can realize the classification of hand gesture recognition with higher accuracy than traditional passive antennas, and give an HMI solution.
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
13. Zhou, Y., Zheng, H., Kravchenko, I. I. & Valentine, J. Flat optics for image differentiation. *Nat. Photonics* **14**, 316–323 (2020). [*(paper)*](https://doi.org/10.1038/s41566-020-0591-3)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Flat optics for image differentiation.webp" 
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
       Image processing has become a critical technology in a variety of science and engineering disciplines. Although most image processing is performed digitally, optical analog processing has the advantages of being low-power and high-speed, but it requires a large volume. Here, we demonstrate flat optics for direct image differentiation, allowing us to significantly shrink the required optical system size. We first demonstrate how the differentiator can be combined with traditional imaging systems such as a commercial optical microscope and camera sensor for edge detection with a numerical aperture up to 0.32. We next demonstrate how the entire processing system can be realized as a monolithic compound flat optic by integrating the differentiator with a metalens. The compound nanophotonic system manifests the advantage of thin form factor as well as the ability to implement complex transfer functions, and could open new opportunities in applications such as biological imaging and computer vision.
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
14. Weng, J. et al. Meta-neural-network for real-time and passive deep-learning-based object recognition. *Nat. Commun.* **11**, 6309 (2020). [*(paper)*](https://doi.org/10.1038/s41467-020-19693-x)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-neural-network for real-time and passive deep-learning-based object recognition.webp" 
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
       Analyzing scattered wave to recognize object is of fundamental significance in wave physics. Recently-emerged deep learning technique achieved great success in interpreting wave field such as in ultrasound non-destructive testing and disease diagnosis, but conventionally need time-consuming computer postprocessing or bulky-sized diffractive elements. Here we theoretically propose and experimentally demonstrate a purely-passive and small-footprint meta-neural-network for real-time recognizing complicated objects by analyzing acoustic scattering. We prove meta-neural-network mimics a standard neural network despite its compactness, thanks to unique capability of its metamaterial unit-cells (dubbed meta-neurons) to produce deep-subwavelength phase shift as training parameters. The resulting device exhibits the “intelligence” to perform desired tasks with potential to overcome the current limitations, showcased by two distinctive examples of handwritten digit recognition and discerning misaligned orbital-angular-momentum vortices. Our mechanism opens the route to new metamaterial-based deep-learning paradigms and enable conceptual devices automatically analyzing signals, with far-reaching implications for acoustics and related fields.
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
15. Zhou, J. et al. Optical edge detection based on high-efficiency dielectric metasurface. *Proc. Natl. Acad. Sci. USA* **116**, 11137–11140 (2019). [*(paper)*](https://doi.org/10.1073/pnas.1820636116)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/ptical edge detection based on high-efficiency dielectric metasurface.jpeg" 
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
       Optical edge detection is a useful method for characterizing boundaries, which is also in the forefront of image processing for object detection. As the field of metamaterials and metasurface is growing fast in an effort to miniaturize optical devices at unprecedented scales, experimental realization of optical edge detection with metamaterials remains a challenge and lags behind theoretical proposals. Here, we propose a mechanism of edge detection based on a Pancharatnam–Berry-phase metasurface. We experimentally demonstrated broadband edge detection using designed dielectric metasurfaces with high optical efficiency. The metasurfaces were fabricated by scanning a focused laser beam inside glass substrate and can be easily integrated with traditional optical components. The proposed edge-detection mechanism may find important applications in image processing, high-contrast microscopy, and real-time object detection on compact optical platforms such as mobile phones and smart cameras.
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
16. Li, L. et al. Intelligent metasurface imager and recognizer. *Light Sci. Appl.* **8**, 97 (2019). [*(paper)*](https://doi.org/10.1038/s41377-019-0209-z)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Intelligent metasurface imager and recognizer.webp" 
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
       There is an increasing need to remotely monitor people in daily life using radio-frequency probe signals. However, conventional systems can hardly be deployed in real-world settings since they typically require objects to either deliberately cooperate or carry a wireless active device or identification tag. To accomplish complicated successive tasks using a single device in real time, we propose the simultaneous use of a smart metasurface imager and recognizer, empowered by a network of artificial neural networks (ANNs) for adaptively controlling data flow. Here, three ANNs are employed in an integrated hierarchy, transforming measured microwave data into images of the whole human body, classifying specifically designated spots (hand and chest) within the whole image, and recognizing human hand signs instantly at a Wi-Fi frequency of 2.4 GHz. Instantaneous in situ full-scene imaging and adaptive recognition of hand signs and vital signs of multiple non-cooperative people were experimentally demonstrated. We also show that the proposed intelligent metasurface system works well even when it is passively excited by stray Wi-Fi signals that ubiquitously exist in our daily lives. The reported strategy could open up a new avenue for future smart cities, smart homes, human-device interaction interfaces, health monitoring, and safety screening free of visual privacy issues.
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
17. Li, L. et al. Machine-learning reprogrammable metasurface imager. *Nat. Commun.* **10**, 1082 (2019). [*(paper)*](https://doi.org/10.1038/s41467-019-09103-2)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Machine-learning reprogrammable metasurface imager.webp" 
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
       Conventional microwave imagers usually require either time-consuming data acquisition, or complicated reconstruction algorithms for data post-processing, making them largely ineffective for complex in-situ sensing and monitoring. Here, we experimentally report a real-time digital-metasurface imager that can be trained in-situ to generate the radiation patterns required by machine-learning optimized measurement modes. This imager is electronically reprogrammed in real time to access the optimized solution for an entire data set, realizing storage and transfer of full-resolution raw data in dynamically varying scenes. High-accuracy image coding and recognition are demonstrated in situ for various image sets, including hand-written digits and through-wall body gestures, using a single physical hardware imager, reprogrammed in real time. Our electronically controlled metasurface imager opens new venues for intelligent surveillance, fast data acquisition and processing, imaging at various frequencies, and beyond.
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
18. Miyazaki, H. et al. Dual-band infrared metasurface thermal emitter for CO2 sensing. *Appl. Phys. Lett.* **105**, 121107 (2014). [*(paper)*](https://doi.org/10.1063/1.4896545)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Dual-band infrared metasurface thermal emitter for CO2 sensing.jpeg" 
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
       Polarization- and angle-independent, dual-band metasurface thermal emitter was developed. The metasurface emits radiation at 4.26 μm and 3.95 μm, conventionally used for CO2 sensing. The metasurface is based on a planar Au/Al2O3/Au structure, in which orthogonal rectangular Au patches are arrayed alternately, and generates nearly perfect blackbody radiation with an emittance as high as 0.97. The metasurface is integrated on a resistive heater mounted on a SiN membrane, so that the infrared waves are produced by applying a voltage. The metasurface emitter was incorporated into an actual CO2 sensing system and was demonstrated to reduce the electric power needed by about 30% compared with a conventional blackbody emitter by suppressing unnecessary radiation.
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

### 7. Holographic Field Reconstruction

![](assets/holographic_field_reconstruction.png)

1. Aththanayake, A. et al. Tunable holographic metasurfaces for augmented and virtual reality. *Nanophotonics* (2025). [*(paper)*](https://doi.org/10.1515/nanoph-2024-0734)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Tunable holographic metasurfaces for augmented and virtual reality.jpg" 
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
       Augmented and virtual reality (AR/VR) is transforming how humans interact with technology in a wide range of fields and industries, from healthcare and education to entertainment. However, current device limitations have impeded wider integration. Tunable holographic metasurfaces represent a promising platform for revolutionizing AR/VR devices by precisely controlling light at the subwavelength scale. This article examines current challenges and opportunities from both the AR/VR and holographic metamaterial perspectives and explores how improvements to state-of-the-art approaches can address these challenges. In particular, we propose a focus on easily manufacturable and broadly electrically tunable metasurface technologies including liquid crystal integration and excitonic tuning in 2D materials. Advanced metasurface optimization techniques including machine learning will also be crucial for exploring the large design space.
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
2. Jue, J. et al. Three-photon direct laser writing of the qd-polymer metasurface for large field-of-view optical holography. *ACS Appl. Mater. Interfaces* **17**, 14520–14526 (2025). [*(paper)*](https://doi.org/10.1021/acsami.4c21233)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Three-photon direct laser writing of the qd-polymer metasurface for large field-of-view optical holography.webp" 
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
       Conventional metasurface holography based on special structural designs is extremely sensitive to the angle of the incident light. Without complex angle optimization for metasurface units, even a small increase in the angle may lead to a rapid decrease in the diffraction efficiency and loss of imaging information. Moreover, the response spectral range of most metasurface holographies cannot be freely adjusted from ultraviolet to infrared. In this study, we prepare a quantum dot (QD)–polymer material system and introduce 1035 nm three-photon direct laser writing (DLW) technology to fabricate the QD–polymer metasurface for large field-of-view optical holography. Based on the stable light absorption characteristics and insensitivity to the angle of incident light of QDs, we achieve a binary amplitude-only holography with a large field of view of ±70°. Moreover, based on the quantum confinement effect of the QDs, the tunable broadband characteristic of the QD–polymer metasurface holography from the ultraviolet to near-infrared is demonstrated, and the binary amplitude-only holography also shows polarization independence. In addition, based on the QD–polymer material system, we can realize a Pancharatnam–Berry phase holography. DLW-processed QD–polymer metasurfaces have the potential to maintain a long-term stability. This study provides a material system and a versatile and flexible technology for realizing various nanoparticle–polymer metasurface holography with a large field of view and tunable broadband characteristics.
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
3. Meng, W. et al. Ultranarrow-linewidth wavelength-vortex metasurface holography. *Sci. Adv.* **11**, eadl9159 (2025). [*(paper)*](https://doi.org/10.1126/sciadv.adt9159)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Ultranarrow-linewidth wavelength-vortex metasurface holography..jpg" 
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
       Metasurface holograms harness multiple degrees of freedom of light to enhance information channel capacity. Traditionally, wavelength multiplexing holography with high-capacity information channel was only achievable through 3D volume holograms using Bragg diffraction. Here, we demonstrate ultranarrow-linewidth wavelength-vortex multiplexing holography in metasurface holograms. By applying elementary dispersion engineering, we develop a sparse k-vector–filtering aperture array in momentum space, enabling sharp wavelength selectivity combined with orbital angular momentum selectivity. Further leveraging transformer neural networks for the design of phase-only holograms, we showcase the reconstruction of up to 118 independent images from a single hologram, achieving a simulated ultranarrow linewidth of 2 nanometers within the visible range. We apply these developed metasurface holograms for holographic visual cryptography, attaining unprecedented security levels with an information rate over 2500 times higher than traditional methods. Our results open exciting avenues for the application of metasurface holograms in various fields, including 3D displays, holographic encryption, and optical artificial intelligence.
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
4. Yin, Y. et al. Color holographic display based on complex-amplitude metasurface. *Laser Photonics Rev.* **19**, 2400884 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202400884)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Color holographic display based on complex-amplitude metasurface.jpg" 
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
       Holography is an ideal solution for truly 3D display. Complex-amplitude hologram can realize high quality reconstructions compared to amplitude-only hologram and phase-only hologram. It is difficult for conventional spatial light modulators to achieve complex-amplitude holographic display while ensuring temporal and spatial resolution, let alone color complex-amplitude holographic display. Benefiting from the subwavelength pixel size and the powerful multi-dimensional electromagnetic wave control capabilities, a few metasurface hologram with large viewing angle, high resolution, and no high-order diffraction crosstalk based on complex-amplitude control have been studied and realized. Nevertheless, colorful complex-amplitude metasurface holography at visible frequency has not been implemented yet. Here a complex-amplitude dual-wavelength metasurface holography is proposed by using a single cross-shaped meta-atom. The polarization conversion efficiency of each wavelength channel is controlled by adjusting the geometric size, while the phase value from 0 to 2π is manipulated based on the Pancharatnam–Berry(PB) phase by rotating the meta-atom. Without spatial multiplexing, the high-resolution property of the metasurface is retained. The designed metasurface achieves dual-color holographic display in the far-field and the experimental results agree well with the simulation results. The proposed metasurface opens a pathway for high quality color holographic displays and other applications that require complex-amplitude modulation at different wavelengths.
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
5. Sun, J. & Li, T. Cascaded metalenses boost applications in near-eye display. *Light Sci. Appl.* **14**, 58 (2025). [*(paper)*](https://doi.org/10.1038/s41377-024-01699-5)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Cascaded metalenses boost applications in near-eye display.webp" 
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
       As computing and artificial intelligence progress, technologies like augmented reality (AR) and virtual reality (VR) are transferring those fancy ideas to practical applications1,2,3. A key element of AR and VR systems is the increasing need for near-eye displays. However, traditional near-eye displays are always positioned too close to the eye, making them uncomfortable for extended use4,5. To mitigate this issue, optical elements are necessary to adjust the light path and reduce eye strain and discomfort. Unfortunately, conventional refractive optical components tend to be large and bulky, while head-mounted devices require more compact optics, which constrains design possibilities. To tackle this, various compact solutions, such as pancake optics6,7, holography8, and leaky waveguides9, have been proposed. Despite their potential, these approaches encounter issues like low efficiency. Consequently, achieving a balance between portability and high performance continues to be a significant challenge.
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
6. Rao, R., Shi, Y., Wang, Z., Wan, S. & Li, Z. On-chip cascaded metasurfaces for visible wavelength division multiplexing and color-routing meta-display. *Nano Lett.* **25**, 2452–2458 (2025). [*(paper)*](https://doi.org/10.1021/acs.nanolett.4c05946)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/On-chip cascaded metasurfaces for visible wavelength division multiplexing and color-routing meta-display.webp" 
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
       Integrating metasurfaces on-chip offers a promising strategy for modulating and extracting guided waves, suggesting tremendous applications in compact wearable devices. However, despite the full acquisition of on-chip manipulation of optical parameters, including phase, amplitude, and polarization, the functionality of on-chip metasurfaces remains limited by the lack of wavelength selectivity. Here, an on-chip approach to differentiate wavelength components is proposed in the visible regime for wavelength division multiplexing (WDM). Through horizontally cascading on-chip meta-atoms with structural dimension variation and optimization, different wavelength components propagating along the waveguide would be selectively extracted, realizing meta-demultiplexing functionality. More intriguingly, color nanoprinting images or holographic displays can be correspondingly enabled. This approach surpasses conventional free-space meta-devices in terms of exhibiting improved wavelength-selective allocation and eliminating the energy waste caused by spatial multiplexing. We envision that such an on-chip cascading strategy paves the way for next-generation WDM devices in photonic integrated circuits and wearable miniature meta-displays.
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
7. Gopakumar, M. et al. Full-colour 3d holographic augmented-reality displays with metasurface waveguides. *Nature* **629**, 791–797 (2024). [*(paper)*](https://doi.org/10.1038/s41586-024-07386-0)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Full-colour 3d holographic augmented-reality displays with metasurface waveguides.webp" 
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
       Emerging spatial computing systems seamlessly superimpose digital information on the physical environment observed by a user, enabling transformative experiences across various domains, such as entertainment, education, communication and training1,2,3. However, the widespread adoption of augmented-reality (AR) displays has been limited due to the bulky projection optics of their light engines and their inability to accurately portray three-dimensional (3D) depth cues for virtual content, among other factors4,5. Here we introduce a holographic AR system that overcomes these challenges using a unique combination of inverse-designed full-colour metasurface gratings, a compact dispersion-compensating waveguide geometry and artificial-intelligence-driven holography algorithms. These elements are co-designed to eliminate the need for bulky collimation optics between the spatial light modulator and the waveguide and to present vibrant, full-colour, 3D AR content in a compact device form factor. To deliver unprecedented visual quality with our prototype, we develop an innovative image formation model that combines a physically accurate waveguide model with learned components that are automatically calibrated using camera feedback. Our unique co-design of a nanophotonic metasurface waveguide and artificial-intelligence-driven holographic algorithms represents a significant advancement in creating visually compelling 3D AR experiences in a compact wearable device.
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
8. Sun, S. et al. High-efficiency, broadband, and low-crosstalk 3d holography by multi-layer holographic-lens integrated metasurface. *APL Photonics* **9**, 086102 (2024). [*(paper)*](https://doi.org/10.1063/5.0218862)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/High-efficiency, broadband, and low-crosstalk 3d holography by multi-layer holographic-lens integrated metasurface.jpeg" 
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
       Holographic display is considered the holy grail of photorealistic three-dimensional (3D) visualization technology because it can provide arbitrary wavefronts related to the essential visual cues of 3D images. Metasurfaces with exceptional high-pixel light modulation capability are increasingly favored for implementing high-quality 3D holography. However, current 3D metasurface holography always has some trade-offs among lots of algorithmic data, acceptable time, image quality, and structure complexity. Therefore, the development of a high-efficiency 3D metasurface holography device is still necessary to meet the increasing high space bandwidth product (SBP) of 3D technology. Here, based on the holographic-lens (HL) computer-generated hologram (CGH) algorithm, we experimentally demonstrate a new 3D metasurface holography device that integrates the 3D image phase cues and multiple layers of virtual lenses with different focal lengths, which exhibits significant capabilities in terms of ultra-high spatial pixel modulation and the generation of high-quality 3D holography characterized by high-efficiency, broadband response, low-crosstalk, and reduced acceptable time. The HL-CGH algorithm was efficiently integrated into parameter-optimized α-Si nanopillar meta-atoms, enabling enhanced visualization of 3D clues in a lens-free system. The prepared 3D HL-metasurface holography presented the presence of multiple depths of a 3D holographic image across a broad spectral range (400–900 nm), providing enhanced 3D visual cues. Our work provides a new perspective on designing metasurface-driven high-SBP 3D holography.
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
9.  Yin, Y. et al. Multi-dimensional multiplexed metasurface holography by inverse design. *Adv. Mater.* **36**, 2312303 (2024). [*(paper)*](https://doi.org/10.1002/adma.202312303)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multi-dimensional multiplexed metasurface holography by inverse design.jpg" 
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
       Multi-dimensional multiplexed metasurface holography extends holographic information capacity and promises revolutionary advancements for vivid imaging, information storage, and encryption. However, achieving multifunctional metasurface holography by forward design method is still difficult because it relies heavily on Jones matrix engineering, which places high demands on physical knowledge and processing technology. To break these limitations and simplify the design process, here, an end-to-end inverse design framework is proposed. By directly linking the metasurface to the reconstructed images and employing a loss function to guide the update of metasurface, the calculation of hologram can be omitted; thus, greatly simplifying the design process. In addition, the requirements on the completeness of meta-library can also be significantly reduced, allowing multi-channel hologram to be achieved using meta-atoms with only two degrees of freedom, which is very friendly to processing. By exploiting the proposed method, metasurface hologram containing up to 12 channels of multi-wavelength, multi-plane, and multi-polarization is designed and experimentally demonstrated, which exhibits the state-of-the-art information multiplexing capacity of the metasurface composed of simple meta-atoms. This method is conducive to promoting the intelligent design of multifunctional meta-devices, and it is expected to eventually accelerate the application of meta-devices in colorful display, imaging, storage and other fields.
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
10. Wang, D. et al. Decimeter-depth and polarization addressable color 3d meta-holography. *Nat. Commun.* **15**, 8242 (2024). [*(paper)*](https://doi.org/10.1038/s41467-024-52267-9)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Decimeter-depth and polarization addressable color 3d meta-holography.webp" 
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
       Fueled by the rapid advancement of nanofabrication, metasurface has provided unprecedented opportunities for 3D holography. Large depth 3D meta-holography not only greatly increases information storage capacity, but also enables distinguishing of the relative spatial relationship of 3D objects, which has important applications in fields like optical information storage and medical diagnosis. Although the methods based on Fresnel diffraction theory can reconstruct the real depth information of 3D objects, the maximum depth is only 2 mm. Here, we develop a 3D meta-holography based on angular spectrum diffraction theory to break through the depth limit. By developing the angular spectrum diffraction theory into meta-holography, the metasurface structure with independent polarization control is used to create a polarization multiplexing 3D meta-hologram. The fabricated amorphous silicon metasurface increases the depth range by 47.5 times and realizes 0.95 dm depth reconstruction for polarization independent and different color 3D meta-hologram in visible. Such polarization controlled large-depth color meta-holography is expected to open avenue for data storage, display, information security and virtual reality.
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
11. Zhang, J. C. et al. Programmable optical meta-holograms. *Nanophotonics* **13**, 1201–1217 (2024). [*(paper)*](https://doi.org/10.1515/nanoph-2023-0544)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Programmable optical meta-holograms.jpg" 
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
       The metaverse has captured significant attention as it provides a virtual realm that cannot be experienced in the physical world. Programmable optical holograms, integral components of the metaverse, allow users to access diverse information without needing external equipment. Meta-devices composed of artificially customized nano-antennas are excellent candidates for programmable optical holograms due to their compact footprint and flexible electromagnetic manipulation. Programmable optical meta-holograms can dynamically alter reconstructed images in real-time by directly modulating the optical properties of the metasurface or by modifying the incident light. Information can be encoded across multiple channels and freely selected through switchable functionality. These advantages will broaden the range of virtual scenarios in the metaverse, facilitating further development and practical applications. This review concentrates on recent advancements in the fundamentals and applications of programmable optical meta-holograms. We aim to provide readers with general knowledge and potential inspiration for applying programmable optical meta-holograms, both intrinsic and external ways, into the metaverse for better performance. An outlook and perspective on the challenges and prospects in these rapidly growing research areas are provided.
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
12. Li, Z., Shi, Y., Dai, C. & Li, Z. On-chip-driven multicolor 3d meta-display. *Laser Photonics Rev.* **18**, 2301240 (2024). [*(paper)*](https://doi.org/10.1002/lpor.202301240)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/On-chip-driven multicolor 3d meta-display.jpg" 
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
       Integrating metasurfaces on-chip provides a promising approach to modulating and extracting the in-plane waves, which bridges the conversion between guided and free-space waves and suggests tremendous applications, including guided-wave-driven holography, photonic integrated lasers, and on-chip routers. However, despite these efforts, it remains challenging to achieve multicolor 3D holographic projections via on-chip meta-optics, along with switchability. Here, the multicolor 3D holography free from zero-order diffraction and the immersion switchable display enabled by the on-chip integrated metasurface is proposed and demonstrated. By leveraging the propagation-accumulated phase of the guided waves and exploiting an optimization algorithm, an on-chip meta-hologram driven by guided waves is developed to project both multicolor and multiplane images with independent encoding freedom. Moreover, the switch between two colorful holographic images is also demonstrated via an easily accessible immersion tuning scheme. Such an on-chip-driven meta-hologram exhibits low background noise or crosstalk with high information quality and is also free from sophisticated nanostructure searching or elaborate target-image predesigning. The proposed on-chip-driven metasurface for multicolor 3D holography promises future applications in dynamic display, virtual/augmented reality, and liquid sensing.
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
13. Fan, Z.-B. et al. Integral imaging near-eye 3d display using a nanoimprint metalens array. *eLight* **4**, 3 (2024). [*(paper)*](https://doi.org/10.1186/s43593-023-00055-1)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Integral imaging near-eye 3d display using a nanoimprint metalens array.webp" 
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
       Integral imaging (II) display, one of the most critical true-3D display technologies, has received increasing research recently. Significantly, an achromatic metalens array has realized a broadband metalens-array-based II (meta-II). However, the past micro-scale metalens arrays were incompatible with commercial micro-displays; furthermore, the elemental image array (EIA) rendering is always slow. The two hinders in device and algorithm prevent meta-II from being used for practical video-rate near-eye displays (NEDs). This research demonstrates a meta-II NED combining a commercial micro-display and a metalens array. The large-area nanoimprint technology fabricates the metalens array, and a novel real-time rendering algorithm is proposed to generate the EIA. The hardware and software efforts solve the bottlenecks of video-rate meta-II displays. We also build a see-through prototype based on our meta-II NED, demonstrating the feasibility of augmented reality. Our work explores the potential of video-rate meta-II displays, which we expect can be valuable for future virtual and augmented reality.
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
14. Liu, Z. et al. Metasurface-enabled augmented reality display: a review. *Adv. Photonics* **5**, 034001 (2023). [*(paper)*](https://doi.org/10.1117/1.AP.5.3.034001)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-enabled augmented reality display a review.png" 
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
       Augmented reality (AR) display, which superimposes virtual images on ambient scene, can visually blend the physical world and the digital world and thus opens a new vista for human–machine interaction. AR display is considered as one of the next-generation display technologies and has been drawing huge attention from both academia and industry. Current AR display systems operate based on a combination of various refractive, reflective, and diffractive optical elements, such as lenses, prisms, mirrors, and gratings. Constrained by the underlying physical mechanisms, these conventional elements only provide limited light-field modulation capability and suffer from issues such as bulky volume and considerable dispersion, resulting in large size, severe chromatic aberration, and narrow field of view of the composed AR display system. Recent years have witnessed the emerging of a new type of optical elements—metasurfaces, which are planar arrays of subwavelength electromagnetic structures that feature an ultracompact footprint and flexible light-field modulation capability, and are widely believed to be an enabling tool for overcoming the limitations faced by current AR displays. Here, we aim to provide a comprehensive review on the recent development of metasurface-enabled AR display technology. We first familiarize readers with the fundamentals of AR display, covering its basic working principle, existing conventional-optics-based solutions, as well as the associated pros and cons. We then introduce the concept of optical metasurfaces, emphasizing typical operating mechanisms, and representative phase modulation methods. We elaborate on three kinds of metasurface devices, namely, metalenses, metacouplers, and metaholograms, which have empowered different forms of AR displays. Their physical principles, device designs, and the performance improvement of the associated AR displays are explained in details. In the end, we discuss the existing challenges of metasurface optics for AR display applications and provide our perspective on future research endeavors.
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
15. Li, Z. et al. Inverse design enables large-scale high-performance meta-optics reshaping virtual reality. *Nat. Commun.* **13**, 2409 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-29973-3)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Inverse design enables large-scale high-performance meta-optics reshaping virtual reality.webp" 
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
       Meta-optics has achieved major breakthroughs in the past decade; however, conventional forward design faces challenges as functionality complexity and device size scale up. Inverse design aims at optimizing meta-optics design but has been currently limited by expensive brute-force numerical solvers to small devices, which are also difficult to realize experimentally. Here, we present a general inverse-design framework for aperiodic large-scale (20k × 20k λ2) complex meta-optics in three dimensions, which alleviates computational cost for both simulation and optimization via a fast approximate solver and an adjoint method, respectively. Our framework naturally accounts for fabrication constraints via a surrogate model. In experiments, we demonstrate aberration-corrected metalenses working in the visible with high numerical aperture, poly-chromatic focusing, and large diameter up to the centimeter scale. Such large-scale meta-optics opens a new paradigm for applications, and we demonstrate its potential for future virtual-reality platforms by using a meta-eyepiece and a laser back-illuminated micro-Liquid Crystal Display.
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
16. Li, Y. et al. Ultracompact multifunctional metalens visor for augmented reality displays. *PhotonIX* **3**, 29 (2022). [*(paper)*](https://doi.org/10.1186/s43074-022-00075-z)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Ultracompact multifunctional metalens visor for augmented reality displays.webp" 
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
       Virtual reality (VR) and augmented reality (AR) have found widespread applications in education, engineering, healthcare, and entertainment. However, these near-eye displays are often bulky and heavy, and thus are not suitable for long-term wearing. Metalenses, with an ultra-thin formfactor, subwavelength modulation scale, and high modulation flexibility, are promising candidates to replace the conventional optics in AR display systems. In this work, we proposed and fabricated a novel reflective dielectric metalens-visor based on Pancharatnam-Berry phase with see-through capability. It achieves diffraction-limited focusing behavior for the reflected red light, while keeping a good transmission spectrum in the visible region. Hence, this single piece metalens-visor can perform the function of two integrated elements simultaneously: an eyepiece and an optical combiner, which in turn greatly reduces the weight and the size of an AR display. We have implemented a proof-of-concept AR display system employing the metalens-visor, and experimentally demonstrated color AR images with good image quality. This work reveals the great potential of multi-functional metasurface devices which enables optical integration in interdisciplinary applications including wearable displays, biological imaging, and aeronautic optical instruments.
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
17. Kim, J. et al. Tunable metasurfaces towards versatile metalenses and metabolograms: a review. *Adv. Photonics* **4**, 024001 (2022). [*(paper)*](https://doi.org/10.1117/1.AP.4.2.024001)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Tunable metasurfaces towards versatile metalenses and metabolograms a review.png" 
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
        Metasurfaces have attracted great attention due to their ability to manipulate the phase, amplitude, and polarization of light in a compact form. Tunable metasurfaces have been investigated recently through the integration with mechanically moving components and electrically tunable elements. Two interesting applications, in particular, are to vary the focal point of metalenses and to switch between holographic images. We present the recent progress on tunable metasurfaces focused on metalenses and metaholograms, including the basic working principles, advantages, and disadvantages of each working mechanism. We classify the tunable stimuli based on the light source and electrical bias, as well as others such as thermal and mechanical modulation. We conclude by summarizing the recent progress of metalenses and metaholograms, and providing our perspectives for the further development of tunable metasurfaces.   
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
18. Boo, H. et al. Metasurface wavefront control for high-performance user-natural augmented reality waveguide glasses. *Sci. Rep.* **12**, 5832 (2022). [*(paper)*](https://doi.org/10.1038/s41598-022-09680-1)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface wavefront control for high-performance user-natural augmented reality waveguide glasses.webp" 
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
       Augmented reality (AR) devices, as smart glasses, enable users to see both the real world and virtual images simultaneously, contributing to an immersive experience in interactions and visualization. Recently, to reduce the size and weight of smart glasses, waveguides incorporating holographic optical elements in the form of advanced grating structures have been utilized to provide light-weight solutions instead of bulky helmet-type headsets. However current waveguide displays often have limited display resolution, efficiency and field-of-view, with complex multi-step fabrication processes of lower yield. In addition, current AR displays often have vergence-accommodation conflict in the augmented and virtual images, resulting in focusing-visual fatigue and eye strain. Here we report metasurface optical elements designed and experimentally implemented as a platform solution to overcome these limitations. Through careful dispersion control in the excited propagation and diffraction modes, we design and implement our high-resolution full-color prototype, via the combination of analytical–numerical simulations, nanofabrication and device measurements. With the metasurface control of the light propagation, our prototype device achieves a 1080-pixel resolution, a field-of-view more than 40°, an overall input–output efficiency more than 1%, and addresses the vergence-accommodation conflict through our focal-free implementation. Furthermore, our AR waveguide is achieved in a single metasurface-waveguide layer, aiding the scalability and process yield control.
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
19. Li, Z. et al. Meta-optics achieves rgb-achromatic focusing for virtual reality. *Sci. Adv.* **7**, eabe4458 (2021). [*(paper)*](https://doi.org/10.1126/sciadv.abe4458)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Meta-optics achieves rgb-achromatic focusing for virtual reality.jpeg" 
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
       Virtual and augmented realities are rapidly developing technologies, but their large-scale penetration will require lightweight optical components with small aberrations. We demonstrate millimeter-scale diameter, high-NA, submicron-thin, metasurface-based lenses that achieve diffraction-limited achromatic focusing of the primary colors by exploiting constructive interference of light from multiple zones and dispersion engineering. To illustrate the potential of this approach, we demonstrate a virtual reality system based on a home-built fiber scanning near-eye display.
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
20. Xiong, J., Hsiang, E.-L., He, Z., Zhan, T. & Wu, S.-T. Augmented reality and virtual reality displays: emerging technologies and future perspectives. *Light Sci. Appl.* **10**, 216 (2021). [*(paper)*](https://doi.org/10.1038/s41377-021-00658-8)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Augmented reality and virtual reality displays emerging technologies and future perspectives.webp" 
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
       With rapid advances in high-speed communication and computation, augmented reality (AR) and virtual reality (VR) are emerging as next-generation display platforms for deeper human-digital interactions. Nonetheless, to simultaneously match the exceptional performance of human vision and keep the near-eye display module compact and lightweight imposes unprecedented challenges on optical engineering. Fortunately, recent progress in holographic optical elements (HOEs) and lithography-enabled devices provide innovative ways to tackle these obstacles in AR and VR that are otherwise difficult with traditional optics. In this review, we begin with introducing the basic structures of AR and VR headsets, and then describing the operation principles of various HOEs and lithography-enabled devices. Their properties are analyzed in detail, including strong selectivity on wavelength and incident angle, and multiplexing ability of volume HOEs, polarization dependency and active switching of liquid crystal HOEs, device fabrication, and properties of micro-LEDs (light-emitting diodes), and large design freedoms of metasurfaces. Afterwards, we discuss how these devices help enhance the AR and VR performance, with detailed description and analysis of some state-of-the-art architectures. Finally, we cast a perspective on potential developments and research directions of these photonic devices for future AR and VR displays.
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
21. Georgi, P. et al. Optical secret sharing with cascaded metasurface holography. *Sci. Adv.* **7**, eabf9718 (2021). [*(paper)*](https://doi.org/10.1126/sciadv.abf9718)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Optical secret sharing with cascaded metasurface holography.jpeg" 
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
       Secret sharing is a well-established cryptographic primitive for storing highly sensitive information like encryption keys for encoded data. It describes the problem of splitting a secret into different shares, without revealing any information to its shareholders. Here, we demonstrate an all-optical solution for secret sharing based on metasurface holography. In our concept, metasurface holograms are used as spatially separable shares that carry encrypted messages in the form of holographic images. Two of these shares can be recombined by bringing them close together. Light passing through this stack of metasurfaces accumulates the phase shift of both holograms and optically reconstructs the secret with high fidelity. In addition, the hologram generated by each single metasurface can uniquely identify its shareholder. Furthermore, we demonstrate that the inherent translational alignment sensitivity between two stacked metasurface holograms can be used for spatial multiplexing, which can be further extended to realize optical rulers.

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
22. Kim, I. et al. Pixelated bifunctional metasurface-driven dynamic vectorial holographic color prints for photonic security platform. *Nat. Commun.* **12**, 3614 (2021). [*(paper)*](https://doi.org/10.1038/s41467-021-23814-5)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Pixelated bifunctional metasurface-driven dynamic vectorial holographic color prints for photonic security platform.webp" 
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
       Vectorial holography has gained a lot of attention due to the promise of versatile polarization control of structured light for enhanced optical security and multi-channel optical communication. Here, we propose a bifunctional metasurface which combines both structural color printing and vectorial holography with eight polarization channels towards advanced encryption applications. The structural colour prints are observed under white light while the polarization encoded holograms are reconstructed under laser illumination. To encode multiple holographic images for different polarization states, a pixelated metasurface is adopted. As a proof-of-concept, we devise an electrically tunable optical security platform incorporated with liquid crystals. The optical security platform is doubly encrypted: an image under white light is decrypted to provide the first key and the corresponding information is used to fully unlock the encrypted information via projected vectorial holographic images. Such an electrically tunable optical security platform may enable smart labels for security and anticounterfeiting applications.


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
23. Kim, J. et al. Geometric and physical configurations of meta-atoms for advanced metasurface holography. *InfoMat* **3**, 739–754 (2021). [*(paper)*](https://doi.org/10.1002/inf2.12191)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Geometric and physical configurations of meta-atoms for advanced metasurface holography.jpg" 
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
       Metasurfaces consisting of subwavelength structures, so-called meta-atoms, have steadily attracted considerable attention for advanced holography due to their advantages in terms of high-resolution holographic images, large field of view, and compact device volume. In contrast to conventional holographic displays using bulky conventional diffractive optical elements, metasurface holography enables arbitrary complex wavefront shaping with a much smaller footprint. In this review, we classify metasurface holography according to the meta-atom design methodologies, which can further expand hologram functionalities. We describe light-matter interactions, particularly in metasurface systems, using the relevant the Jones matrix to rigorously explain modulations of the amplitude, phase, and polarization of light. Six different types of meta-atoms are presented, and the corresponding achievable wavefronts that form the holographic images in the far-field are also provided. Such a simple classification will give a straightforward approach to design and further realize advanced metasurface holographic devices.



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
24. Xiong, B. et al. Realizing colorful holographic mimicry by metasurfaces. *Adv. Mater.* **33**, 2005864 (2021). [*(paper)*](https://doi.org/10.1002/adma.202005864)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Realizing colorful holographic mimicry by metasurfaces.jpg" 
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
       1Mimicry is a biological camouflage phenomenon whereby an organism can change its shape and color to resemble another object. Herein, the idea of biological mimicry and rich degrees of freedom in metasurface designs are combined to realize holographic mimicry devices. A general mathematical method, called phase matrix transformation, to accomplish the holographic mimicry process is proposed. Based on this method, a dynamic metasurface hologram is designed, which shows an image of a “bird” in the air, and a distinct image of a “fish” when the environment is changed to oil. Furthermore, to make the mimicry behavior more generic, holographic mimicry operating at dual wavelengths is also designed and experimentally demonstrated. Moreover, the fully independent phase modulation realized by phase matrix transformation makes the working efficiency of the device relatively higher than the conventional multiwavelength holographic devices with off-axis illumination or interleaved subarrays. The work potentially opens a new research paradigm interfacing bionics with nanophotonics, which may produce novel applications for optical information encryption, virtual/augmented reality (VR/AR), and military camouflage systems.


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
25. Mu, Y., Zheng, M., Qi, J., Li, H. & Qiu, J. A large field-of-view metasurface for complex-amplitude hologram breaking numerical aperture limitation. *Nanophotonics* **9**, 4749–4759 (2020). [*(paper)*](https://doi.org/10.1515/nanoph-2020-0448)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A large field-of-view metasurface for complex-amplitude hologram breaking numerical aperture limitation.jpg" 
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
       Owing to the potential to manipulate simultaneously amplitude and phase of electromagnetic wave, complex-amplitude holographic metasurfaces (CAHMs) can achieve improved image-reconstruction quality compared with amplitude-only and phase-only ones. However, prevailing design methods based on Huygens–Fresnel theory for CAHMs, e.g., Rayleigh–Sommerfeld diffraction theory (RSDT), restrict acquisition of high-precision reconstruction in a large field of view (FOV), especially in the small numerical aperture (NA) scenario. To this end, a CAHM consisting of Sine-shaped meta-atoms is proposed in a microwave region, enabled by a novel complex amplitude retrieval method, to realize large FOV holograms while breaking the large NA limitation. Calculations and full-wave simulations demonstrate that the proposed method can achieve superior-quality holograms, even for nonparaxial holograms in a relatively small NA scenario, thus improving FOV and aperture utilization efficiency of CAHMs. The reconstruction comparison of a complex multi-intensity field distribution between CAHM prototypes designed by our method and by RSDT further confirms this point. We also compare both theoretically and experimentally the CAHM by our method with the phase-only metasurface by weighted Gerchberg–Saxton algorithm. Superior-quality holograms with suppressed background noise and relieved deformation, promised by the extra amplitude manipulation freedom, is witnessed. Finally, due to its wavelength irrelevance, the proposed method is applicable to the entire spectrum, spanning from microwave to optics.


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
26. Deng, Z.-L. et al. Full-color complex-amplitude vectorial holograms based on multi-freedom metasurfaces. *Adv. Funct. Mater.* **30**, 1910610 (2020). [*(paper)*](https://doi.org/10.1002/adfm.201910610)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Full-Color Complex-Amplitude Vectorial Holograms Based on Multi-Freedom Metasurfaces.jpg" 
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
       Phase, polarization, amplitude, and frequency represent the basic dimensions of light, playing crucial roles for both fundamental light–material interactions and all major optical applications. Metasurfaces have emerged as a compact platform to manipulate these knobs, but previous metasurfaces have limited flexibility to simultaneous control them. A multi-freedom metasurface that can simultaneously and independently modulate phase, polarization, and amplitude in an analytical form is introduced, and frequency multiplexing is further realized by a k-space engineering technique. The multi-freedom metasurface seamlessly combines geometric Pancharatnam–Berry phase and detour phase, both of which are frequency independent. As a result, it allows complex-amplitude vectorial hologram at various frequencies based on the same design strategy, without sophisticated nanostructure searching of massive geometric parameters. Based on this principle, full-color complex-amplitude vectorial meta-holograms in the visible are experimentally demonstrated with a metal–insulator–metal architecture, unlocking the long-sought full potential of advanced light field manipulation through ultrathin metasurfaces.


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
27. Qu, G. et al. Reprogrammable meta-hologram for optical encryption. *Nat. Commun.* **11**, 5484 (2020). [*(paper)*](https://doi.org/10.1038/s41467-020-19312-9)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Reprogrammable meta-hologram for optical encryption.webp" 
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
       Meta-holographic encryption is a potentially important technique for information security. Despite rapid progresses in multi-tasked meta-holograms, the number of information channels available in metasurfaces is limited, making meta-holographic encryption vulnerable to some attacking algorithms. Herein, we demonstrate a re-programmable metasurface that can produce arbitrary holographic images for optical encryption. The encrypted information is divided into two matrices. These two matrices are imposed to the incident light and the metasurface, respectively. While the all-dielectric metasurface is static, the phase matrix of incident light provides additional degrees of freedom to precisely control the eventual functions at will. With a single Si metasurface, arbitrary holographic images and videos have been transported and decrypted. We hope that this work paves a more promising way to optical information encryption and authentication.


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
28. Jiang, Q., Jin, G. & Cao, L. When metasurface meets hologram: principle and advances. *Adv. Opt. Photonics* **11**, 518–576 (2019). [*(paper)*](https://doi.org/10.1364/AOP.11.000518)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/When metasurface meets hologram principle and advance.jpg" 
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
       Holography has numerous applications because of its capability of arbitrary wavefront modulation. Computer-generated holograms (CGHs) take it a big step forward. Conventional holography engineers the wavefront via phase accumulation, suffering from large size, low resolution, and small viewing angle. Metasurfaces, ultrathin two-dimensional metamaterials with subwavelength features, can manipulate the amplitude, phase, and polarization of the light, solving the above issues. In this review, advances of holography, CGH algorithms, and the principles of various metasurfaces are presented. Metasurface holography, realized by encoding the hologram in the metasurface, is investigated. Information multiplexing methods of metasurface holograms, including wavelength-multiplexed, polarization-multiplexed, complex amplitude modulated, nonlinear, and dynamic metasurfaces, are presented. The challenges and outlook of metasurface holograms are discussed.
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
29. Ren, H. et al. Metasurface orbital angular momentum holography. *Nat. Commun.* **10**, 2986 (2019). [*(paper)*](https://doi.org/10.1038/s41467-019-11030-1)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface orbital angular momentum holography.webp" 
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
       Allowing subwavelength-scale-digitization of optical wavefronts to achieve complete control of light at interfaces, metasurfaces are particularly suited for the realization of planar phase-holograms that promise new applications in high-capacity information technologies. Similarly, the use of orbital angular momentum of light as a new degree of freedom for information processing can further improve the bandwidth of optical communications. However, due to the lack of orbital angular momentum selectivity in the design of conventional holograms, their utilization as an information carrier for holography has never been implemented. Here we demonstrate metasurface orbital angular momentum holography by utilizing strong orbital angular momentum selectivity offered by meta-holograms consisting of GaN nanopillars with discrete spatial frequency distributions. The reported orbital angular momentum-multiplexing allows lensless reconstruction of a range of distinctive orbital angular momentum-dependent holographic images. The results pave the way to the realization of ultrahigh-capacity holographic devices harnessing the previously inaccessible orbital angular momentum multiplexing.


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
30. Hu, Y. et al. 3d-integrated metasurfaces for full-colour holography. *Light Sci. Appl.* **8**, 86 (2019). [*(paper)*](https://doi.org/10.1038/s41377-019-0198-y)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/3D-Integrated metasurfaces for full-colour holography.webp" 
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
       Metasurfaces enable the design of optical elements by engineering the wavefront of light at the subwavelength scale. Due to their ultrathin and compact characteristics, metasurfaces possess great potential to integrate multiple functions in optoelectronic systems for optical device miniaturisation. However, current research based on multiplexing in the 2D plane has not fully utilised the capabilities of metasurfaces for multi-tasking applications. Here, we demonstrate a 3D-integrated metasurface device by stacking a hologram metasurface on a monolithic Fabry–Pérot cavity-based colour filter microarray to simultaneously achieve low-crosstalk, polarisation-independent, high-efficiency, full-colour holography, and microprint. The dual functions of the device outline a novel scheme for data recording, security encryption, colour displays, and information processing. Our 3D integration concept can be extended to achieve multi-tasking flat optical systems by including a variety of functional metasurface layers, such as polarizers, metalenses, and others.


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
31. Lee, G.-Y. et al. Metasurface eyepiece for augmented reality. *Nat. Commun.* **9**, 4562 (2018). [*(paper)*](https://doi.org/10.1038/s41467-018-07011-5)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface eyepiece for augmented reality.webp" 
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
       Recently, metasurfaces composed of artificially fabricated subwavelength structures have shown remarkable potential for the manipulation of light with unprecedented functionality. Here, we first demonstrate a metasurface application to realize a compact near-eye display system for augmented reality with a wide field of view. A key component is a see-through metalens with an anisotropic response, a high numerical aperture with a large aperture, and broadband characteristics. By virtue of these high-performance features, the metalens can overcome the existing bottleneck imposed by the narrow field of view and bulkiness of current systems, which hinders their usability and further development. Experimental demonstrations with a nanoimprinted large-area see-through metalens are reported, showing full-color imaging with a wide field of view and feasibility of mass production. This work on novel metasurface applications shows great potential for the development of optical display systems for future consumer electronics and computer vision applications.


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
32. Li, J. et al. Addressing metasurfaces for dynamic holography and optical information encryption. *Sci. Adv.* **4**, eaaq6768 (2018). [*(paper)*](https://doi.org/10.1126/sciadv.aar6768)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Addressable metasurfaces for dynamic holography and optical information encryption.jpeg" 
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
       Metasurfaces enable manipulation of light propagation at an unprecedented level, benefitting from a number of merits unavailable to conventional optical elements, such as ultracompactness, precise phase and polarization control at deep subwavelength scale, and multifunctionalities. Recent progress in this field has witnessed a plethora of functional metasurfaces, ranging from lenses and vortex beam generation to holography. However, research endeavors have been mainly devoted to static devices, exploiting only a glimpse of opportunities that metasurfaces can offer. We demonstrate a dynamic metasurface platform, which allows independent manipulation of addressable subwavelength pixels at visible frequencies through controlled chemical reactions. In particular, we create dynamic metasurface holograms for advanced optical information processing and encryption. Plasmonic nanorods tailored to exhibit hierarchical reaction kinetics upon hydrogenation/dehydrogenation constitute addressable pixels in multiplexed metasurfaces. The helicity of light, hydrogen, oxygen, and reaction duration serve as multiple keys to encrypt the metasurfaces. One single metasurface can be deciphered into manifold messages with customized keys, featuring a compact data storage scheme as well as a high level of information security. Our work suggests a novel route to protect and transmit classified data, where highly restricted access of information is imposed.

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
33. Deng, Z.-L. & Li, G. Metasurface optical holography. *Mater. Today Phys.* **3**, 16–32 (2017). [*(paper)*](https://doi.org/10.1016/j.mtphys.2017.11.001)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface optical holography.jpg" 
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
       1Photonic metasurface, a 2D array of plasmonic or dielectric optical meta-atoms, provides a versatile and compact platform for manipulating the polarization, phase and amplitude of light. It has been used to design planar optical functional elements such as ultrathin metasurface lens, metasurface waveplates, polarization beam splitter and so on. More generally, metasurface is capable of shaping the general and complex wavefront of light through holography techniques. Compared with conventional techniques, optical holography based on metasurface provides much more flexibilities to control the polarization, view angle, dispersive color crosstalk of holographic images, and thus making the metasurface optics more practical for various applications. In this review, we firstly discuss the concept of metasurface holography based on various phase modulation mechanisms including resonant phase, geometric phase, and propagation phase, etc. Then various holographic multiplexing techniques through degrees of wavelength, polarization, spatial distribution and nonlinear optical processes are summarized. Finally, we envision the future applications of metasurface optical holography from the view of large area fabrication, reconfigurable and dynamic wavefront engineering for 3D displaying, high capacity data storage, information encryption and so on.

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
34. Li, L. et al. Electromagnetic reprogrammable coding-metasurface holograms. *Nat. Commun.* **8**, 197 (2017). [*(paper)*](https://doi.org/10.1038/s41467-017-00164-9)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Electromagnetic reprogrammable coding-metasurface holograms.webp" 
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
       Metasurfaces have enabled a plethora of emerging functions within an ultrathin dimension, paving way towards flat and highly integrated photonic devices. Despite the rapid progress in this area, simultaneous realization of reconfigurability, high efficiency, and full control over the phase and amplitude of scattered light is posing a great challenge. Here, we try to tackle this challenge by introducing the concept of a reprogrammable hologram based on 1-bit coding metasurfaces. The state of each unit cell of the coding metasurface can be switched between ‘1’ and ‘0’ by electrically controlling the loaded diodes. Our proof-of-concept experiments show that multiple desired holographic images can be realized in real time with only a single coding metasurface. The proposed reprogrammable hologram may be a key in enabling future intelligent devices with reconfigurable and programmable functionalities that may lead to advances in a variety of applications such as microscopy, display, security, data storage, and information processing.


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
35. Wan, W., Gao, J. & Yang, X. Full-color plasmonic metasurface holograms. *ACS Nano* **10**, 10671–10680 (2016). [*(paper)*](https://doi.org/10.1021/acsnano.6b05453)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Full-color plasmonic metasurface holograms.gif"
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
       Holography is one of the most attractive approaches for reconstructing optical images, due to its capability of recording both the amplitude and phase information on light scattered from objects. Recently, optical metasurfaces for manipulating the wavefront of light with well-controlled amplitude, phase, and polarization have been utilized to reproduce computer-generated holograms. However, the currently available metasurface holograms have only been designed to achieve limited colors and record either amplitude or phase information. This fact significantly limits the performance of metasurface holograms to reconstruct full-color images with low noise and high quality. Here, we report the design and realization of ultrathin plasmonic metasurface holograms made of subwavelength nanoslits for reconstructing both two- and three-dimensional full-color holographic images. The wavelength-multiplexed metasurface holograms with both amplitude and phase modulations at subwavelength scale can faithfully produce not only three primary colors but also their secondary colors. Our results will advance various holographic applications.


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
36. Wang, B. et al. Wavelength de-multiplexing metasurface hologram. *Sci. Rep.* **6**, 35657 (2016). [*(paper)*](https://doi.org/10.1038/srep35657)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Wavelength de-multiplexing metasurface hologram.webp" 
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
       A wavelength de-multiplexing metasurface hologram composed of subwavelength metallic antennas is designed and demonstrated experimentally in the terahertz (THz) regime. Different character patterns are generated at the separated working frequencies 0.50 THz and 0.63 THz which determine a narrow frequency bandwidth of 130 GHz. The two working frequencies are around the central resonance frequency of the antennas where antennas behave strong wavefront modulation. Each antenna is fully utilized to control the wavefront of the metasurface at different frequencies by an optimization algorithm. The results demonstrate a candidate way to design multi-colors optical display elements.


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

### 8. Functional Integration

![](assets/functional_integration.png)

1. Li, F. et al. Flexible intelligent microwave metasurface with shape-guided adaptive programming. *Nat. Commun.* **16**, 3161 (2025). [*(paper)*](https://doi.org/10.1038/s41467-025-58249-9)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Flexible intelligent microwave metasurface with shape-guided adaptive programming.webp" 
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
       Empowering the reconfigurable metasurfaces (RM) with the capability to be mechanically deformable highlights the possibility to manipulate the electromagnetic (EM) wave across arbitrary surfaces. Such ambition is hampered by the absence of adaptivity to shape variation in current programming strategies for RM. Herein, we present a flexible intelligent surface platform (FISP) as a solution to achieve flexible RM with highly stable performance under dynamic deformation. The geometry acquisition module in FISP enables real-time awareness of RM’s deformation with the conformal sensor array. By merging the actual shape of flexible RM into the input of the adaptive algorithm driven by the artificial neural network, the deformed flexible RM in FISP can be autonomously encoded by the bias voltage supply module to ensure robust performance under various deformation conditions. The versatility of FISP in manipulating EM waves is demonstrated by its applications in electromagnetic illusion, carpet cloaking, and data transmission, illustrating the prospects for seamlessly integrating flexible electronics and RM in the development of future EM metasurfaces.


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
2. Yang, G. et al. Nonlocal phase-change meta-optics for reconfigurable nonvolatile image processing. *Light Sci. Appl.* **14**, 1–10 (2025). [*(paper)*](https://doi.org/10.1038/s41377-025-01841-x)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Nonlocal phase-change metaoptics for reconfigurable nonvolatile image processing.webp" 
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
       The next generation of smart imaging and vision systems will require compact and tunable optical computing hardware to perform high-speed and low-power image processing. These requirements are driving the development of computing metasurfaces to realize efficient front-end analog optical pre-processors, especially for edge detection capability. Yet, there is still a lack of reconfigurable or programmable schemes, which may drastically enhance the impact of these devices at the system level. Here, we propose and experimentally demonstrate a reconfigurable flat optical image processor using low-loss phase-change nonlocal metasurfaces. The metasurface is configured to realize different transfer functions in spatial frequency space, when transitioning the phase-change material between its amorphous and crystalline phases. This enables edge detection and bright field imaging modes on the same device. The metasurface is compatible with a large numerical aperture of ~0.5, making it suitable for high resolution coherent optical imaging microscopy. The concept of phase-change reconfigurable nonlocal metasurfaces may enable emerging applications of artificial intelligence-assisted imaging and vision devices with switchable multitasking.


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
3. Xing, Z. et al. Monolithic spin-multiplexing metalens for dual-functional imaging. *Laser Photonics Rev.* **19**, 2401993 (2025). [*(paper)*](https://doi.org/10.1002/lpor.202401993)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Monolithic Spin-Multiplexing Metalens for Dual-Functional Imaging.jpg" 
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
       Optical microscopic imaging technology is an essential tool for exploring and understanding the microcosmic realm. Among various imaging modes, bright-field and spiral-phase-contrast imaging are widely used, each capable of extracting distinct morphological information from target objects. However, conventional microscopic imaging devices and systems typically operate in a single mode or require additional modules for mode switching. Here, we present a monolithic photonic spin-multiplexing metalens operating in the red and near-infrared regions, which leverages a spin-multiplexed point spread function to seamlessly switch between bright-field and spiral-phase-contrast imaging modes by simply adjusting the spin state of illumination light. The device demonstrates operational efficiency of up to 80% and imaging resolution better than 4.4 µm (228 lp mm−1) in both modes. The metalens's dual-functional imaging performance is validated with both amplitude-type (custom-made metallic patterns) and phase-type (frog tongue epithelium cells and onion epidermal cells) objects. This work provides a viable solution for compact, lightweight, and easily switchable multi-functional microscopic imaging systems, opening new avenues for applications in biomedical imaging, clinical diagnostics, and material characterization.


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
4. Sulejman, S. B. et al. Metasurfaces for infrared multimodal microscopy: phase contrast and bright field. *ACS Photonics* **12**, 1494–1506 (2025). [*(paper)*](https://doi.org/10.1021/acsphotonics.4c02097)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurfaces for infrared multimodal microscopy phase contrast and bright field.gif" 
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
       Different imaging modalities are used to visualize the diverse information carried in an optical field. Two prominent non-computational modalities include bright field and phase contrast microscopy that can create contrast in an image related to the amplitude and phase features of a sample, respectively. Often, the size and cost of the equipment typically required for these applications, such as bulky microscopes, can limit their availability to well-equipped laboratories. Furthermore, capturing both of the phase contrast and bright field images on the same camera in a microscope typically requires interchanging optical components. Metasurfaces are ultra-thin nanostructures that can merge both of these operations into a single miniaturized device in the push toward shrinking the size of imaging systems. Here, a silicon-based metasurface that supports a Mie resonance is demonstrated to perform non-computational, near-infrared phase contrast and bright field multimodal microscopy that can be tuned by changing the polarization of the illumination. We performed experiments using optical fields with phase variations synthesized by a spatial light modulator and introduced by propagation through semi-transparent samples, including C. elegans, unstained human prostate cancer cells, and breast tissue. The results demonstrate the potential of metasurfaces to be used in miniaturized optical systems for label-free point-of-care testing beyond the laboratory.


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
5. Li, N., Zhang, J., Neshev, D. N. & Sukhorukov, A. A. Angle multifunctional dichroism in metasurfaces. *ACS Photonics* **12**, 1441–1447 (2025). [*(paper)*](https://doi.org/10.1021/acsphotonics.4c01999)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Angle Multifunctional Dichroism in Metasurfaces.webp" 
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
       We demonstrate metasurfaces with strong polarization dichroism that depends on the angle of incidence. We present original designs obtained through topology optimization that selectively transmit specific linear or circular polarizations at different incident angles, while the orthogonal polarization transmission is suppressed. The designed metasurfaces exceed 95% transmission efficiency and 50× extinction ratio within the target angle ranges. The experimental characterization of fabricated metasurfaces confirms the desired operation with 90% transmission efficiency and 10× polarization extinction ratio. These results provide important insights into nonlocal and k-space engineering of metasurface response, and the results reveal new opportunities for future multifunctional and angle-selective polarization devices that can find applications in specialized optical instruments and end-user devices.


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
6. Zhou, Y. et al. Flexible metasurfaces for multifunctional interfaces. *ACS Nano* **18**, 2685–2707 (2024). [*(paper)*](https://doi.org/10.1021/acsnano.3c09310)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Flexible Metasurfaces for Multifunctional Interfaces.webp" 
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
       Optical metasurfaces, capable of manipulating the properties of light with a thickness at the subwavelength scale, have been the subject of extensive investigation in recent decades. This research has been mainly driven by their potential to overcome the limitations of traditional, bulky optical devices. However, most existing optical metasurfaces are confined to planar and rigid designs, functions, and technologies, which greatly impede their evolution toward practical applications that often involve complex surfaces. The disconnect between two-dimensional (2D) planar structures and three-dimensional (3D) curved surfaces is becoming increasingly pronounced. In the past two decades, the emergence of flexible electronics has ushered in an emerging era for metasurfaces. This review delves into this cutting-edge field, with a focus on both flexible and conformal design and fabrication techniques. Initially, we reflect on the milestones and trajectories in modern research of optical metasurfaces, complemented by a brief overview of their theoretical underpinnings and primary classifications. We then showcase four advanced applications of optical metasurfaces, emphasizing their promising prospects and relevance in areas such as imaging, biosensing, cloaking, and multifunctionality. Subsequently, we explore three key trends in optical metasurfaces, including mechanically reconfigurable metasurfaces, digitally controlled metasurfaces, and conformal metasurfaces. Finally, we summarize our insights on the ongoing challenges and opportunities in this field.


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
7. Guo, S. et al. Multifunctional metasurface: Holography and spot cloud projection. *Adv. Opt. Mater.* **12**, 2401235 (2024). [*(paper)*](https://doi.org/10.1002/adom.202401235)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multifunctional Metasurface Holography and Spot Cloud Projection.jpg" 
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
       Multifunctionality, integration, and miniaturization are the mainstream trends in modern device development. However, optical display and depth perception, essential for innovative applications like intelligent driving and mixed reality, are typically achieved separately in complex and bulky optical systems. Metasurfaces, ultrathin artificial optical surfaces with strong light–matter interaction capabilities at the nanoscale, offer a versatile platform for creating multifunctional, highly integrated, and miniaturized devices by fully exploring spatial multiplexing and utilizing variables like location, polarization, and frequency. In this study, a multifunctional metasurface that integrates meta-holography with Dammann gratings is presented. By engineering the phase profile, the device can display specific holographic images in the Fresnel region while simultaneously producing a high-density spot cloud with over 37 000 spots covering the entire half space. As a proof-of-concept, a projection and reconstruction experiment is performed to elaborate its potential for retrieving three-dimensional (3D) spatial information of real scenarios. The simultaneous generation of display and point cloud holds significant promise for applications in cutting-edge imaging technologies such as intelligent driving and robot vision.


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
8. Wang, Y. et al. Detection and anti-detection with microwave-infrared compatible camouflage using asymmetric composite metasurface. *Adv. Sci.* **11**, 2410364 (2024). [*(paper)*](https://doi.org/10.1002/advs.202410364)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Detection and anti-detection with microwave-infrared compatible camouflage using asymmetric composite metasurface.jpg" 
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
       Detection and anti-detection with multispectral camouflage are of pivotal importance, while suffer from significant challenges due to the inherent contradiction between detection and anti-detection and conflict microwave and infrared (IR) stealth mechanisms. Here, a strategy is proposed to asymmetrically control transmitted microwave wavefront under radar-IR bi-stealth scheme using composite metasurface. It is engineered composed of infrared stealth layer (IRSL), microwave absorbing layer (MAL), and asymmetric microwave transmissive structure (AMTS) with polarization conversion from top to bottom. Therein, IR emissivity, microwave reflectivity, and transmissivity are simultaneously modulated by elaborately designing the filling ratio of ITO square patches on IRSL, which ensures both efficient microwave transmission and IR camouflage. Furthermore, full-polarized backward microwave stealth is achieved on MAL by transmitting and absorbing microwaves under x- and y- polarization, respectively, while forward wavefront is controlled by precise curvature phase compensation on AMTS according to ray-tracing technology. For verification, a proof-of-concept metadevice is numerically and experimentally characterized. Both results coincide well, demonstrating spiral detective wavefront manipulation under y-polarized forward wave excitation while effective reduction of radar cross section within 8–18 GHz and low IR emissivity (<0.3) for backward detection. This strategy provides a new paradigm for integration of detection and anti-detection with multispectral camouflage.


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
9.  Armghan, A. et al. A high-performance ultra-wideband metasurface absorber and thermal emitter for solar energy harvesting and thermal applications. *Phys. Chem. Chem. Phys.* **26**, 25469–25479 (2024). [*(paper)*](https://doi.org/10.1039/D4CP03336A)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A high-performance ultra-wideband metasurface absorber and thermal emitter for solar energy harvesting and thermal applications.gif" 
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
       Solar radiation is the Earth's most plentiful renewable energy source. Metasurface-based nanostructures can store solar energy efficiently and exhibit consistent behavior when interacting with light waves. This study investigates an ultra-thin, ultra-wideband solar absorber and thermal emitter that operates in the 400–5000 nm spectrum. The proposed structure design consists of a thin MXene monolayer at the top, followed by a nickel-made fractal L-shaped resonator film mounted on a SiO2 substrate. This device achieves greater than 90% of the aggregative absorption over the 4133 nm ultra-wideband region ranging from 867 nm to 5000 nm. Within its operational band, the solar absorber exhibits excellent solar energy storage capabilities under the solar AM 1.5 model curve. Furthermore, the absorber structure maintains a stable thermal radiation efficiency of 94.5–95.5% over the temperature range of 300–700 K. In addition, the physical mechanism underlying the device's ultra-wideband high absorption characteristics is adequately explained using impedance matching theory and the distribution of surface current density at high absorption wavelengths. The proposed structure design's symmetry shows excellent resilience to polarization state variations as well as wide angular stability to maintain high absorption rate. Given all of these advantages, the proposed structure would be highly suitable for solar energy and thermal radiation applications.


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
10. Zhang, Z. et al. Multifunctional ultrathin metasurface with a low radar cross section and variable infrared emissivity. *ACS Appl. Mater. Interfaces* **16**, 21109–21117 (2024). [*(paper)*](https://doi.org/10.1021/acsami.4c01798)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multifunctional ultrathin metasurface with a low radar cross section and variable infrared emissivity.gif" 
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
       The development of stealth devices that are compatible with both infrared (IR) and radar systems remains a significant challenge, as the material properties required for effective IR and radar stealth are often contradictory. In this work, based on an IR electrochromic device (IR-ECD), concepts of metamaterial manipulating electromagnetic waves are applied to develop a multifunctional ultrathin metasurface with a low radar cross section (RCS) and variable infrared emissivity. This paper presents a linear-to-linear polarization conversion metasurface (PCM) designed by hollowing the IR-ECD. In this way, the IR-ECD based on polyaniline (PANI) can also modulate the reflection waves in the microwave band without affecting its features in the infrared region. Thus, the proposed metasurface integrates both microwave stealth and variable infrared emissivity through a single layer. The measured results show that a 10 dB RCS reduction is achieved in the band of 8.46–9.5 GHz, and the infrared emissivity can be adjusted from 0.870 to 0.513 in the infrared stealth band of 8–14 μm. Due to the ultrathin thickness (only 0.081λ0 at 9 GHz), low RCS in the X-band, and variable infrared emissivity, the designed multifunctional stealth metasurface has promising applications on military platforms with various surrounding environments.


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
11. Yang, X., Wen, E., Bharadia, D. & Sievenpiper, D. F. Multifunctional metasurface: simultaneous beam steering, polarization conversion and phase offset. *IEEE Trans. Antennas Propag.* **72**, 4589–4593 (2024). [*(paper)*](https://doi.org/10.1109/TAP.2024.3371697)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multifunctional Metasurface Simultaneous Beam Steering, Polarization Conversion, and Phase Offset.gif" 
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
       A varactor-based reconfigurable multifunctional metasurface capable of simultaneous beam steering, polarization conversion and phase offset is proposed in this communication. The unit cell is designed to naturally decompose the incident waves into two equal-amplitude orthogonal linear components, and by integrating varactors, the reflection phase of the field components can be engineered from −180° to 180°. Taking advantage of the infinite states of the varactors, this design integrates a new function, the phase offset. After simulation validation of its capability, a four-layer 7 by 6 unit 1-D prototype is fabricated as a printed circuit board. It is experimentally demonstrated that it switches between X/Y and circular polarization with more than 0.9 polarization conversion rate (PCR), while reaching ±45° steering and ±180° phase offset.

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
12. Dong, L. et al. Metasurface-enhanced multifunctional flag nanogenerator for efficient wind energy harvesting and environmental sensing. *Nano Energy* **124**, 109508 (2024). [*(paper)*](https://doi.org/10.1016/j.nanoen.2024.109508)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-enhanced multifunctional flag nanogenerator for efficient wind energy harvesting and environmental sensing.jpg" 
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
       Wind energy, as a widely distributed and renewable energy resource, plays a crucial role in promoting self-powered wireless sensor networks and wind speed sensing. However, current research predominantly focuses on specific application purposes, lacking comprehensive investigations into integrated solutions. In this paper, a metasurface-enhanced multifunctional flag-type triboelectric nanogenerator (FTENG) is introduced, which enables efficient wind energy harvesting as well as accurate wind speed sensing over a wide range of wind speeds via the synergistic effect of metasurface treatment on the flagpole and flexible flag fixation approach. The flexible fixation maximally utilizes the upstream wake of metasurface configurations, boosting the energy harvesting power density by up to 23 times. The metasurface-enhanced FTENG with careful optimization, striking a balance between energy harvesting and sensing capabilities, achieves a linearity of 0.992 over a wind speed range of 2.3–14.4 m/s and a peak power density of 250 mW/m2. Finally, the FTENG demonstrates its excellent abilities to light LEDs, power the wireless sensor node (WSN), and serve as a self-powered environmental sensor. This work opens up an impactful possibility for developing versatile self-powered electronics by employing metasurface-enhanced wind energy harvesting techniques.

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
13. Ji, J. et al. On-chip multifunctional metasurfaces with full-parametric multiplexed jones matrix. *Nat. Commun.* **15**, 8271 (2024). [*(paper)*](https://doi.org/10.1038/s41467-024-52476-2)[*(data)*](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-52476-2/MediaObjects/41467_2024_52476_MOESM3_ESM.rar)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/On-chip multifunctional metasurfaces with full-parametric multiplexed Jones matrix.webp" 
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
       On-chip metasurface for guided wave radiation works as an upgrade of conventional grating couplers, enriching the interconnection between guided wave and free-space optical field. However, the number of controllable parameters in equivalent Jones matrix of on-chip metasurface is limited that restricts the channels for multiplexing. Here, a supercell design based on detour phase and geometric phase has been proposed to reach full-parametric modulation of Jones matrix. As proof of concept, four independent sets of amplitude-phase channels have been experimentally demonstrated through a single on-chip metasurface. Moreover, through joint modulation of three phase mechanisms including detour phase, geometric phase and propagation phase, the Jones matrix could be decoupled from forward- and backward-propagating guided waves for direction multiplexing. This work paves the way for guided wave radiation towards high-capacity multiplexing and may further extend its application in optical communications, optical displays and augmented/virtual reality.


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
14. Dai, C., Liu, T., Wang, D. & Zhou, L. Multiplexing near-and far-field functionalities with high-efficiency bi-channel metasurfaces. *PhotonIX* **5**, 11 (2024). [*(paper)*](https://doi.org/10.1186/s43074-024-00128-5)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multiplexing near- and far-field functionalities with high-efficiency bi-channel metasurfaces.webp" 
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
       Propagating waves and surface waves are two distinct types of light-transporting modes, the free control of which are both highly desired in integration photonics. However, previously realized devices are bulky in sizes, inefficient, and/or can only achieve one type of light-manipulation functionality with a single device. Here, we propose a generic approach to design bi-channel meta-devices, constructed by carefully selected meta-atoms possessing reflection phases of both structural-resonance and geometric origins, which can exhibit two distinct light-manipulation functionalities in near-field (NF) and far-field (FF) channels, respectively. After characterizing the scattering properties of basic meta-atoms and briefly stating the theoretical strategy, we design/fabricate three different meta-devices and experimentally characterize their bi-channel wave-control functionalities in the telecom regime. Our experiments show that the first two devices can multiplex the generations of NF and FF optical vortices with different topological charges, while the third one exhibits anomalous surface plasmon polariton focusing in the NF and hologram formation in the FF simultaneously. Our results expand the wave-control functionalities of metasurfaces to all wave-transporting channels, which may inspire many exciting applications in integration optics.


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
15. Yu, S. et al. Dynamic nonlocal metasurface for multifunctional integration via phase-change materials. *Nanophotonics* **13**, 4317–4325 (2024). [*(paper)*](https://doi.org/10.1515/nanoph-2024-0357)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Dynamic nonlocal metasurface for multifunctional integration via phase-change materials.jpg" 
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
       Non-local metasurface supporting geometric phases at bound states in the continuum (BIC) simultaneously enables sharp spectral resonances and spatial wavefront shaping, thus providing a diversified optical platform for multifunctional devices. However, a static nonlocal metasurface cannot manipulate multiple degrees of freedom (DOFs), making it difficult to achieve multifunctional integration and be applied in different scenarios. Here, we presented and demonstrated phase-change non-local metasurfaces that can realize dynamic manipulation of multiple DOFs including resonant frequency, Q values, band, and spatial wavefront. Accordingly, a metasurface integrating multiple distinct functions is designed, as a proof-of-concept demonstration. Utilizing the geometry phase of quasi-BIC and the tunability of vanadium dioxide (VO2), a dynamic meta-lens is achieved by tailoring spatial light response at quasi-BIC in the temperature range from room temperature to 53 °C. Simultaneously, the sharp Fano resonance of quasi-BIC enables the metasurface to serve as an optical sensor in the mid-infrared band, yielding a sensitivity of 7.96 THz/RIU at room temperature. Furthermore, at the metallic state of VO2 (80 °C), the designed metasurface converts into a mid-infrared broadband absorber, achieving higher than 80 % absorptivity and an average absorption of 90 % from 28.62 THz to 37.56 THz. The proposed metasurface enabling multifunctional performances in different temperatures can effectively improve the availability of devices and find more new and complex scenarios in sensing, imaging, and communications.


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
16. Chen, M. K. et al. A meta-device for intelligent depth perception. *Adv. Mater.* **35**, 2107465 (2023). [*(paper)*](https://doi.org/10.1002/adma.202107465)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A Meta-Device for Intelligent Depth Perception.jpg" 
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
       The optical illusion affects depth-sensing due to the limited and specific light-field information acquired by single-lens imaging. The incomplete depth information or visual deception would cause cognitive errors. To resolve this problem, an intelligent and compact depth-sensing meta-device that is miniaturized, integrated, and applicable for diverse scenes in all light levels is demonstrated. The compact and multifunction stereo vision system adopts an array with 3600 achromatic meta-lenses and a size of 1.2 × 1.2 mm2 to measure the depth over a 30 cm range with deep-learning support. The meta-lens array can act as multiple imaging lenses to collect light field information. It can also work with a light source as an active optical device to project a structured light. The meta-lens array can serve as the core functional component of a light-field imaging system under bright conditions or a structured-light projection system in the dark. The depth information in both ways can be analyzed and extracted by the convolutional neural network. This work provides a new avenue for the applications such as autonomous driving, machine vision, human–computer interaction, augmented reality, biometric identification, etc.


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
17. Lan, F. et al. Real-time programmable metasurface for terahertz multifunctional wave front engineering. *Light Sci. Appl.* **12**, 191 (2023). [*(paper)*](https://doi.org/10.1038/s41377-023-01228-w)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Real-time programmable metasurface for terahertz multifunctional wave front engineering.webp" 
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
       Terahertz (THz) technologies have become a focus of research in recent years due to their prominent role in envisioned future communication and sensing systems. One of the key challenges facing the field is the need for tools to enable agile engineering of THz wave fronts. Here, we describe a reconfigurable metasurface based on GaN technology with an array-of-subarrays architecture. This subwavelength-spaced array, under the control of a 1-bit digital coding sequence, can switch between an enormous range of possible configurations, providing facile access to nearly arbitrary wave front control for signals near 0.34 THz. We demonstrate wide-angle beam scanning with 1° of angular precision over 70 GHz of bandwidth, as well as the generation of multi-beam and diffuse wave fronts, with a switching speed up to 100 MHz. This device, offering the ability to rapidly reconfigure a propagating wave front for beam-forming or diffusively scattered wide-angle coverage of a scene, will open new realms of possibilities in sensing, imaging, and networking.


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
18. Intaravanne, Y. et al. Metasurface-enabled 3-in-1 microscopy. *ACS photonics* **10**, 544–551 (2023). [*(paper)*](https://doi.org/10.1021/acsphotonics.2c01971)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-Enabled 3-in-1 Microscopy.webp"
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
       Edge enhancement and polarization detection are critical to image transparent or low-contrast samples. However, currently available systems are limited to performing only a single functionality. To meet the requirement of system integration, there is a pressing need for a microscope with multiple functionalities. Here, we propose and develop a microscope with three different functionalities based on spatial multiplexing and polarization splitting. A novel geometric metasurface (MS) is used to realize a spiral phase profile and two phase gradient profiles along two vertical directions, which can perform such an extremely challenging optical task. This is the first demonstration of a 3-in-1 microscope that can simultaneously obtain five images with different optical properties in an imaging plane for the same sample. Imaging experiments with different samples verify its capability to simultaneously perform edge imaging, polarimetric imaging, and conventional microscope imaging. Benefiting from the compactness and multifunctionality of the optical MS device, the integration does not increase the volume of the microscope. This approach can enable users to visualize the multiple facets of samples in real-time.


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
19. Abdollahramezani, S. et al. Reconfigurable multifunctional metasurfaces employing hybrid phase-change plasmonic architecture. *Nanophotonics* **11**, 3883–3893 (2022). [*(paper)*](https://doi.org/10.1515/nanoph-2022-0271)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Reconfigurable multifunctional metasurfaces employing hybrid phase-change plasmonic architecture.jpg" 
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
       We present a hybrid device platform for creating an electrically reconfigurable metasurface formed by the integration of plasmonic nanostructures with phase-change material germanium antimony telluride (GST). By changing the phase of GST from amorphous to crystalline through Joule heating, a large range of responses from the metasurface can be achieved. Furthermore, by using the intermediate phases of GST, the metasurface can interact with the incident light in both over-coupling and under-coupling regimes, leading to an inherently broadband response. Through a detailed investigation of the nature of the fundamental modes, we demonstrate that changing the crystalline phase of the GST at the pixel-level enables an effective control over the key properties (i.e., amplitude, phase, and polarization) of incident light. This leads to the realization of a broadband electrically tunable multifunctional metadevice enabling beam switching, focusing, steering, and polarization conversion. Such a hybrid structure offers a high-speed, broadband, and nonvolatile reconfigurable paradigm for electrically programmable optical devices such as switches, holograms, and polarimeters.


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
20. Du, K. et al. Optical metasurfaces towards multifunctionality and tunability. *Nanophotonics* **11**, 1761–1781 (2022). [*(paper)*](https://doi.org/10.1515/nanoph-2021-0684)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Optical metasurfaces towards multifunctionality and tunability.jpg" 
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
       Optical metasurfaces is a rapidly developing research field driven by its exceptional applications for creating easy-to-integrate ultrathin planar optical devices. The tight confinement of the local electromagnetic fields in resonant photonic nanostructures can boost many optical effects and offer novel opportunities for the nanoscale control of light–matter interactions. However, once the structure-only metasurfaces are fabricated, their functions will be fixed, which limits it to make breakthroughs in practical applications. Recently, persistent efforts have led to functional multiplexing. Besides, dynamic light manipulation based on metasurfaces has been demonstrated, providing a footing ground for arbitrary light control in full space-time dimensions. Here, we review the latest research progress in multifunctional and tunable metasurfaces. Firstly, we introduce the evolution of metasurfaces and then present the concepts, the basic principles, and the design methods of multifunctional metasurface. Then with more details, we discuss how to realize metasurfaces with both multifunctionality and tunability. Finally, we also foresee various future research directions and applications of metasurfaces including innovative design methods, new material platforms, and tunable metasurfaces based metadevices.


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
21. Tonkaev, P. et al. Multifunctional and transformative metaphotonics with emerging materials. *Chem. Rev.* **122**, 15414–15449 (2022). [*(paper)*](https://doi.org/10.1021/acs.chemrev.1c01029)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multifunctional and Transformative Metaphotonics with Emerging Materials.webp" 
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
       Future technologies underpinning multifunctional physical and chemical systems and compact biological sensors will rely on densely packed transformative and tunable circuitry employing nanophotonics. For many years, plasmonics was considered as the only available platform for subwavelength optics, but the recently emerged field of resonant metaphotonics may provide a versatile practical platform for nanoscale science by employing resonances in high-index dielectric nanoparticles and metasurfaces. Here, we discuss the recently emerged field of metaphotonics and describe its connection to material science and chemistry. For tunabilty, metaphotonics employs a variety of the recently highlighted materials such as polymers, perovskites, transition metal dichalcogenides, and phase change materials. This allows to achieve diverse functionalities of metasystems and metasurfaces for efficient spatial and temporal control of light by employing multipolar resonances and the physics of bound states in the continuum. We anticipate expanding applications of these concepts in nanolasers, tunable metadevices, metachemistry, as well as a design of a new generation of chemical and biological ultracompact sensing devices.


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
22. Xu, X. et al. Multifunctional metamaterials for energy harvesting and vibration control. *Adv. Funct. Mater.* **32**, 2107896 (2022). [*(paper)*](https://doi.org/10.1002/adfm.202107896)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multifunctional Metamaterials for Energy Harvesting and Vibration Control.jpg" 
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
       Multifunctional metamaterials (MFMs) capable of energy harvesting and vibration control are particularly attractive for smart structures, wearable/biointegrated electronics, and intelligent robotics. Here, a novel MFM based on triboelectric nanogenerators (TENGs), which can harvest environmental energy and reduce vibration simultaneously, is reported. The unit cells of the MFM consist of a local resonator, an integrated contact- separation mode TENG, and spiral-shaped connecting beams. A multiphysics theoretical model is developed for quantitatively evaluating the performance of the MFM by including the mechanical and electrical fields interactions, which is further validated by experimental testing. It is demonstrated that the TENG-based MFM can not only effectively harvest vibration energy to power electronics but also dramatically suppress low-frequency mechanical vibration. This work provides a new design and model for developing novel TENG-based MFMs for advanced smart systems used in a variety of applications.


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
23. Zhang, J., Shao, L., Li, Z., Zhang, C. & Zhu, W. Graphene-based optically transparent metasurface capable of dual-polarized modulation for electromagnetic stealth. *ACS Appl. Mater. Interfaces* **14**, 31075–31084 (2022). [*(paper)*](https://doi.org/10.1021/acsami.2c04414)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Graphene-Based Optically Transparent Metasurface Capable of Dual-Polarized Modulation for Electromagnetic Stealth.webp" 
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
       Microwave stealth technology with optical transparency is of great significance for solar-powered aircrafts (e.g., satellites or unmanned aerial vehicles) in increasingly complex electromagnetic environments. By coating them with optically transparent absorbing materials or devices, these large-sized solar panels could avoid detection by radar while maintaining highly efficient collection of solar energy. However, conventional microwave-absorbing materials/devices for solar panels suffer from bulky volume and fixed stealth performance that significantly hinders their practicality or multifunctionality. Particularly, dynamic modulation of microwave absorption for dual polarization remains a challenge. In this paper, we propose the design, fabrication, and characterization of an optically transparent and dynamically tunable microwave-absorbing metasurface that enables dual modulations (amplitude and frequency) independently for two orthogonal linearly polarized excitations. The tunability of the proposed metasurface is guaranteed by an elaborately designed anisotropic meta-atom composed of a patterned graphene structure whose electromagnetic responses for different polarizations can be dynamically and independently controlled via bias voltages. The dual tunability in such a graphene-based absorbing metasurface is experimentally measured, which agrees well with those numerical results. We further build an equivalent lumped circuit model to analyze the physical relation between the tunable sheet resistance of graphene and the polarization-independent modulations of the metasurface. Taking into account the advantages of optical transparency and flexibility, the proposed microwave-absorbing metasurface significantly enhances the multitasking stealth performance in complex scenarios and has the potential for advanced solar energy devices.


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
24. Liu, M. et al. Multifunctional metasurfaces enabled by simultaneous and independent control of phase and amplitude for orthogonal polarization states. *Light Sci. Appl.* **10**, 107 (2021). [*(paper)*](https://doi.org/10.1038/s41377-021-00552-3)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multifunctional metasurfaces enabled by simultaneous and independent control of phase and amplitude for orthogonal polarization states.webp" 
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
       Monochromatic light can be characterized by its three fundamental properties: amplitude, phase, and polarization. In this work, we propose a versatile, transmission-mode all-dielectric metasurface platform that can independently manipulate the phase and amplitude for two orthogonal states of polarization in the visible frequency range. For proof-of-concept experimental demonstration, various single-layer metasurfaces composed of subwavelength-spaced titanium-dioxide nanopillars are designed, fabricated, and characterized to exhibit the ability of polarization-switchable multidimensional light-field manipulation, including polarization-switchable grayscale nanoprinting, nonuniform cylindrical lensing, and complex-amplitude holography. We envision the metasurface platform demonstrated here to open new possibilities toward creating compact multifunctional optical devices for applications in polarization optics, information encoding, optical data storage, and security.


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
25. Shirmanesh, G. K., Sokhoyan, R., Wu, P. C. & Atwater, H. A. Electro-optically tunable multifunctional metasurfaces. *ACS Nano* **14**, 6912–6920 (2020). [*(paper)*](https://doi.org/10.1021/acsnano.0c01269)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Electro-optically Tunable Multifunctional Metasurfaces.gif" 
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
       Shaping the flow of light at the nanoscale has been a grand challenge for nanophotonics over decades. It is now widely recognized that metasurfaces represent a chip-scale nanophotonics array technology capable of comprehensively controlling the wavefront of light via appropriately configuring subwavelength antenna elements. Here, we demonstrate a reconfigurable metasurface that is multifunctional, i.e., notionally capable of providing diverse optical functions in the telecommunication wavelength regime, using a single compact, lightweight, electronically controlled array with no moving parts. By electro-optical control of the phase of the scattered light from each identical individual metasurface element in an array, we demonstrate a single prototype multifunctional programmable metasurface that is capable of both dynamic beam steering and reconfigurable light focusing. Reconfigurable multifunctional metasurfaces with arrays of tunable optical antennas thus can perform arbitrary optical functions by programmable array-level control of scattered light phase, amplitude, and polarization, similar to dynamic and programmable memories in electronics.


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
26. Chen, S., Liu, W., Li, Z., Cheng, H. & Tian, J. Metasurface-empowered optical multiplexing and multifunction. *Adv. Mater.* **32**, 1805912 (2020). [*(paper)*](https://doi.org/10.1002/adma.201805912)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-Empowered Optical Multiplexing and Multifunction.jpg" 
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
       Metasurfaces are planar photonic elements composed of subwavelength nanostructures, which can deeply interact with light and exploit new degrees of freedom (DOF) to manipulate optical fields. In the past decade, metasurfaces have drawn great interest from the scientific community due to their profound potential to arbitrarily control light. Here, recent developments of multiplexing and multifunctional metasurfaces, which enable concurrent tasks through a dramatic compact design, are reviewed. The fundamental properties, design strategies, and applications of multiplexing and multifunctional metasurfaces are then discussed. First, recent progress on angular momentum multiplexing, including its behavior under different incident conditions, is considered. Second, a detailed overview of polarization-controlled, wavelength-selective, angle-selective, and reconfigurable multiplexing/multifunctional metasurfaces is provided. Then, the integrated and on-chip design of multifunctional metasurfaces is addressed. Finally, future directions and potential applications are presented.


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
27. Shabanpour, J., Beyraghi, S. & Cheldavi, A. Ultrafast reprogrammable multifunctional vanadium-dioxide-assisted metasurface for dynamic thz wavefront engineering. *Sci. Rep.* **10**, 8950 (2020). [*(paper)*](https://doi.org/10.1038/s41598-020-65533-9)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Ultrafast reprogrammable multifunctional vanadium-dioxide-assisted metasurface for dynamic THz wavefront engineering.webp" 
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
       In this paper, for the first time, a new generation of ultrafast reprogrammable multi-mission bias encoded metasurface is proposed for dynamic terahertz wavefront engineering by employing VO2 reversible and fast monoclinic to tetragonal phase transition. The multi-functionality of our designed VO2 based coding metasurface (VBCM) was guaranteed by elaborately designed meta-atom comprising three-patterned VO2 thin films whose operational statuses can be dynamically tuned among four states of “00”-“11” by merely changing the biasing voltage controlled by an external Field-programmable gate array platform. Capitalizing on such meta-atom design and by driving VBCM with different spiral-like and spiral-parabola-like coding sequences, single vortex beam and focused vortex beam with interchangeable orbital angular momentum modes were satisfactorily generated respectively. Additionally, by adopting superposition theorem and convolution operation, symmetric/asymmetric multiple beams and arbitrarily-oriented multiple vortex beams in pre-demined directions with different topological charges are realized. Several illustrative examples successfully have clarified that the proposed VBCM is a promising candidate for solving crucial terahertz challenges such as high data rate wireless communication where ultrafast switching between several missions is required.


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
28. Kwon, H. et al. Single-shot quantitative phase gradient microscopy using a system of multifunctional metasurfaces. *Nat. Photonics* **14**, 109–114 (2020). [*(paper)*](https://doi.org/10.1038/s41566-019-0536-x)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Single-shot quantitative phase gradient microscopy using a system of multifunctional metasurfaces.webp" 
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
       Quantitative phase imaging (QPI) of transparent samples plays an essential role in multiple biomedical applications, and miniaturizing these systems will enable their adoption into point-of-care and in vivo applications. Here, we propose a compact quantitative phase gradient microscope (QGPM) based on two dielectric metasurface layers, inspired by a classical differential interference contrast (DIC) microscope. Owing to the multifunctionality and compactness of the dielectric metasurfaces, the QPGM simultaneously captures three DIC images to generate a quantitative phase gradient image in a single shot. The volume of the metasurface optical system is on the order of 1 mm3. Imaging experiments with various phase resolution samples verify the capability to capture quantitative phase gradient data, with phase gradient sensitivity better than 92.3 mrad μm−1 and single-cell resolution. The results showcase the potential of metasurfaces for developing miniaturized QPI systems for label-free cellular imaging and point-of-care devices.


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
29. Chu, H. et al. A hybrid invisibility cloak based on integration of transparent metasurfaces and zero-index materials. *Light Sci. Appl.* **7**, 50 (2018). [*(paper)*](https://doi.org/10.1038/s41377-018-0052-7)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A hybrid invisibility cloak based on integration of transparent metasurfaces and zero-index materials.webp" 
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
       The invisibility cloak, a long-standing fantastic dream for humans, has become more tangible with the development of metamaterials. Recently, metasurface-based invisibility cloaks have been proposed and realized with significantly reduced thickness and complexity of the cloaking shell. However, the previous scheme is based on reflection-type metasurfaces and is thus limited to reflection geometry. In this work, by integrating the wavefront tailoring functionality of transparent metasurfaces and the wave tunneling functionality of zero-index materials, we have realized a unique type of hybrid invisibility cloak that functions in transmission geometry. The principle is general and applicable to arbitrary shapes. For experimental demonstration, we constructed a rhombic double-layer cloaking shell composed of a highly transparent metasurface and a double-zero medium consisting of dielectric photonic crystals with Dirac cone dispersions. The cloaking effect is verified by both full-wave simulations and microwave experimental results. The principle also reveals exciting possibilities for realizing skin-thick ultrathin cloaking shells in transmission geometry, which can eliminate the need for spatially varying extreme parameters. Our work paves a path for novel optical and electromagnetic devices based on the integration of metasurfaces and metamaterials.


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
30. Ee, H.-S. & Agarwal, R. Tunable metasurface and flat optical zoom lens on a stretchable substrate. *Nano Lett.* **16**, 2818–2823 (2016). [*(paper)*](https://doi.org/10.1021/acs.nanolett.6b00618)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Tunable Metasurface and Flat Optical Zoom Lens on a Stretchable Substrate.jpeg" 
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
       A mechanically reconfigurable metasurface that can continuously tune the wavefront is demonstrated in the visible frequency range by changing the lattice constant of a complex Au nanorod array fabricated on a stretchable polydimethylsiloxane substrate. It is shown that the anomalous refraction angle of visible light at 632.8 nm interacting with the tunable metasurface can be adjusted from 11.4° to 14.9° by stretching the substrate by ∼30%. An ultrathin flat 1.7× zoom lens whose focal length can continuously be changed from 150 to 250 μm is realized, which also demonstrates the potential of utilizing metasurfaces for reconfigurable flat optics.


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

### 9. Compact Device Integration

![](assets/compact_device_integration.png) 

1.  Bao, Y. & Li, B. Single-shot simultaneous intensity, phase, and polarization imaging with metasurface. *Natl. Sci. Rev.* **12**, nwae418 (2025). [*(paper)*](https://doi.org/10.1093/nsr/nwae418)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Single-shot simultaneous intensity, phase and polarization imaging with metasurface.jpeg" 
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
       Optical imaging of the intensity, phase and polarization distributions of optical fields is fundamental to numerous applications. Traditional methods rely on bulky optical components and require multiple measurements. Recently, metasurface-based (MS-based) imaging strategies have emerged as a promising solution to address these challenges. However, they have been primarily limited to capturing partial information of the three parameters, tailored to specific optical fields, which poses challenges when addressing arbitrary field distributions and achieving three-parameter imaging. In this study, we introduce an MS-based approach for single-shot optical imaging that simultaneously captures all three parameters of optical fields with arbitrary intensity, phase and polarization distributions. We experimentally validate the versatility of our method by conducting imaging of various types of optical fields with arbitrary well-defined distributions. The strategy presented in our work is expected to open up promising avenues for diverse applications, including imaging and optical communications.


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
2.  Chi, H. et al. Neural network-assisted end-to-end design for full light field control of meta-optics. *Adv. Mater.* **37**, 2419621 (2025). [*(paper)*](https://doi.org/10.1002/adma.202419621)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Neural Network-Assisted End-to-End Design for Full Light Field Control of Meta-Optics.jpg" 
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
       Meta-optics, with unique light-matter interactions and extensive design space, underpins versatile and compact optical devices through flexible multi-parameter light field control. However, conventional designs struggle with the intricate interdependencies of nano-structural complex responses across wavelengths and polarizations at a system level, hindering high-performance full-light field control. Here, a neural network-assisted end-to-end design framework that facilitates global, gradient-based optimization of multifunctional meta-optics layouts for full light field control is proposed. Its superiority over separated design is showcased by utilizing the limited design space for multi-wavelength-polarization holography with enhanced performance (e.g., ≈6 × structural similarity index experimentally). By harnessing the dispersive full-parameter Jones matrix, orthogonal tri-polarization multi-wavelength-depth holography is further demonstrated, breaking conventional channel limitations. To highlight its versatility, non-orthogonal polarizations (>3) are showcased for arbitrary polarized-spectral multi-information processing applications in display, imaging, and computing. The comprehensive framework elevates light field control in meta-optics, delivering superior performance, enhanced functionality, and improved reliability, thereby paving the way for next-generation intelligent optical technologies.


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
3.  Wen, S. et al. Metasurface array for single-shot spectroscopic ellipsometry. *Light Sci. Appl.* **13**, 88 (2024). [*(paper)*](https://doi.org/10.1038/s41377-024-01396-3)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface array for single-shot spectroscopic ellipsometry.webp" 
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
       Spectroscopic ellipsometry is a potent method that is widely adopted for the measurement of thin film thickness and refractive index. Most conventional ellipsometers utilize mechanically rotating polarizers and grating-based spectrometers for spectropolarimetric detection. Here, we demonstrated a compact metasurface array-based spectroscopic ellipsometry system that allows single-shot spectropolarimetric detection and accurate determination of thin film properties without any mechanical movement. The silicon-based metasurface array with a highly anisotropic and diverse spectral response is combined with iterative optimization to reconstruct the full Stokes polarization spectrum of the light reflected by the thin film with high fidelity. Subsequently, the film thickness and refractive index can be determined by fitting the measurement results to a proper material model with high accuracy. Our approach opens up a new pathway towards a compact and robust spectroscopic ellipsometry system for the high throughput measurement of thin film properties.


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
4.  Yin, Y. et al. Multi-dimensional multiplexed metasurface holography by inverse design. *Adv. Mater.* **36**, 2312303 (2024). [*(paper)*](https://doi.org/10.1002/adma.202312303)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Multi-Dimensional Multiplexed Metasurface Holography by Inverse Design.jpg" 
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
       Multi-dimensional multiplexed metasurface holography extends holographic information capacity and promises revolutionary advancements for vivid imaging, information storage, and encryption. However, achieving multifunctional metasurface holography by forward design method is still difficult because it relies heavily on Jones matrix engineering, which places high demands on physical knowledge and processing technology. To break these limitations and simplify the design process, here, an end-to-end inverse design framework is proposed. By directly linking the metasurface to the reconstructed images and employing a loss function to guide the update of metasurface, the calculation of hologram can be omitted; thus, greatly simplifying the design process. In addition, the requirements on the completeness of meta-library can also be significantly reduced, allowing multi-channel hologram to be achieved using meta-atoms with only two degrees of freedom, which is very friendly to processing. By exploiting the proposed method, metasurface hologram containing up to 12 channels of multi-wavelength, multi-plane, and multi-polarization is designed and experimentally demonstrated, which exhibits the state-of-the-art information multiplexing capacity of the metasurface composed of simple meta-atoms. This method is conducive to promoting the intelligent design of multifunctional meta-devices, and it is expected to eventually accelerate the application of meta-devices in colorful display, imaging, storage and other fields.


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
5.  Seo, J. et al. Deep-learning-driven end-to-end metalens imaging. *Adv. Photonics* **6**, 066002 (2024). [*(paper)*](https://doi.org/10.1117/1.AP.6.6.066002) [*(data)*](https://github.com/yhy258/EIDL_DRMI) [*(code)*](https://github.com/yhy258/EIDL_DRMI)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Deep-learning-driven end-to-end metalens imaging.png" 
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
       Recent advances in metasurface lenses (metalenses) have shown great potential for opening a new era in compact imaging, photography, light detection, and ranging (LiDAR) and virtual reality/augmented reality applications. However, the fundamental trade-off between broadband focusing efficiency and operating bandwidth limits the performance of broadband metalenses, resulting in chromatic aberration, angular aberration, and a relatively low efficiency. A deep-learning-based image restoration framework is proposed to overcome these limitations and realize end-to-end metalens imaging, thereby achieving aberration-free full-color imaging for mass-produced metalenses with 10 mm diameter. Neural-network-assisted metalens imaging achieved a high resolution comparable to that of the ground truth image.


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
6.  Zuo, J. et al. Chip-integrated metasurface full-Stokes polarimetric imaging sensor. *Light Sci. Appl.* **12**, 218 (2023). [*(paper)*](https://doi.org/10.1038/s41377-023-01260-w)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Chip-integrated metasurface full-Stokes polarimetric imaging sensor.webp" 
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
       Polarimetric imaging has a wide range of applications for uncovering features invisible to human eyes and conventional imaging sensors. Chip-integrated, fast, cost-effective, and accurate full-Stokes polarimetric imaging sensors are highly desirable in many applications, which, however, remain elusive due to fundamental material limitations. Here we present a chip-integrated Metasurface-based Full-Stokes Polarimetric Imaging sensor (MetaPolarIm) realized by integrating an ultrathin (~600 nm) metasurface polarization filter array (MPFA) onto a visible imaging sensor with CMOS compatible fabrication processes. The MPFA is featured with broadband dielectric-metal hybrid chiral metasurfaces and double-layer nanograting polarizers. This chip-integrated polarimetric imaging sensor enables single-shot full-Stokes imaging (speed limited by the CMOS imager) with the most compact form factor, records high measurement accuracy, dual-color operation (green and red) and a field of view up to 40 degrees. MetaPolarIm holds great promise to enable transformative applications in autonomous vision, industry inspection, space exploration, medical imaging and diagnosis.


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
7.  Cao, G. et al. Infrared metasurface-enabled compact polarization nanodevices. *Mater. Today* **50**, 499–515 (2023). [*(paper)*](https://doi.org/10.1016/j.mattod.2021.06.014)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Infrared metasurface-enabled compact polarization nanodevices.jpg" 
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
       Infrared metasurface, especially that having a working range covering wavelengths from 0.75 to 25 μm, has been exploited as a revolutionary tool to manipulate the properties of electromagnetic waves owing to its potential applications in military and civilian fields. It owns the capacity to steer electromagnetic waves within subwavelength scale, with full degrees of freedom such as phase, amplitude and polarization, allowing the development of a number of planar meta-devices including the metalens, hologram, wave-plate and polarimeter. In particular, polarization, which determines the interaction of electromagnetic waves with matter, is important in almost every area of science. However, conventional materials for infrared polarization control inevitably introduce extra optical components and bulky configurations, hindering future miniaturization and integration. Moreover, compared with their short wavelength counterparts, polarization nanodevices in the infrared band and especially those in the long-wavelength infrared region have been far less explored due to the loss of material and immature fabrication techniques. Here, we review recent progress in the development of infrared metasurfaces in terms of generating, manipulating and detecting the polarization on standard and higher-order Poincaré spheres. The principles, typical strategies and emerging applications of these processes are introduced. We also discuss the challenges and outlook of future developments in this emerging field.

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
8.  Chen, M. K. et al. A meta-device for intelligent depth perception. *Adv. Mater.* **35**, 2107465 (2023). [*(paper)*](https://doi.org/10.1002/adma.202107465)
     
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/A Meta-Device for Intelligent Depth Perception.jpg" 
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
       The optical illusion affects depth-sensing due to the limited and specific light-field information acquired by single-lens imaging. The incomplete depth information or visual deception would cause cognitive errors. To resolve this problem, an intelligent and compact depth-sensing meta-device that is miniaturized, integrated, and applicable for diverse scenes in all light levels is demonstrated. The compact and multifunction stereo vision system adopts an array with 3600 achromatic meta-lenses and a size of 1.2 × 1.2 mm2 to measure the depth over a 30 cm range with deep-learning support. The meta-lens array can act as multiple imaging lenses to collect light field information. It can also work with a light source as an active optical device to project a structured light. The meta-lens array can serve as the core functional component of a light-field imaging system under bright conditions or a structured-light projection system in the dark. The depth information in both ways can be analyzed and extracted by the convolutional neural network. This work provides a new avenue for the applications such as autonomous driving, machine vision, human–computer interaction, augmented reality, biometric identification, etc.


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
9.  Xiong, J. et al. Dynamic brain spectrum acquired by a real-time ultraspectral imaging chip with reconfigurable metasurfaces. *Optica* **9**, 461–468 (2022). [*(paper)*](https://doi.org/10.1364/OPTICA.440013)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Dynamic brain spectrum acquired by a real-time ultraspectral imaging chip with reconfigurable metasurfaces.jpg" 
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
       Spectral imaging paves the way for various fields, particularly in biomedical research. However, spectral imaging, mainly depending on spatial or temporal scanning, cannot achieve high temporal, spatial, and spectral resolution simultaneously. In this study, we demonstrated a silicon real-time ultraspectral imaging chip based on reconfigurable metasurfaces, comprising 155,216 (356*436) image-adaptive microspectrometers with ultra-high center-wavelength accuracy of 0.04 nm and spectral resolution of 0.8 nm. It is employed for imaging brain hemodynamics, and the dynamic spectral absorption properties of deoxyhemoglobin and oxyhemoglobin in a rat barrel cortex were obtained, which enlighten spectroscopy in vivo studies and other real-time applications.
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
10.  Luo, X. et al. Metasurface-enabled on-chip multiplexed diffractive neural networks in the visible. *Light Sci. Appl.* **11**, 158 (2022). [*(paper)*](https://doi.org/10.1038/s41377-022-00844-2)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-enabled on-chip multiplexed diffractive neural networks in the visible.webp" 
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
       Replacing electrons with photons is a compelling route toward high-speed, massively parallel, and low-power artificial intelligence computing. Recently, diffractive networks composed of phase surfaces were trained to perform machine learning tasks through linear optical transformations. However, the existing architectures often comprise bulky components and, most critically, they cannot mimic the human brain for multitasking. Here, we demonstrate a multi-skilled diffractive neural network based on a metasurface device, which can perform on-chip multi-channel sensing and multitasking in the visible. The polarization multiplexing scheme of the subwavelength nanostructures is applied to construct a multi-channel classifier framework for simultaneous recognition of digital and fashionable items. The areal density of the artificial neurons can reach up to 6.25 × 106 mm−2 multiplied by the number of channels. The metasurface is integrated with the mature complementary metal-oxide semiconductor imaging sensor, providing a chip-scale architecture to process information directly at physical layers for energy-efficient and ultra-fast image processing in machine vision, autonomous driving, and precision medicine.


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
11.  Hua, X. et al. Ultra-compact snapshot spectral light-field imaging. *Nat. Commun.* **13**, 2732 (2022). [*(paper)*](https://doi.org/10.1038/s41467-022-30439-9)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Ultra-compact snapshot spectral light-field imaging.webp" 
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
       Ideal imaging, which is constantly pursued, requires the collection of all kinds of optical information of the objects in view, such as three-dimensional spatial information (3D) including the planar distribution and depth, and the colors, i.e., spectral information (1D). Although three-dimensional spatial imaging and spectral imaging have individually evolved rapidly, their straightforward combination is a cumbersome system, severely hindering the practical applications of four-dimensional (4D) imaging. Here, we demonstrate the ultra-compact spectral light-field imaging (SLIM) by using a transversely dispersive metalens array and a monochrome imaging sensor. With only one snapshot, the SLIM presents advanced imaging with a 4 nm spectral resolution and near-diffraction-limit spatial resolution. Consequently, visually indistinguishable objects and materials can be discriminated through SLIM, which promotes significant progress towards ideal plenoptic imaging.


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
12.  Reshef, O. et al. An optic to replace space and its application towards ultra-thin imaging systems. *Nat. Commun.* **12**, 3512 (2021). [*(paper)*](https://doi.org/10.1038/s41467-021-23358-8)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/An optic to replace space and its application towards ultra-thin imaging systems.webp" 
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
       1Centuries of effort to improve imaging has focused on perfecting and combining lenses to obtain better optical performance and new functionalities. The arrival of nanotechnology has brought to this effort engineered surfaces called metalenses, which promise to make imaging devices more compact. However, unaddressed by this promise is the space between the lenses, which is crucial for image formation but takes up by far the most room in imaging systems. Here, we address this issue by presenting the concept of and experimentally demonstrating an optical ‘spaceplate’, an optic that effectively propagates light for a distance that can be considerably longer than the plate thickness. Such an optic would shrink future imaging systems, opening the possibility for ultra-thin monolithic cameras. More broadly, a spaceplate can be applied to miniaturize important devices that implicitly manipulate the spatial profile of light, for example, solar concentrators, collimators for light sources, integrated optical components, and spectrometers.


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
13.  Xu, B. et al. Metalens-integrated compact imaging devices for wide-field microscopy. *Adv. Photonics* **2**, 066004 (2020). [*(paper)*](https://doi.org/10.1117/1.AP.2.6.066004)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metalens-integrated compact imaging devices for wide-field microscopy.png" 
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
       Metasurfaces have demonstrated unprecedented capabilities in manipulating light with ultrathin and flat architectures. Although great progress has been made in the metasurface designs and function demonstrations, most metalenses still only work as a substitution of conventional lenses in optical settings, whose integration advantage is rarely manifested. We propose a highly integrated imaging device with silicon metalenses directly mounted on a complementary metal oxide semiconductor image sensor, whose working distance is in hundreds of micrometers. The imaging performances including resolution, signal-to-noise ratio, and field of view (FOV) are investigated. Moreover, we develop a metalens array with polarization-multiplexed dual-phase design for a wide-field microscopic imaging. This approach remarkably expands the FOV without reducing the resolution, which promises a non-limited space-bandwidth product imaging for wide-field microscopy. As a result, we demonstrate a centimeter-scale prototype for microscopic imaging, showing uniqueness of meta-design for compact integration.


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
14.  Joo, W.-J. et al. Metasurface-driven OLED displays beyond 10,000 pixels per inch. *Science* **370**, 459–463 (2020). [*(paper)*](https://doi.org/10.1126/science.abc8530)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface-driven OLED displays beyond 10,000 pixels per inch.jpeg" 
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
       Organic light-emitting diodes (OLEDs) have found wide application in high-resolution, large-area televisions and the handheld displays of smartphones and tablets. With the screen located some distance from the eye, the typical number of pixels per inch is in the region of hundreds. For near-eye microdisplays—for example, in virtual and augmented reality applications—the required pixel density runs to several thousand pixels per inch and cannot be met by present display technologies. Joo et al. developed a full-color, high-brightness OLED design based on an engineered metasurface as a tunable back-reflector. An ultrahigh density of 10,000 pixels per inch readily meets the requirements for the next-generation microdisplays that can be fabricated on glasses or contact lenses.

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
15.  Pahlevaninezhad, H. et al. Nano-optic endoscope for high-resolution optical coherence tomography in vivo. *Nat. Photonics* **12**, 540–547 (2018). [*(paper)*](https://doi.org/10.1038/s41566-018-0224-2)
      
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Nano-optic endoscope for high-resolution optical coherence tomography in vivo.webp"
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
       Acquisition of high-resolution images from within internal organs using endoscopic optical imaging has numerous clinical applications. However, difficulties associated with optical aberrations and the trade-off between transverse resolution and depth of focus significantly limit the scope of applications. Here, we integrate a metalens, with the ability to modify the phase of incident light at subwavelength level, into the design of an endoscopic optical coherence tomography catheter (termed nano-optic endoscope) to achieve near diffraction-limited imaging through negating non-chromatic aberrations. Remarkably, the tailored chromatic dispersion of the metalens in the context of spectral interferometry is utilized to maintain high-resolution imaging beyond the input field Rayleigh range, easing the trade-off between transverse resolution and depth of focus. We demonstrate endoscopic imaging in resected human lung specimens and in sheep airways in vivo. The combination of the superior resolution and higher imaging depth of focus of the nano-optic endoscope is likely to increase the clinical utility of endoscopic optical imaging.


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
16.  Colburn, S., Zhan, A. & Majumdar, A. Metasurface optics for full-color computational imaging. *Sci. Adv.* **4**, eaar2114 (2018). [*(paper)*](https://doi.org/10.1126/sciadv.aar2114)
  
     <div style="
       text-align:center;
       background-color:#f2f2f2;
       border-radius:10px;
       padding:12px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       margin-bottom:18px;
     ">
       <img 
         src="abstract image/Metasurface optics for full-color computational imaging.jpeg" 
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
       Acquisition of high-resolution images from within internal organs using endoscopic optical imaging has numerous clinical applications. However, difficulties associated with optical aberrations and the trade-off between transverse resolution and depth of focus significantly limit the scope of applications. Here, we integrate a metalens, with the ability to modify the phase of incident light at subwavelength level, into the design of an endoscopic optical coherence tomography catheter (termed nano-optic endoscope) to achieve near diffraction-limited imaging through negating non-chromatic aberrations. Remarkably, the tailored chromatic dispersion of the metalens in the context of spectral interferometry is utilized to maintain high-resolution imaging beyond the input field Rayleigh range, easing the trade-off between transverse resolution and depth of focus. We demonstrate endoscopic imaging in resected human lung specimens and in sheep airways in vivo. The combination of the superior resolution and higher imaging depth of focus of the nano-optic endoscope is likely to increase the clinical utility of endoscopic optical imaging.


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
