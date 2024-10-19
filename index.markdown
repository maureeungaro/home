---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# See https://github.com/jekyll/minima#readme

# Table: add first row (3 |) for autoformatting

layout: default

mauri: "
<img src=\"assets/images/home/mauri.png\" style=\"width: 60%\"/><br/><br/>
<span style=\"color:#222222;font-weight:200;font-size:30px\"><center>Maurizio Ungaro</center></span><span style=\"color:#888888;font-weight:200;font-size:24px\">Staff Scientist</span><br/><br/>
[Jefferson Laboratory](https://www.jlab.org) <br/>[Experimental Hall-B](https://www.jlab.org/physics/hall-b)<br/><br/>
<a href=\"https://scholar.google.com/citations?user=zkWYILYAAAAJ&hl=en\" target=_blank><img class=\"zoomIcon\" src=\"assets/images/home/gscholar.png\"/> </a> 
<a href=\"https://github.com/maureeungaro\"                              target=_blank><img class=\"zoomIcon\" src=\"assets/images/home/github.png\"  /> </a> 
<a href=\"https://inspirehep.net/authors/1322331\"                       target=_blank><img class=\"zoomIcon\" src=\"assets/images/home/inspire.png\" /> </a> 
<a href=\"mailto:ungaro@jlab.org\"                                                    ><img class=\"zoomIcon\" src=\"assets/images/home/email.png\"   /> </a>
<br/><br/><br/><br/><br/>"

abtme: "<span style=\"color:#222222;font-weight:500;font-size:2.5rem; font-family: Montserrat,sans-serif; \">About Me</span> <br/>"

hello: "<br/>I'm Mauri, a physicist working in [Hall-B](https://www.jlab.org/physics/hall-b) at [Jefferson Lab](https://www.jlab.org).<br/><br/>
My research is focused on the internal structure and dynamics of the nucleon, <br/>
in particular the physics beyond the constituent quark model and the link between <br/>
form factors and dressed quark mass (see for example the [N → Δ(1232) transition](meson/pi0_delta/pi0_delta)<br/>
and the [meson electro-production at high Q<sup>2</sup>](meson/pi0_resonance/pi0_resonance) analyses). <br/><br/>
I work on the Refurbishment, Operation / Maintenance / Calibration of the<br/> 
[Low Threshold Cherenkov Counter](https://www.jlab.org/Hall-B/clas12-web/specs/ltcc.pdf) detector in Hall-B. <br/><br/>
I am developing the [GEMC](gemc/gemc)  simulation framework and the [CLAS12 simulations](clas12Tags/clas12Tags),  <br/>
including [web submissions](osg/osg) to the [Open Science Grid (OSG)](https://gracc.opensciencegrid.org/d/000000033/osg-project-accounting?orgId=1).<br/><br/>
Most recently I joined the [Geant4](https://geant4.web.cern.ch) collaboration with the purpose of 
[supporting it at JLab](https://jeffersonlab.github.io/g4home/).<br/><br/>
In my free time I am learning to play hockey, while watching and [assisting](showcase/hockey)<br/>
 my kid learning it much faster than me.
<br/><br/>"




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
<span style=\"color:#888888;font-weight:300;font-size:18px\"><a style=\"color:#448844;\" href=\"https://www.jlab.org\">Jefferson Laboratory</a>, VA, USA, 2011-present</span><br/><br/>
<img src=\"assets/images/home/degree.png\" width=30px/> <img src=\"assets/images/home/physics.png\" width=30px/> Post-Doc and Research Associate<br/>
<span style=\"color:#888888;font-weight:300;font-size:18px\"><a style=\"color:#448844;\" href=\"https://www.uconn.edu\">University of Connecticut</a>, USA, 2004-2011</span><br/><br/>
<img src=\"assets/images/home/degree.png\" width=30px/> PhD in Nuclear Physics     <br/>
<span style=\"color:#888888;font-weight:300;font-size:18px\"><a style=\"color:#448844;\" href=\"https://www.rpi.edu\">Rensselaer Polytechnic Institute</a>, Troy, NY, USA, 2003</span><br/><br/>
<img src=\"assets/images/home/degree.png\" width=30px/> Laurea in Fisica <br/>
<span style=\"color:#888888;font-weight:300;font-size:18px\"><a style=\"color:#448844;\" href=\"https://www.difi.unige.it/it\">Università degli studi di Genova</a>, Italy, 1999</span><br/>
</td>
</tr>
</table>{:/}
"

p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"

---

|                                                      |                                                       |
|:----------------------------------------------------:|-------------------------------------------------------|
|                    {{page.mauri}}                    | {{page.abtme}} {{page.hello}}     {{page.interest}}   |
| ---------------------------------------------------- | ----------------------------------------------------- |

<div class="colored_band">

<br/><br/><br/>

<p style="text-align:center">
<span style="color:#444;font-weight:300;font-size:54px">Recent and Upcoming talks</span>
</p>
<br/><br/>
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


<br/><br/>

<p style="text-align:center"><span style="color:#444;font-weight:300;font-size:54px;">Skills</span></p>    
<br/>


<table style="text-align:center;">
<tr>
    <th style="width: 25%"><img src="assets/images/home/code.png" alt="code"/>      <br/>Programming</th>
    <th></th>
    <th style="width: 25%"><img src="assets/images/home/software.png"/>  <br/>Software</th>
    <th></th>
    <th style="width: 25%"><img src="assets/images/home/languages.png"/> <br/>Languages</th>
</tr>
<tr>
    <td><p style="color:#333;font-weight:400;font-size:16px; font-family: Monaco">C++, [z][ba][c]sh, Python, LaTex, Git, Github CI, Docker, Environment-modules, HTCondor, CMake, SCons, Fortran, PHP, Javascript, Highchart, Html, CSS, Markdown</p></td>
    <td></td>
    <td><p style="color:#333;font-weight:400;font-size:18px; font-family: Avenir"> Geant4, ROOT, XCode, PyCharm, CLion, FreeCad, Gimp, Excel, Powerpoint, Keynote, Numbers  </p></td>
    <td></td>
    <td><p style="color:#333;font-weight:400;font-size:16px">English, Italian</p></td>
</tr>
</table>
<br/>


<div class="colored_band">
	<br/>
	<p style="text-align:center"><span style="color:#444;font-weight:300;font-size:54px;">Latest News</span></p>    
	<br/><br/>
	<table class="alternate">
	{% for news in site.data.news %}
		<tr>
			<td> <a href="{{news.link}}"><img src="{{news.image}}" width="100px">&nbsp;&nbsp;&nbsp;{{news.title}}</a> </td>
			<td> {{news.date}} </td>
		</tr>
	{% endfor %}
	</table>
	<br/><br/>
</div>



<link type="text/css" rel="stylesheet" href="/home/assets/lightslider.css" />
<script src="/home/assets/jq.js"></script>
<script src="/home/assets/lightslider.js"></script>

<div>
	<br/><br/><br/>
	<p style="text-align:center"><span style="color:#444;font-weight:300;font-size:54px;">Galleria</span></p>    
	<br/>

	<ul style="text-align:center"  id="light-slider" >
    	<li data-thumb="assets/images/empty.png">
			<img src="assets/images/home/quote1.png" height="500px" width="90%"/><br/><br/><br/>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/software/charts">Chart CSV displayer<br/><img src="assets/images/software/charts_big.png" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/meson/pi0_delta/pi0_delta">N → Δ(1232) transition <br/><img src="assets/images/pi0/pi0_delta_results.png" height="500px" width="90%"/></a>
    	</li>
	</ul>

</div>

<script type="text/javascript">
    $(document).ready(function() {
            $('#light-slider').lightSlider({
                gallery:true,
                item:1,
                thumbItem:2,
                slideMargin: 1,
                speed:500,
		        pause: 5000,
                auto:true,
                loop:true,
                onSliderLoad: function() {
                    $('#light-slider').removeClass('cS-hidden');
                }  
		});
});
</script>

<br/><br/><br/>
<br/><br/><br/>


[mauri]: assets/images/home/mauri.png

[gscholar]: assets/images/home/google-scholar.png

[github]: assets/images/home/github.png

[inspire]: assets/images/home/inspire.png

[degree]: assets/images/home/degree.png

[code]: assets/images/home/code.png

[software]: assets/images/home/software.png

[languages]: assets/images/home/languages.png

[quote1]: assets/images/home/quote1.png
