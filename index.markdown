---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# See https://github.com/jekyll/minima#readme

# Table: add first row (3 |) for autoformatting

layout: default

interest: |
  
  - ▸ Quark Structure
  - ▸ MonteCarlo Simulations
  - ▸ Large Language Models
  - ▸ Data Analysis
  - ▸ Geant4
  - ▸ Cherenkov Counters
  - ▸ Software Development

education: |
  - <span class="large-emoji">🔬</span> **Staff Scientist**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Jefferson Laboratory](https://www.jlab.org), VA, USA, 2011-present <br/><br/>

  - <span class="large-emoji">🎓 🔬</span>  **Post-Doc and Research Associate**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[University of Connecticut](https://uconn.edu), USA, 2004-2011 <br/><br/>

  - <span class="large-emoji">🎓</span>  **PhD in Nuclear Physics**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Rensselaer Polytechnic Institute](https://www.rpi.edu), Troy, NY, USA, 2003 <br/><br/>

  - <span class="large-emoji">🎓</span>  **Laurea in Fisica**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Università degli studi di Genova](https://www.difi.unige.it/it), Italy, 1999 <br/><br/>

p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"


---


{% assign gscholar_img = '/assets/images/home/gscholar.png' | relative_url %}
{% assign gscholar_link = 'https://scholar.google.com/citations?user=zkWYILYAAAAJ&hl=en' %}
{% assign github_img = '/assets/images/home/github.png' | relative_url %}
{% assign github_link = 'https://github.com/maureeungaro' %}
{% assign inspire_img = '/assets/images/home/inspire.png' | relative_url %}
{% assign inspire_link = 'https://inspirehep.net/authors/1322331' %}
{% assign email_img = '/assets/images/home/email.png' | relative_url %}
{% assign email_link = 'mailto:ungaro@jlab.org' %}
{% assign physics_img = '/assets/images/home/physics.png' | relative_url %}
{% assign degree_img = '/assets/images/home/degree.png' | relative_url %}

{% capture left %}

{% include figure.html
src="assets/images/home/mauri.png"
alt="Database-driven architecture"
width="170"
%}

<div style="text-align: center">
<h2>Maurizio Ungaro</h2> 
</div>

|                     `Staff Scientist`                      |
|:----------------------------------------------------------:|
|        [Jefferson Laboratory](https://www.jlab.org)        |
|:----------------------------------------------------------:|
| [Experimental Hall-B](https://www.jlab.org/physics/hall-b) |

|--------------------------------------------|--------------------------------------|-----------------------------------------|-----------------------------------|
| [![gscholar][gscholar-img]][gscholar-link] | [![github][github-img]][github-link] | [![inspire][inspire-img]][inspire-link] | [![email][email-img]][email-link] |

[gscholar-img]: {{ gscholar_img }}
[gscholar-link]: {{ gscholar_link }}
[github-img]: {{ github_img }}
[github-link]: {{ github_link }}
[inspire-img]: {{ inspire_img }}
[inspire-link]: {{ inspire_link }}
[email-img]: {{ email_img }}
[email-link]: {{ email_link }}

{% endcapture %}

{% capture right %}

<br/>

## About Me

I’m Mauri, a physicist working in [Hall-B](https://www.jlab.org/physics/hall-b) at [Jefferson Lab](https://www.jlab.org).

My research is focused on the internal structure and dynamics of the nucleon, in particular the physics beyond the
constituent quark model and the link between form factors and dressed quark mass (see for example
the [N → Δ(1232) transition](meson/pi0_delta/pi0_delta) and the
[meson electro-production at high Q<sup>2</sup>](meson/pi0_resonance/pi0_resonance) analyses).

I work on the Refurbishment, Operation / Maintenance / Calibration of the
[Low Threshold Cherenkov Counter](https://www.jlab.org/Hall-B/clas12-web/specs/ltcc.pdf) detector in Hall-B.

I am developing the [GEMC](https://gemc.github.io/home/) Geant4 simulation framework
and the [CLAS12 Simulations](https://github.com/gemc/clas12Tags), including
[Web Submissions](https://gemc.jlab.org/web_interface/index.php) to the
[Open Science Grid (OSG)](https://osg-htc.org), see for example our
[CLAS12 Project accounting](https://gracc.opensciencegrid.org/d/000000033/osg-project-accounting?orgId=1).

Most recently I joined the [Geant4](https://geant4.web.cern.ch) collaboration with the purpose of
[supporting it at JLab](https://jeffersonlab.github.io/g4home/).

In my free time I am learning to play hockey, while enjoying watching my kid skating much faster than me.

{% endcapture %}

{% include two_col_md.html left="30%" right="70%" left_content=left right_content=right %}

<br/><br/>

{% capture left2 %}
<br/>
<br/><br/>
<br/>

## Interests

<br/>


<div class="no-bullets-list">
  {{ page.interest | markdownify }}
</div>

  {% endcapture %}


{% capture right2 %}

## Education

<br/>


<div class="no-bullets-list">
  {{ page.education | markdownify }}
</div>
{% endcapture %}

{% include two_col_md.html left="40%" right="60%" left_content=left2 right_content=right2 %}

<br/>

<br/>

## Recent and Upcoming Work/Talks

<br/>

<table class="alternate">

	<tr>
		<td> Title </td>
		<td> pdf </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	

	{% for presentation in site.data.recent_and_upcoming_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> pdf </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> pdf </a> </td>
                 {% else %}
                    <td>  </td>
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

<br/>

## Skills

<table style="text-align:center;">
<tr>
    <th style="width: 35%"><img src="assets/images/home/code.png" alt="code"/>      <br/>Programming</th>
    <th></th>
    <th style="width: 25%"><img src="assets/images/home/software.png"/>  <br/>Software</th>
    <th></th>
    <th style="width: 25%"><img src="assets/images/home/languages.png"/> <br/>Languages</th>
</tr>
<tr>
    <td><p style="font-family: Monaco">C++, [z][ba][c]sh, Python, LaTex, Git, Github, Continuous Integration, Docker, Environment-modules, HTCondor, meson, cmake, scons, fortran, PHP, Javascript, Highchart, html, CSS, Markdown</p></td>
    <td></td>
    <td><p style="font-family: Monaco"> Geant4, ROOT, XCode, PyCharm, CLion, FreeCad, Gimp, Excel, Powerpoint, Keynote, Numbers  </p></td>
    <td></td>
    <td><p style="font-family: Monaco">English, Italian</p></td>
</tr>
</table>


<br/>

## Latest News

<br/>

<div >
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


<br/>

## Galleria

<link type="text/css" rel="stylesheet" href="/home/assets/lightslider.css" />
<script src="/home/assets/jq.js"></script>
<script src="/home/assets/lightslider.js"></script>

<div>
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


<br/><br/><br/>

{:.zebra}

| Home Page Deployment | [![CI][CI-badge]][CI]  |


[CI]: https://github.com/maureeungaro/home/actions/workflows/jekyll.yml
[CI-badge]: https://github.com/maureeungaro/home/actions/workflows/jekyll.yml/badge.svg


<br/><br/><br/>

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


[code]: assets/images/home/code.png

[software]: assets/images/home/software.png

[languages]: assets/images/home/languages.png

[quote1]: assets/images/home/quote1.png






