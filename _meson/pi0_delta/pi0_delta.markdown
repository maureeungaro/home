---
layout: default

c1:  "The Form Factor G<sub>M</sub><sup>*</sup>/3G<sub>D</sub>."
c2:  "The filled red squares are from the current CLAS experiment utilizing the Unitary Isobar Model (UIM). "
c3:  "The errors shown are statistical, while estimated systematic errors are shown as gray bars at "
c4:  "the bottom of the graph. Also shown are selected earlier published results. "
c5:  "The filled triangles correspond to a recent analysis of previous CLAS data and the filled circles arefrom an earlier JLab Hall C experiment."


d1: "The ratios R<sub>EM</sub> (upper panel) and R<sub>SM</sub> (lower panel). The filled red squares are from the current CLAS experiment"
d2: "utilizing the UIM. The errors shown are statistical, while estimated systematic"
d3: "errors are shown as gray bars at the bottom of the graph. Also shown are selected earlier published results. "
d4: "The filled triangles correspond to a recent analysis of previous CLAS data and the filled circles are from an earlier ]Lab Hall C experiment."


gmstarImg:            "../../assets/images/pi0/gmstar.png"
multipoles_ratiosImg: "../../assets/images/pi0/multipoles_ratios.png"
pdfPaperLink:         "https://userweb.jlab.org/~ungaro/pubs/pdfs/e1_prl.pdf"
archiveLink:          "http://arxiv.org/pdf/hep-ex/0606042"
anoteLink:            "https://userweb.jlab.org/~ungaro/pubs/pdfs/pi0_delta.pdf"
---

## [ &#8673; Single meson electro-production at high {{ site.q2 }} with CLAS ](../meson)

# Single {{ site.pi0 }} electro-production at high {{ site.q2 }} in the Delta resonance region

<br/>

---

<br/>

We report the analysis of exclusive single {{ site.pi0 }} electro-production in the {{ site.deltaM }} resonance region at Jefferson Lab in the {{ site.q2 }} range 2.4 {{ site.rarr }} 6 {{ site.gev2 }}.<br/>
{{ site.pi0 }} c.m. angular distributions are obtained over the entire 4{{site.pi}} c.m. solid angle and the c.m. differential cross section is measured.<br/>
The {{ site.gms }} form factor and multipoles ratios {{ site.rem }} = {{ site.e1p }} / {{ site.m1p }} and {{ site.rsm }} = {{ site.s1p }} / {{ site.m1p }}  for the {{ site.deltaM }} resonance production are extracted using both a truncated multipoles analysis and the JANR unitary isobar model. 

<br/>

---

<br/>


| Documents                                                                     |
|-------------------------------------------------------------------------------|
| PRL Paper [(pdf)]({{page.pdfPaperLink}}) [(arxiv)]({{page.archiveLink}})      |
| [Analysis Note]({{page.anoteLink}})                                           |
| ----------------------------------------------------------------------------- |



| Distributions                                                          | 
|------------------------------------------------------------------------|
| [Experimental Cross Sections](distributions/cross_sections)            | 
| [Theoretical Cross Sections](distributions/theo_cross_sections)        | 
| ---------------------------------------------------------------------- | 



<br/>

---

<br/>

### Main Results:

|                                                                        |                                                                                 |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [![pi0][gmstarImg]]({{page.gmstarImg}})                                | [![gemc][multipoles_ratiosImg]]({{page.multipoles_ratiosImg}})                  |
| {{ page.c1 }} {{ page.c2 }} {{ page.c3 }} {{ page.c4 }} {{ page.c5 }}  | {{ page.d1 }} {{ page.d2 }} {{ page.d3 }} {{ page.d4 }}                         |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------- |


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


