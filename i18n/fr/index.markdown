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

lang: fr
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
src="assets/images/home/mauri.png"
alt="Portrait of Maurizio Ungaro"
width="170"
%}

<div style="text-align: center">
<h2>Maurizio Ungaro</h2> 
<p>Physicien nucléaire et développeur de logiciels de simulation</p>
</div>

|                     `Staff Scientist`                      |
|:----------------------------------------------------------:|
|        [Jefferson Laboratory](https://www.jlab.org)        |
| [Hall expérimental B](https://www.jlab.org/physics/hall-b) |

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

## À propos de moi

Je suis Maurizio (Mauri) Ungaro, chercheur permanent au [Hall-B](https://www.jlab.org/physics/hall-b)
du [Jefferson Lab](https://www.jlab.org). Je travaille sur la physique nucléaire, les systèmes de détecteurs et les logiciels de simulation.

Mes travaux actuels comprennent des simulations fondées sur Geant4 avec GEMC, les chaînes de production CLAS12 sur
l'Open Science Grid, ainsi que l'exploitation, l'étalonnage et les études de performance du compteur Cherenkov
à bas seuil de CLAS12. Mes recherches explorent la structure du nucléon par l'électroproduction de mésons.

Vous trouverez ici des logiciels, des présentations, des notes techniques et des exemples pratiques pour les collaborateurs et les étudiants.

Pendant mon temps libre, j'apprends à jouer au hockey tout en prenant plaisir à regarder mon enfant patiner bien plus vite que moi.

<table class="zebra compact-table">
  <tr>
    <th>Liens principaux</th>
    <td><a href="/home/profile/">Profil</a></td>
    <td><a href="https://gemc.github.io/home/">GEMC</a></td>
    <td><a href="/home/showcase/">Recherche et présentations</a></td>
    <td><a href="/home/mynotes/">Notes</a></td>
  </tr>
</table>

Pour toute collaboration ou aide concernant les simulations et les détecteurs, [écrivez-moi](mailto:ungaro@jlab.org).
Vous pouvez également retrouver mes publications et mon code via les profils ci-dessous.
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
    <td><a href="{{ email_link }}"><img src="{{ email_img }}" alt="Email"></a><br/><a href="{{ email_link }}">Courriel</a></td>
  </tr>
</table>

<br/><br/>

## Dernières actualités et travaux à venir

<table class="alternate">
  <thead>
    <tr><th scope="col">Actualités</th><th scope="col">Date / Statut</th></tr>
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

La note CLAS12 à paraître décrit le framework simGrid OSG, avec des schémas de son architecture
et de ses flux de traitement des tâches. En attendant sa publication,
le lien d'actualité mène à [l'aperçu de CLAS12 sur OSG]({{ '/osg/osg' | relative_url }}).

<br/>

## Par où commencer

| Si vous cherchez...                          | Commencez par                                            |
|:---------------------------------------------|:---------------------------------------------------------|
| Biographie, CV, résumé professionnel ou liens professionnels | [Profil](/home/profile/)                    |
| Exemples Geant4, tutoriels ou assistance JLab | [Geant4 au JLab](https://jeffersonlab.github.io/g4home/) |
| Chaînes de simulation GEMC                    | [GEMC](https://gemc.github.io/home/)                     |
| Versions des simulations CLAS12               | [Simulations CLAS12](https://github.com/gemc/clas12Tags) |
| Production distribuée de simulations          | [CLAS12 sur OSG](/home/osg/osg)                          |
| Présentations de recherche, articles et notes techniques | [Recherche et présentations](/home/showcase/)    |
| Notes pratiques d'informatique                | [Notes](/home/mynotes/)                                  |

<br/><br/>

## Mes domaines de travail

- **Physique nucléaire :** structure du nucléon, analyses dans la région des résonances et transition entre les descriptions
  hadronique et partonique, notamment la [transition N → Δ (1232)](/home/meson/pi0_delta/pi0_delta)
  et l'[électroproduction de mésons à Q<sup>2</sup> élevé](/home/meson/pi0_resonance/pi0_resonance).
- **Systèmes de détecteurs :** exploitation, maintenance, étalonnage et études de performance du
  [compteur Cherenkov à bas seuil de CLAS12](/home/ltcc/ltcc).
- **Logiciels de simulation :** développement de [GEMC et GEMC3](https://gemc.github.io/home/),
  des [simulations CLAS12](https://github.com/gemc/clas12Tags) et des
  [chaînes de production sur l'Open Science Grid](/home/osg/osg).
- **Calcul scientifique et assistance :** [Geant4 au JLab](https://jeffersonlab.github.io/g4home/),
  chaînes de simulation reproductibles, tutoriels, exemples et documentation destinée aux utilisateurs.

<br/>

## Présentations et notes récentes et à venir

<br/>

<table class="alternate">

	<tr>
		<th scope="col">Titre</th>
		<th scope="col">PDF</th>
		<th scope="col">Événement</th>
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

D'autres présentations, articles et notes figurent dans [Recherche et présentations](/home/showcase/).

<br/>

## Compétences techniques

| Domaine                        | Outils et expérience                                                                                                          |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Simulation et analyse          | Geant4, GEMC, simulations CLAS12, ROOT, géométrie des détecteurs, génération d'événements, chaînes de numérisation           |
| Programmation et infrastructure | C++, Python, scripts shell, Git, GitHub, intégration continue, Docker, Environment Modules, HTCondor, Meson, CMake, SCons |
| Communication scientifique     | LaTeX, Markdown, HTML, CSS, JavaScript, Highcharts, documentation technique, tutoriels, présentations                         |
| Langues                        | Anglais, italien                                                                                                              |

<br/>

{% capture left2 %}

## Centres d'intérêt

<div class="no-bullets-list">
  {{ page.interest | markdownify }}
</div>

{% endcapture %}

{% capture right2 %}

## Expérience et formation

<br/>

<div class="no-bullets-list">

{{ page.education | markdownify }}
</div>

{% endcapture %}

{% include two_col_md.html left="40%" right="60%" left_content=left2 right_content=right2 %}

<br/>

## Galerie

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
			<a href="/home/software/charts">Afficheur de graphiques CSV<br/><img src="assets/images/software/charts_big.png" alt="Chart CSV displayer screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/meson/pi0_delta/pi0_delta">Transition N → Δ(1232) <br/><img src="assets/images/pi0/pi0_delta_results.png" alt="N to Delta transition results" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/wfd/">Planificateur de repas What's For Dinner<br/><img src="assets/images/home/wfd.png" alt="What's For Dinner meal planner screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="https://gemc.github.io/home/">Page d'accueil de GEMC<br/><img src="assets/images/home/gemc_home.png" alt="GEMC home page screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="https://gemc.jlab.org/web_interface/index.php">Interface web de simulation GEMC<br/><img src="assets/images/home/osg.png" alt="GEMC simulation web interface screenshot" height="500px" width="90%"/></a>
    	</li>
	</ul>

</div>


<br/><br/><br/>

{:.zebra}

| Déploiement de la page d'accueil | [![CI][CI-badge]][CI]  |


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
