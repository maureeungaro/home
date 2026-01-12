---
layout: default

c1:  "{::nomarkdown}The Form Factor G<sub>M</sub><sup>*</sup>/3G<sub>D</sub>.
The filled red squares are from the current CLAS experiment utilizing the Unitary Isobar Model (UIM). 
The errors shown are statistical, while estimated systematic errors are shown as gray bars at 
the bottom of the graph. Also shown are selected earlier published results. 
The filled triangles correspond to a recent analysis of previous CLAS data and the filled circles 
are from an earlier JLab Hall C experiment.<br/><br/>
<h2> Bottom Line</h2> 
The magnetic form factor G<sub>M</sub><sup>*</sup> decreases with Q2 faster than the elastic magnetic form factor.<br/><br/>
<h2> ELI5</h2> 
In general particles sizes decrease as the probe energy increase, typically like the proton. 
For some unknown reason, the &Delta;(1232) resonance size becomes smaller a lot faster.<br/>
{:/}
"


d1: "{::nomarkdown}The ratios R<sub>EM</sub> (upper panel) and R<sub>SM</sub> (lower panel). The filled red squares are from the current CLAS experiment
utilizing the UIM. The errors shown are statistical, while estimated systematic
errors are shown as gray bars at the bottom of the graph. Also shown are selected earlier published results. 
The filled triangles correspond to a recent analysis of previous CLAS data and the filled circles are from an earlier ]Lab Hall C experiment.<br/><br/>
<h2> Bottom Line</h2> 
R<sub>EM</sub>  is small and negative, while  R<sub>SM</sub> remains negative and increases in magnitude.
These results confirm the absence of pQCD scaling at these kinematics and suggest large helicity non-conservation.<br/><br/>
<h2> ELI5</h2> 
At these energies, we cannot use pQCD to describe the &Delta;(1232) resonance: the contributions
from quark and gluons interactions is just too strong, and unknown.<br/>
{:/}
"


gmstarImg:            "../../assets/images/pi0/gmstar.png"
multipoles_ratiosImg: "../../assets/images/pi0/multipoles_ratios.png"
inspireLink:         "https://inspirehep.net/literature/719584"
archiveLink:          "http://arxiv.org/pdf/hep-ex/0606042"
anoteLink:            "https://userweb.jlab.org/~ungaro/pubs/pdfs/pi0_delta.pdf"
---

## [ &#8673; Single meson electro-production at high {{ site.q2 }} with CLAS ](../meson)

# Single {{ site.pi0 }} electro-production at high {{ site.q2 }} in the Delta resonance region

<br/>

---

<br/>


We report the analysis of exclusive single {{ site.pi0 }} electro-production in the {{ site.deltaM }} 
resonance region at Jefferson Lab in the {{ site.q2 }} range 2.4 {{ site.rarr }} 6 {{ site.gev2 }}.
{{ site.pi0 }} c.m. angular distributions are obtained over the entire 4{{site.pi}} c.m. 
solid angle and the c.m. differential cross section is measured.<br/>
The {{ site.gms }} form factor and multipoles ratios  {{ site.rem }} = {{ site.e1p }} / {{ site.m1p }} and {{ site.rsm }} = {{ site.s1p }} / {{ site.m1p }} for 
the {{ site.deltaM }} resonance production are extracted using both a truncated multipoles 
analysis and the JANR unitary isobar model. 

<br/>

<table class="alternate">
<tr> 
<td style="width: 50%;"> PRL Paper <a href="https://inspirehep.net/literature/719584">(inSPIRE)</a>  <a href="https://arxiv.org/pdf/hep-ex/0606042.pdf">(arxiv pdf)</a></td>
<td> <a href="https://userweb.jlab.org/~ungaro/pubs/pdfs/pi0_delta.pdf">Analysis Note (May 2009)</a> </td>
</tr>
</table>

<br/>



<br/><br/>

<h2> Cross Sections, Structure Functions and Legendre Coefficients Distributions </h2>

<table class="alternate">
<tr> 
<td style="width: 50%;"> <a href="distributions/cross_sections">Experimental Cross Sections</a> </td>
<td> <a href="distributions/theo_cross_sections">Theoretical Cross Sections</a> </td>
</tr>
<tr> 
<td> <a href="distributions/structure_functions">Structure Functions</a> </td>
<td> <a href="distributions/legendre_coefficients">Legendre Coefficients</a> </td>
</tr>
<tr> 
<td> <a href="distributions/multipoles">Multipoles</a> </td>
<td> </td>
</tr>
</table>


<br/><br/><br/>


<br/>
---

<br/>

# Main Results:

With high enough energy we expected to 'see' past the mesons / gluons cloud and be able to probe directly the quarks in 
the {{ site.deltaM }} resonance. This is clearly not the case at these energy: the meson/gluon contribution
is still too strong, and unknown.<br/>


|                                                                        |     |                                                                                |
|:-----------------------------------------------------------------------|-----| ---------------------------------------------------------------------------------|
| [![pi0][gmstarImg]]({{page.gmstarImg}})                                |     | [![gemc][multipoles_ratiosImg]]({{page.multipoles_ratiosImg}})                  |
| {{ page.c1 }}                                                          |     | {{ page.d1 }}                          |
| ---------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------- |





<br/>

---


<br/>


## Related theoretical models


<br/>

___

<br/>


## Related publications

<table class="alternate">
	{% for paper in site.data.pi0_delta_related_publications %}
		<tr>
            <td> {{ paper.author }} </td>
            <td> <a href="{{ paper.link }}"> {{ paper.title }}</a> </td>
        </tr>
	{% endfor %}
</table>

[gmstarImg]: {{ page.gmstarImg }}
[multipoles_ratiosImg]: {{ page.multipoles_ratiosImg }}


