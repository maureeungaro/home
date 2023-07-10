---
# Table: add first row (3 |) for autoformatting
layout: default
title: "Meson Physics"

c1:  "<br/><a href=\"pi0_resonance/pi0_resonance\"><img src=\"../assets/images/pi0/gmstar.png\"
border=\"0px\" width=\"650px\" height=\"650px\"/></a><br/> 
The Form Factor G<sub>M</sub><sup>*</sup>/3G<sub>D</sub>.<br/>
The filled red squares are from the current CLAS experiment utilizing the Unitary <br/>
Isobar Model (UIM).  The errors shown are statistical, while estimated systematic <br/>
errors are shown as gray bars at  the bottom of the graph. Also shown are selected <br/> 
earlier published results. The filled triangles correspond to a recent analysis of <br/>
previous CLAS data and the filled circles arefrom an earlier JLab Hall C experiment."



d1: "<h1> Main Results</h1> <br/>
The ratios R<sub>EM</sub> (upper panel) and R<sub>SM</sub> (lower panel). <br/>
The filled red squares are from the current CLAS <br/>
experiment utilizing the UIM.  <br/>
The errors shown are statistical, while  estimated  <br/>
systematic errors are shown as gray bars at the <br/>
bottom of the graph. <br/>
Also shown are selected earlier published results. <br/>
The filled triangles correspond to a recent analysis  <br/>
of previous CLAS data and the filled circles are   <br/>
from an earlier ]Lab Hall C experiment."




multipoles_ratiosImg:      "../assets/images/pi0/multipoles_ratios.png"
lpt_structure_functionImg: "../assets/images/pi0/q2-3.00_sf-LPT_runningvar-ctheta.png"


ratios: "<br/><a href=\"pi0_resonance/pi0_resonance\"><img src=\"../assets/images/pi0/multipoles_ratios.png\"
border=\"0px\" width=\"750px\" height=\"950px\"/></a><br/> "

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


<table class="alternate">
<tr> 
<td> <a href="https://userweb.jlab.org/~ungaro/pubs/pdfs/pi0.pdf">Current Analysis Note</a> </td>
</tr>
</table>

|                                  |                                                                                       |
|:--------------------------------:|:-------------------------------------------------------------------------------------:|
|    The LPT structure function    |          [![gemc][lpt_structure_functionImg]]( pi0_resonance/pi0_resonance )          |
| :------------------------------: | :-----------------------------------------------------------------------------------: |


<br/><br/>

---

<br/>

<div class="colored_band">

<br/><br/>

<h1><a href="pi0_delta/pi0_delta">{{ site.pi0 }} electro-production at high {{ site.q2 }} in the {{ site.deltaM }} resonance region</a></h1>


We report the analysis of exclusive single {{ site.pi0 }} electro-production in the {{ site.deltaM }} 
resonance region at Jefferson Lab in the {{ site.q2 }} range 2.4 {{ site.rarr }} 6 {{ site.gev2 }}.<br/>
{{ site.pi0 }} c.m. angular distributions are obtained over the entire 4{{site.pi}} c.m. 
solid angle and the c.m. differential cross section is measured.<br/>
The {{ site.gms }} form factor and multipoles ratios 
{{ site.rem }} = {{ site.e1p }} / {{ site.m1p }} and {{ site.rsm }} = {{ site.s1p }} / {{ site.m1p }}  
for the {{ site.deltaM }} resonance production are extracted using both a truncated multipoles 
analysis and the JANR unitary isobar model. 

<br/><br/>

<table class="alternate">
<tr> 
<td> PRL Paper <a href="https://inspirehep.net/literature/719584">(inSPIRE)</a>  <a href="https://arxiv.org/pdf/hep-ex/0606042.pdf">(arxiv pdf)</a></td>
<td> <a href="https://userweb.jlab.org/~ungaro/pubs/pdfs/pi0_delta.pdf">Analysis Note</a> </td>
</tr>
</table>

<br/><br/>
<table class="alternate">
		<tr>
            <td> {{ page.d1 }} </td>
            <td> {{ page.ratios }} </td>
        </tr>

</table>
<br/><br/><br/>

</div>

<br/>

---






[lpt_structure_functionImg]: {{ page.lpt_structure_functionImg }}
[multipoles_ratiosImg]:  {{ page.multipoles_ratiosImg }}
