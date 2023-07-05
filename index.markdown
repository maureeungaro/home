---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# See https://github.com/jekyll/minima#readme

# Table: add first row (3 |) for autoformatting

layout: default

mauri: "
<img src=\"assets/images/home/mauri.png\"/><br/><br/>
<span style=\"color:#222222;font-weight:200;font-size:32px\"><center>Maurizio Ungaro</center></span><span style=\"color:#888888;font-weight:200;font-size:26px\">Staff Scientist</span><br/>
[Jefferson Laboratory](https://www.jlab.org) <br/>[Experimental Hall-B](https://www.jlab.org/physics/hall-b)<br/><br/>
<a href=\"https://scholar.google.com/citations?user=zkWYILYAAAAJ&hl=en\" target=_blank><img class=\"zoomIcon\" src=\"assets/images/home/gscholar.png\"/> </a> &nbsp;
<a href=\"https://github.com/maureeungaro\"                              target=_blank><img class=\"zoomIcon\" src=\"assets/images/home/github.png\"/>   </a> &nbsp;
<a href=\"https://inspirehep.net/authors/1322331\"                       target=_blank><img class=\"zoomIcon\" src=\"assets/images/home/inspire.png\"/>  </a>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>"

abtme: "<span style=\"color:#222222;font-weight:500;font-size:2.5rem; font-family: Montserrat,sans-serif; \">About Me</span> <br/>"

hello: "<br/>I'm Mauri, a physicist working in [Hall-B](https://www.jlab.org/physics/hall-b) at [Jefferson Lab](https://www.jlab.org).<br/><br/>
My research is focused on the internal structure and dynamics of the nucleon, <br/>
in particular the physics beyond the constituent quark model and the link between <br/>
form factors and dressed quark mass (see for example the [N → Δ(1232) transition](meson/pi0_delta/pi0_delta)<br/>
and the [meson electro-production at high Q<sup>2</sup>](meson/meson) analyses). <br/><br/>
I worked on the Refurbishment, Operation / Maintenance / Calibration of the<br/> 
[Low Threshold Cherenkov Counter](https://www.jlab.org/Hall-B/clas12-web/specs/ltcc.pdf) detector in Hall-B. <br/><br/>
I also work on the [GEMC](https://gemc.github.io/home/)  simulation framework and the<br/>
[CLAS12 Geant4 simulations](https://github.com/gemc/clas12Tags), including large [submissions](https://gemc.jlab.org/web_interface/index.php) to the<br/>
[Open Science Grid (OSG)](https://gracc.opensciencegrid.org/d/000000033/osg-project-accounting?orgId=1).<br/><br/>
Most recently I joined the [Geant4](https://geant4.web.cern.ch) collaboration with the purpose of supporting <br/>
its development.<br/><br/>"




interest: "{::nomarkdown}
<table>
<tr>
<th>Interests</th>   
<th>Education</th>
</tr>
<tr>
<td>
<ul>
<li> Quark Structure</li>
<li> MonteCarlo Simulations</li>
<li> Data Analysis</li>
<li> Geant4</li>
<li> Cherenkov Counters</li>
<li> Software Development<br/><br/><br/><br/><br/><br/></li>
</ul>
</td>
<td>
<img src=\"assets/images/home/physics.png\" width=30px/> Staff Scientist<br/>
<span style=\"color:#888888;font-weight:300;font-size:18px\">Jefferson Laboratory, VA, USA, 2011-present</span><br/><br/>
<img src=\"assets/images/home/degree.png\" width=30px/> <img src=\"assets/images/home/physics.png\" width=30px/> Post-Doc and Research Associate<br/>
<span style=\"color:#888888;font-weight:300;font-size:18px\">University of Connecticut, USA, 2004-2011</span><br/><br/>
<img src=\"assets/images/home/degree.png\" width=30px/> PhD in Nuclear Physics     <br/>
<span style=\"color:#888888;font-weight:300;font-size:18px\">Rensselaer Polytechnic Institute, Troy, NY, USA, 2003</span><br/><br/>
<img src=\"assets/images/home/degree.png\" width=30px/> Laurea in Fisica <br/>
<span style=\"color:#888888;font-weight:300;font-size:18px\">Università degli studi di Genova, Italy, 1999</span><br/>
</td>
</tr>
</table>{:/}
"

---

|                                                      |                                                       |
|:----------------------------------------------------:|-------------------------------------------------------|
|                    {{page.mauri}}                    | {{page.abtme}} {{page.hello}}     {{page.interest}}   |
| ---------------------------------------------------- | ----------------------------------------------------- |

<div class="colored_band">

<br/><br/><br/>

<span style="color:#444;font-weight:400;font-size:38px">Recent and Upcoming talks</span>
<br/><br/><br/>
<table class="alternate">
	{% for presentation in site.data.recent_and_upcoming_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> pdf </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> pdf </a> </td>
                 {% else %}
                    <td> na </td>
                {% endif %}

                {% if presentation.key == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.key"  target="_blank"> key </a> </td>
                {% else %}
                    <td> na </td>
                {% endif %}

                {% if presentation.pptx == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pptx" target="_blank"> ppt </a> </td>
                {% else %}
                    <td> na </td>
                {% endif %}

                 {% if presentation.occasion_url == "NA" %}
                    <td>{{presentation.occasion}} </td>
                {% else %}
                     <td> <a href="{{ presentation.occasion_url }}"  target="_blank"> {{presentation.occasion}} </a> </td>
                {% endif %}

            <td> {{presentation.date}} </td>

        </tr>
	{% endfor %}
</table>
<br/><br/><br/>

</div>


[mauri]: assets/images/home/mauri.png

[gscholar]: assets/images/home/google-scholar.png

[github]: assets/images/home/github.png

[inspire]: assets/images/home/inspire.png

[degree]: assets/images/home/degree.png
