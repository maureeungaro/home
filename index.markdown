---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# See https://github.com/jekyll/minima#readme

# Table: add first row (3 |) for autoformatting

layout: default
title: Maurizio Ungaro
description: >-
  Nuclear physicist and simulation software developer at Jefferson Lab working on Geant4, GEMC,
  CLAS12 detector systems, nucleon structure, and scientific computing workflows.
image: /assets/images/home/mauri.png
nav_exclude: true

interest: |
  - ▸ Quark Structure
  - ▸ Monte Carlo Simulations
  - ▸ Large Language Models
  - ▸ Data Analysis
  - ▸ Geant4
  - ▸ Cherenkov Counters
  - ▸ Software Development

education: |
  - <span class="large-emoji">🔬</span> **Staff Scientist**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Jefferson Laboratory](https://www.jlab.org), VA, USA, 2011-present <br/><br/>

  - <span class="large-emoji">🎓 🔬</span>  **Postdoctoral Researcher and Research Associate**<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[University of Connecticut](https://uconn.edu), USA, 2004-2011 <br/><br/>

  - <span class="large-emoji">🎓</span>  **Ph.D. in Nuclear Physics**<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Rensselaer Polytechnic Institute](https://www.rpi.edu), Troy, NY, USA, 2003 <br/><br/>

  - <span class="large-emoji">🎓</span>  **Laurea in Fisica**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    [Università degli Studi di Genova](https://unige.it/), Italy, 1999 <br/><br/>

p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"


---


{% assign gscholar_img = '/assets/images/home/gscholar.png' | relative_url %}
{% assign gscholar_link = 'https://scholar.google.com/citations?user=zkWYILYAAAAJ&hl=en' %}
{% assign github_img = '/assets/images/home/github.png' | relative_url %}
{% assign github_link = 'https://github.com/maureeungaro' %}
{% assign inspire_img = '/assets/images/home/inspire.png' | relative_url %}
{% assign inspire_link = 'https://inspirehep.net/authors/1322331' %}
{% assign researchgate_img = '/assets/images/home/researchgate.svg' | relative_url %}
{% assign researchgate_link = 'https://www.researchgate.net/profile/Maurizio-Ungaro' %}
{% assign scopus_img = '/assets/images/home/scopus.svg' | relative_url %}
{% assign scopus_link = 'https://www.scopus.com/authid/detail.uri?authorId=35228099400' %}
{% assign email_img = '/assets/images/home/email.png' | relative_url %}
{% assign email_link = 'mailto:ungaro@jlab.org' %}
{% assign orcid_img = '/assets/images/home/orcid.svg' | relative_url %}
{% assign orcid_link = 'https://orcid.org/0000-0001-6982-3310' %}
{% assign linkedin_img = '/assets/images/home/linkedin.svg' | relative_url %}
{% assign linkedin_link = 'https://www.linkedin.com/in/maurizio-ungaro-37992062/' %}
{% assign physics_img = '/assets/images/home/physics.png' | relative_url %}
{% assign degree_img = '/assets/images/home/degree.png' | relative_url %}

{% capture left %}

{% include figure.html
src="assets/images/home/mauri.png"
alt="Portrait of Maurizio Ungaro"
width="170"
%}

<div style="text-align: center">
<h2>Maurizio Ungaro</h2> 
<p>Nuclear physicist and simulation software developer</p>
</div>

|                      `Staff Scientist`                       |
|:------------------------------------------------------------:|
|      [Jefferson Laboratory](https://www.jlab.org)            |
|  [Experimental Hall-B](https://www.jlab.org/physics/hall-b)  |

[gscholar-img]: {{ gscholar_img }}
[gscholar-link]: {{ gscholar_link }}
[github-img]: {{ github_img }}
[github-link]: {{ github_link }}
[inspire-img]: {{ inspire_img }}
[inspire-link]: {{ inspire_link }}
[researchgate-img]: {{ researchgate_img }}
[researchgate-link]: {{ researchgate_link }}
[scopus-img]: {{ scopus_img }}
[scopus-link]: {{ scopus_link }}
[email-img]: {{ email_img }}
[email-link]: {{ email_link }}
[orcid-img]: {{ orcid_img }}
[orcid-link]: {{ orcid_link }}
[linkedin-img]: {{ linkedin_img }}
[linkedin-link]: {{ linkedin_link }}

{% endcapture %}

{% capture right %}

<br/>

## About Me

I am Maurizio (Mauri) Ungaro, a Staff Scientist in [Hall-B](https://www.jlab.org/physics/hall-b)
at [Jefferson Lab](https://www.jlab.org). I work on nuclear physics, detector systems, and simulation software.

My current work includes Geant4-based simulations with GEMC, CLAS12 production workflows on the
Open Science Grid, and operation, calibration, and performance studies of the CLAS12 Low Threshold
Cherenkov Counter. My research explores nucleon structure through meson electroproduction.

Here you can find software, talks, technical notes, and practical examples for collaborators and students.

In my free time, I am learning to play hockey while enjoying watching my kid skate much faster than me.

<br/>

<table class="zebra compact-table">
  <tr>
    <th>Primary links</th>
    <td><a href="/home/profile/">Profile</a></td>
    <td><a href="https://gemc.github.io/home/">GEMC</a></td>
    <td><a href="/home/showcase/">Research & Talks</a></td>
    <td><a href="/home/mynotes/">Notes</a></td>
  </tr>
</table>

<br/>

For collaboration or help with simulations and detector work, [email me](mailto:ungaro@jlab.org).
You can also find my publications and code through the profiles below.
<br/>
<br/>

<table class="small-icons">
  <tr>
    <td><a href="{{ gscholar_link }}"><img src="{{ gscholar_img }}" alt="Google Scholar"></a><br/><a href="{{ gscholar_link }}">Google Scholar</a></td>
    <td><a href="{{ inspire_link }}"><img src="{{ inspire_img }}" alt="INSPIRE"></a><br/><a href="{{ inspire_link }}">INSPIRE</a></td>
    <td>
      <a href="{{ scopus_link }}"><img src="{{ scopus_img }}" alt="Scopus"></a><br/>
      <a href="{{ scopus_link }}">Scopus</a>
    </td>
    <td>
      <a href="{{ researchgate_link }}"><img src="{{ researchgate_img }}" alt="ResearchGate"></a><br/>
      <a href="{{ researchgate_link }}">ResearchGate</a>
    </td>
  </tr>
  <tr>
    <td><a href="{{ github_link }}"><img src="{{ github_img }}" alt="GitHub"></a><br/><a href="{{ github_link }}">GitHub</a></td>
    <td><a href="{{ orcid_link }}"><img src="{{ orcid_img }}" alt="ORCID"></a><br/><a href="{{ orcid_link }}">ORCID</a></td>
    <td><a href="{{ linkedin_link }}"><img src="{{ linkedin_img }}" alt="LinkedIn"></a><br/><a href="{{ linkedin_link }}">LinkedIn</a></td>
    <td><a href="{{ email_link }}"><img src="{{ email_img }}" alt="Email"></a><br/><a href="{{ email_link }}">Email</a></td>
  </tr>
</table>

{% endcapture %}

{% include two_col_md.html left="30%" right="70%" left_content=left right_content=right %}

<br/><br/>

## Latest News and Upcoming Work

<table class="alternate">
  <thead>
    <tr><th scope="col">News</th><th scope="col">Date / Status</th></tr>
  </thead>
  <tbody>
    {% for news in site.data.news %}
    <tr>
      <td>
        <a href="{{ news.link }}">
          <img src="{{ news.image }}" alt="" width="100"> {{ news.title }}
        </a>
      </td>
      <td>{{ news.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

The upcoming CLAS12 note describes the simGrid OSG framework, with diagrams of its architecture
and job workflows. Until the note is available,
the news link leads to the [CLAS12 on OSG overview]({{ '/osg/osg' | relative_url }}).

<br/>

## Start Here

| If you are looking for... | Start with |
|:--|:--|
| Biography, CV, resume, or professional links | [Profile](/home/profile/) |
| Geant4 examples, tutorials, or JLab support | [Geant4 at JLab](https://jeffersonlab.github.io/g4home/) |
| GEMC simulation workflows | [GEMC](https://gemc.github.io/home/) |
| CLAS12 simulation releases | [CLAS12 Simulations](https://github.com/gemc/clas12Tags) |
| Distributed simulation production | [CLAS12 on OSG](/home/osg/osg) |
| Research talks, papers, and technical notes | [Research & Talks](/home/showcase/) |
| Practical computing notes | [Notes](/home/mynotes/) |

<br/><br/>

## What I Work On

- **Nuclear physics:** nucleon structure, resonance-region analyses, and the transition between hadronic
  and partonic descriptions, including the [N → Δ(1232) transition](/home/meson/pi0_delta/pi0_delta)
  and [meson electroproduction at high Q<sup>2</sup>](/home/meson/pi0_resonance/pi0_resonance).
- **Detector systems:** operation, maintenance, calibration, and performance studies of the
  [CLAS12 Low Threshold Cherenkov Counter](/home/ltcc/ltcc).
- **Simulation software:** development of [GEMC and GEMC3](https://gemc.github.io/home/),
  [CLAS12 simulations](https://github.com/gemc/clas12Tags), and
  [Open Science Grid production workflows](/home/osg/osg).
- **Scientific computing and support:** [Geant4 at JLab](https://jeffersonlab.github.io/g4home/),
  reproducible simulation workflows, tutorials, examples, and user-facing documentation.

<br/>

## Recent and Upcoming Talks and Notes

<br/>

<table class="alternate">

	<tr>
		<th scope="col">Title</th>
		<th scope="col">PDF</th>
		<th scope="col">Occasion</th>
		<th scope="col">Date</th>
	</tr>	

	{% for presentation in site.data.recent_and_upcoming_presentations limit: 6 %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td>
                      <a href="{{ page.p_baseurl }}{{ presentation.filename }}.pdf" target="_blank">PDF</a>
                    </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td>
                      <a href="{{ page.p_baseurl }}no_pdf_animation.pdf" target="_blank">PDF</a>
                    </td>
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

More talks, papers, and notes are listed in [Research & Talks](/home/showcase/).

<br/>

## Technical Skills

| Area | Tools and Experience |
|:--|:--|
| Simulation and analysis | Geant4, GEMC, CLAS12 simulations, ROOT, detector geometry, event generation, digitization workflows |
| Programming and infrastructure | C++, Python, shell scripting, Git, GitHub, continuous integration, Docker, Environment Modules, HTCondor, Meson, CMake, SCons |
| Scientific communication | LaTeX, Markdown, HTML, CSS, JavaScript, Highcharts, technical documentation, tutorials, presentations |
| Languages | English, Italian |


<br/>

{% capture left2 %}


## Interests


<div class="no-bullets-list">
  {{ page.interest | markdownify }}
</div>

{% endcapture %}


{% capture right2 %}


## Experience and Education

<br/>

<div class="no-bullets-list">

  {{ page.education | markdownify }}
</div>

{% endcapture %}

{% include two_col_md.html left="40%" right="60%" left_content=left2 right_content=right2 %}

<br/>

## Gallery

<link type="text/css" rel="stylesheet" href="/home/assets/lightslider.css" />
<script src="/home/assets/jq.js"></script>
<script src="/home/assets/lightslider.js"></script>

<div>
	<br/>

	<ul style="text-align:center"  id="light-slider" >
    	<li data-thumb="assets/images/empty.png">
			<img src="assets/images/home/quote1.png" alt="Quote" height="500px" width="90%"/><br/><br/><br/>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/software/charts">Chart CSV displayer<br/><img src="assets/images/software/charts_big.png" alt="Chart CSV displayer screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/meson/pi0_delta/pi0_delta">N → Δ(1232) transition <br/><img src="assets/images/pi0/pi0_delta_results.png" alt="N to Delta transition results" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/wfd/">What's For Dinner meal planner<br/><img src="assets/images/home/wfd.png" alt="What's For Dinner meal planner screenshot" height="500px" width="90%"/></a>
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
