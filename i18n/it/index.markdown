---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# See https://github.com/jekyll/minima#readme

# Table: add first row (3 |) for autoformatting

layout: default
permalink: /
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

lang: it
human_reviewed: false
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
src="/assets/images/home/mauri.png"
alt="Portrait of Maurizio Ungaro"
width="170"
%}

<div style="text-align: center">
<h2>Maurizio Ungaro</h2> 
<p>Fisico nucleare e sviluppatore di software di simulazione</p>
</div>

|                     `Staff Scientist`                      |
|:----------------------------------------------------------:|
|        [Jefferson Laboratory](https://www.jlab.org)        |
| [Sala sperimentale Hall-B](https://www.jlab.org/physics/hall-b) |

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

## Chi sono

Sono Maurizio (Mauri) Ungaro, Staff Scientist nella [Hall-B](https://www.jlab.org/physics/hall-b)
al [Jefferson Lab](https://www.jlab.org). Mi occupo di fisica nucleare, rivelatori e software di simulazione.

Il mio lavoro attuale comprende simulazioni basate su Geant4 con GEMC, flussi di produzione CLAS12 sulla
Open Science Grid e attività di gestione, calibrazione e studio delle prestazioni del rivelatore
Cherenkov a bassa soglia di CLAS12. La mia ricerca esplora la struttura del nucleone tramite l'elettroproduzione di mesoni.

Qui puoi trovare software, presentazioni, note tecniche ed esempi pratici per collaboratori e studenti.

Nel tempo libero sto imparando a giocare a hockey e mi diverto a guardare mio figlio pattinare molto più veloce di me.

<table class="zebra compact-table">
  <tr>
    <th>Link principali</th>
    <td><a href="/home/profile/">Profilo</a></td>
    <td><a href="https://gemc.github.io/home/">GEMC</a></td>
    <td><a href="/home/showcase/">Ricerca e presentazioni</a></td>
    <td><a href="/home/mynotes/">Note</a></td>
  </tr>
</table>

Per collaborazioni o assistenza con le simulazioni e le attività sui rivelatori, [scrivimi](mailto:ungaro@jlab.org).
Puoi anche trovare le mie pubblicazioni e il mio codice tramite i profili qui sotto.
<br/>
<br/>

{% endcapture %}

{% include two_col_md.html left="30%" right="70%" left_content=left right_content=right %}

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
    <td><a href="{{ github_link }}"><img src="{{ github_img }}" alt="GitHub"></a><br/><a href="{{ github_link }}">GitHub</a></td>
    <td><a href="{{ orcid_link }}"><img src="{{ orcid_img }}" alt="ORCID"></a><br/><a href="{{ orcid_link }}">ORCID</a></td>
    <td><a href="{{ linkedin_link }}"><img src="{{ linkedin_img }}" alt="LinkedIn"></a><br/><a href="{{ linkedin_link }}">LinkedIn</a></td>
    <td><a href="{{ email_link }}"><img src="{{ email_img }}" alt="Email"></a><br/><a href="{{ email_link }}">Email</a></td>
  </tr>
</table>

<br/><br/>

## Ultime novità e lavori in arrivo

<table class="alternate">
  <thead>
    <tr><th scope="col">Novità</th><th scope="col">Data / Stato</th></tr>
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

La nota CLAS12 di prossima pubblicazione descrive il framework simGrid OSG, con diagrammi dell'architettura
e dei flussi di lavoro dei job. Finché la nota non sarà disponibile,
il link della notizia rimanda alla [panoramica di CLAS12 su OSG]({{ '/osg/osg' | relative_url }}).

<br/>

## Da dove iniziare

| Se stai cercando...                           | Inizia da                                                |
|:---------------------------------------------|:---------------------------------------------------------|
| Biografia, CV, curriculum o link professionali | [Profilo](/home/profile/)                                |
| Esempi e tutorial Geant4 o supporto JLab      | [Geant4 al JLab](https://jeffersonlab.github.io/g4home/) |
| Flussi di lavoro per le simulazioni GEMC     | [GEMC](https://gemc.github.io/home/)                     |
| Release delle simulazioni CLAS12             | [Simulazioni CLAS12](https://github.com/gemc/clas12Tags) |
| Produzione distribuita di simulazioni       | [CLAS12 su OSG](/home/osg/osg)                           |
| Presentazioni di ricerca, articoli e note tecniche | [Ricerca e presentazioni](/home/showcase/)          |
| Note pratiche di informatica                 | [Note](/home/mynotes/)                                  |

<br/><br/>

## Di cosa mi occupo

- **Fisica nucleare:** struttura del nucleone, analisi nella regione delle risonanze e transizione tra descrizioni
  adroniche e partoniche, inclusa la [transizione N → Δ (1232)](/home/meson/pi0_delta/pi0_delta)
  e l'[elettroproduzione di mesoni a Q<sup>2</sup> elevato](/home/meson/pi0_resonance/pi0_resonance).
- **Sistemi di rivelazione:** gestione, manutenzione, calibrazione e studi delle prestazioni del
  [rivelatore Cherenkov a bassa soglia di CLAS12](/home/ltcc/ltcc).
- **Software di simulazione:** sviluppo di [GEMC e GEMC3](https://gemc.github.io/home/),
  delle [simulazioni CLAS12](https://github.com/gemc/clas12Tags) e dei
  [flussi di produzione sulla Open Science Grid](/home/osg/osg).
- **Calcolo scientifico e supporto:** [Geant4 al JLab](https://jeffersonlab.github.io/g4home/),
  flussi di lavoro riproducibili per le simulazioni, tutorial, esempi e documentazione rivolta agli utenti.

<br/>

## Presentazioni e note recenti e in arrivo

<br/>

<table class="alternate">

	<tr>
		<th scope="col">Titolo</th>
		<th scope="col">PDF</th>
		<th scope="col">Evento</th>
		<th scope="col">Data</th>
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

Altre presentazioni, articoli e note sono elencati in [Ricerca e presentazioni](/home/showcase/).

<br/>

## Competenze tecniche

| Area                           | Strumenti ed esperienza                                                                                                       |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Simulazione e analisi          | Geant4, GEMC, simulazioni CLAS12, ROOT, geometria dei rivelatori, generazione di eventi, flussi di digitizzazione             |
| Programmazione e infrastruttura | C++, Python, scripting di shell, Git, GitHub, integrazione continua, Docker, Environment Modules, HTCondor, Meson, CMake, SCons |
| Comunicazione scientifica      | LaTeX, Markdown, HTML, CSS, JavaScript, Highcharts, documentazione tecnica, tutorial, presentazioni                          |
| Lingue                         | Inglese, italiano                                                                                                             |

<br/>

{% capture left2 %}

## Interessi

<div class="no-bullets-list">
  {{ page.interest | markdownify }}
</div>

{% endcapture %}

{% capture right2 %}

## Esperienza e formazione

<br/>

<div class="no-bullets-list">

{{ page.education | markdownify }}
</div>

{% endcapture %}

{% include two_col_md.html left="40%" right="60%" left_content=left2 right_content=right2 %}

<br/>

## Galleria

<link type="text/css" rel="stylesheet" href="/home/assets/lightslider.css" />
<script src="/home/assets/jq.js"></script>
<script src="/home/assets/lightslider.js"></script>

<div>
	<br/>

	<ul style="text-align:center"  id="light-slider" >
    	<li data-thumb="/home/assets/images/empty.png">
			<img src="/home/assets/images/home/quote1.png" alt="Quote" height="500px" width="90%"/><br/><br/><br/>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="/home/software/charts">Visualizzatore di grafici da CSV<br/><img src="/home/assets/images/software/charts_big.png" alt="Chart CSV displayer screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="/home/meson/pi0_delta/pi0_delta">Transizione N → Δ(1232) <br/><img src="/home/assets/images/pi0/pi0_delta_results.png" alt="N to Delta transition results" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="/home/wfd/">Pianificatore di pasti What's For Dinner<br/><img src="/home/assets/images/home/wfd.png" alt="What's For Dinner meal planner screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="https://gemc.github.io/home/">Pagina iniziale di GEMC<br/><img src="/home/assets/images/home/gemc_home.png" alt="GEMC home page screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="https://gemc.jlab.org/web_interface/index.php">Interfaccia web per le simulazioni GEMC<br/><img src="/home/assets/images/home/osg.png" alt="GEMC simulation web interface screenshot" height="500px" width="90%"/></a>
    	</li>
	</ul>

</div>


<br/><br/><br/>

{:.zebra}

| Pubblicazione della pagina iniziale | [![CI][CI-badge]][CI]  |


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


[code]: /home/assets/images/home/code.png

[software]: /home/assets/images/home/software.png

[languages]: /home/assets/images/home/languages.png

[quote1]: /home/assets/images/home/quote1.png
