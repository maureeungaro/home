---
# Table: add first row (3 |) for autoformatting
layout: default
title: "Meson Physics"

d1: "<h1> Main Result</h1> <br/>
The ratios R<sub>EM</sub> (upper panel) and R<sub>SM</sub> (lower panel). <br/>
The filled red squares are from the current CLAS <br/>
experiment utilizing the UIM.  <br/>
The errors shown are statistical, while  estimated  <br/>
systematic errors are shown as gray bars at the <br/>
bottom of the graph. <br/>
Also shown are selected earlier published results. <br/>
The filled triangles correspond to a recent analysis  <br/>
of previous CLAS data and the filled circles are   <br/>
from an earlier ]Lab Hall C experiment.

<br/><br/>

<h2> Bottom Line</h2> 
R<sub>EM</sub>  is small and negative, while  R<sub>SM</sub> remains negative and increases in magnitude.
These results confirm the absence of pQCD scaling at these kinematics and suggest large helicity non-conservation.

<br/><br/>

<h2> ELI5</h2> 

At these energies, we cannot use pQCD to describe the &Delta;(1232) resonance: the contributions
from quark and gluons interactions is just too strong, and unknown!<br/>
"


ratios: "<br/><a href=\"pi0_delta/pi0_delta\"><img src=\"../assets/images/pi0/multipoles_ratios.png\"
border=\"0px\" /></a><br/> "

pi0_resonance_current_status: "
This analysis was resumed in 2022.  <br/>
Currently I'm in the process of refining <br/>
the data reduction cuts, update the ROOT macros <br/>
to the latest version of ROOT, and write <br/> 
the analysis note. <br/><br/>

Completed parts, included in the analysis note: <br/>
<i>(d=done updating, p=done previously and processing update)</i><br/><br/>

<ul>
<li> [d] electron, proton identification</li>
<li> [d] vertex corrections</li>
<li> [d] electron fiducial cuts</li>
<li> [d] proton fiducial cuts</li>
<li> [d] Kinematic corrections</li>
<li> [p] Pi0 identification</li>
</ul>

On the right is a picture of the π0 missing mass versus ϕ distribution before and after the kinematic corrections for sector 1 . <br/><br/>

Upcoming:<br/> 
<i>(y=done previously, n=not done)</i><br/><br/>

<ul>
<li> [y] Acceptance correction</li>
<li> [y] Phi fits</li>
<li> [y] Structure Functions Extraction</li>
</ul>
 
"

status_image: "<br/><a href=\"pi0_resonance/pi0_resonance\"><img src=\"https://userweb.jlab.org/~ungaro/plots/e_kin_cor/img/dist-pi0vsPhi_sector-1.png\"
border=\"0px\"  /></a><br/> "


---

<br/>

# Single meson electro-production at high {{ site.q2 }} with CLAS

<br/>

---

<br/>


# [{{ site.pi0 }} electro-production at high {{ site.q2 }} in the first and second resonance region](pi0_resonance/pi0_resonance)



<br/>
<table class="alternate">
		<tr>
            <td style="width: 50%"> {{ page.pi0_resonance_current_status }} </td>
            <td> {{ page.status_image }} </td>
        </tr>

</table>
<br/><br/><br/>

---

<br/>

<div class="colored_band">

<br/><br/>

<h1><a href="pi0_delta/pi0_delta">{{ site.pi0 }} electro-production at high {{ site.q2 }} in the {{ site.deltaM }} resonance region</a></h1>





<br/><br/>
<table class="alternate">
		<tr>
            <td  style="width: 50%; padding: 8%;"> {{ page.d1 }} </td>
            <td> {{ page.ratios }} </td>
        </tr>

</table>
<br/><br/><br/>

</div>

<br/>

---



