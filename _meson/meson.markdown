---
# Table: add first row (3 |) for autoformatting
layout: default
title: "Meson Physics"

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


ratios: "<br/><a href=\"pi0_resonance/pi0_resonance\"><img src=\"../assets/images/pi0/multipoles_ratios.png\"
border=\"0px\" width=\"650px\" /></a><br/> "

pi0_resonance_current_status: "
This analysis was resumed in 2022.  <br/>
Currently I'm in the process of refining <br/>
the data reduction cuts, update the ROOT macros <br/>
to the latest version of ROOT, and write <br/> 
the analysis note. <br/><br/>

Completed parts, included in the analysis note: <br/>
<i>(u=updated, p=done previously, processing update)</i><br/><br/>

<ul>
<li> [u] electron, proton identification</li>
<li> [u] vertex corrections</li>
<li> [u] electron fiducial cuts</li>
<li> [p] proton fiducial cuts</li>
</ul>

On the right is a picture of the electron fiducial cuts in the DC2 plane. <br/><br/>

Upcoming:<br/> 
<i>(y=done previously, n=not done)</i><br/><br/>

<ul>
<li> [y] Kinematic corrections</li>
<li> [y] Pi0 identification</li>
<li> [y] Acceptance correction</li>
<li> [y] Phi fits</li>
<li> [y] Structure Functions Extraction</li>
</ul>
 
"

status_image: "<br/><a href=\"pi0_resonance/pi0_resonance\"><img src=\"https://userweb.jlab.org/~ungaro/plots/efid/img/plane-DC2_intsector-2.png\"
border=\"0px\" width=\"750px\" /></a><br/> "


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
            <td> {{ page.pi0_resonance_current_status }} </td>
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
            <td> {{ page.d1 }} </td>
            <td> {{ page.ratios }} </td>
        </tr>

</table>
<br/><br/><br/>

</div>

<br/>

---



