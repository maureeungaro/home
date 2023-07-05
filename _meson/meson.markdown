---
# Table: add first row (3 |) for autoformatting
layout: default
title: "Meson Physics"

c1:  "The Form Factor G<sub>M</sub><sup>*</sup>/3G<sub>D</sub>."
c2:  "The filled red squares are from the current CLAS experiment utilizing the Unitary Isobar Model (UIM). "
c3:  "The errors shown are statistical, while estimated systematic errors are shown as gray bars at "
c4:  "the bottom of the graph. Also shown are selected earlier published results. "
c5:  "The filled triangles correspond to a recent analysis of previous CLAS data and the filled circles arefrom an earlier JLab Hall C experiment."


d1: "The ratios R<sub>EM</sub> (upper panel) and R<sub>SM</sub> (lower panel). The filled red squares are from the current CLAS experiment"
d2: "utilizing the UIM. The errors shown are statistical, while estimated systematic"
d3: "errors are shown as gray bars at the bottom of the graph. Also shown are selected earlier published results. "
d4: "The filled triangles correspond to a recent analysis of previous CLAS data and the filled circles are from an earlier ]Lab Hall C experiment."

a1: "We report the analysis of exclusive single &pi;<sup>0</sup> electro-production in the  &Delta;(1232) resonance region at Jefferson Lab in the Q<sup>2</sup> range 2 &rarr; 6 GeV<sup>2</sup>.<br/>"


multipoles_ratiosImg:      "../assets/images/pi0/multipoles_ratios.png"
multipoles_ratiosImgf:      "../assets/images/pi0/multipoles_ratios_fixedw.png"
lpt_structure_functionImg: "../assets/images/pi0/q2-3.00_sf-LPT_runningvar-ctheta.png"
pi0_resonance_note:        "https://userweb.jlab.org/~ungaro/pubs/pdfs/pi0.pdf"

---

<br/>

# Single meson electro-production at high {{ site.q2 }} with CLAS

<br/>

---

<br/>


# [{{ site.pi0 }} electro-production at high {{ site.q2 }} in the first and second resonance region](pi0_resonance/pi0_resonance)

We report the analysis of exclusive single {{ site.pi0 }} electro-production in the first and second resonance regions at Jefferson Lab in the {{ site.q2 }} range 2.15 {{ site.rarr }} 6 {{ site.gev2 }}. <br/>
{{ site.pi0 }} angular distributions are obtained over the entire 4{{ site.pi }} center of mass solid angle. 
The c.m. differential cross sections are measured.<br/>

|:--------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
|     [Current analysis note]( {{page.pi0_resonance_note}} )     |                                      Main Result                                      |
| :------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
|                   The LPT structure function                   |          [![gemc][lpt_structure_functionImg]]( pi0_resonance/pi0_resonance )          |
| :------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |


<br/>

---

<br/>

#  [ {{ site.pi0 }} electro-production at high {{ site.q2 }} in the {{ site.deltaM }} resonance region](pi0_delta/pi0_delta)

We report the analysis of exclusive single {{ site.pi0 }} electro-production in the {{ site.deltaM }} resonance region at Jefferson Lab in the {{ site.q2 }} range 2.4 {{ site.rarr }} 6 {{ site.gev2 }}.<br/>
{{ site.pi0 }} c.m. angular distributions are obtained over the entire 4{{site.pi}} c.m. solid angle and the c.m. differential cross section is measured.<br/>
The {{ site.gms }} form factor and multipoles ratios {{ site.rem }} = {{ site.e1p }} / {{ site.m1p }} and {{ site.rsm }} = {{ site.s1p }} / {{ site.m1p }}  for the {{ site.deltaM }} resonance production are extracted using both a truncated multipoles analysis and the JANR unitary isobar model. 

|:-------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
|           [PRL Paper](https://inspirehep.net/literature/719584)           |                          Main Result                                                  |
|      :------------------------------------------------------------:       | :-----------------------------------------------------------------------------------: |
|    {{ page.d1 }} {{ page.d2 }} {{ page.d3 }} {{ page.d4 }}                |                 [![gemc][multipoles_ratiosImg]](pi0_delta/pi0_delta)                  |
|      :------------------------------------------------------------:       | :-----------------------------------------------------------------------------------: |





<br/>

---

<br/>


[lpt_structure_functionImg]: {{ page.lpt_structure_functionImg }}
[multipoles_ratiosImg]:  {{ page.multipoles_ratiosImg }}
