---
layout: default
title: "Recherche et présentations"
description: Selected papers, talks, tutorials, and technical notes on Geant4, GEMC, CLAS12 simulations, detector work, and nucleon-structure research.
permalink: /showcase/
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
pub_baseurl: "https://userweb.jlab.org/~ungaro/pubs/"
lang: fr
human_reviewed: false
---

<br/>

# Exposés et notes récents

Séminaires, tutoriels, notes techniques et actualités des collaborations portant sur Geant4, GEMC, la simulation CLAS12 et les travaux sur les détecteurs.

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Événement </td>
		<td> Date </td>
	</tr>

	{% for presentation in site.data.recent_and_upcoming_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
                 {% else %}
                    <td></td>
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
<br/><br/>

# Articles choisis

Articles représentatifs liés à mes travaux sur la simulation, les détecteurs et l'électroproduction de mésons.

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Revue </td>
	</tr>
	{% for paper in site.data.selected_papers %}
		<tr>
            <td> <a href="{{ paper.inspire }}"> {{ paper.title }}</a> </td>
            <td> <a href="{{ paper.pdf }}"> PDF </a> </td>
            <td> {{ paper.journal }} </td>
        </tr>
	{% endfor %}
</table>


Tous les articles de recherche sont répertoriés dans le [profil INSPIRE de Maurizio Ungaro](https://inspirehep.net/authors/1322331){:target="_blank"}.

<br/><br/>

# Présentations sur l'électroproduction de mésons

Présentations choisies :

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Événement </td>
		<td> Date </td>
	</tr>
	{% for presentation in site.data.meson_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf" target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"          target="_blank"> PDF </a> </td>
                {% else %}
                    <td></td>
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

Toutes les présentations sur l'électroproduction de mésons sont répertoriées dans [Exposés sur l'électroproduction de mésons](/home/showcase/meson).

<br/><br/>

# Compteur Cherenkov à bas seuil (LTCC)

Exposés choisis sur le fonctionnement, l'étalonnage et les performances du détecteur LTCC.

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Événement </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.ltcc_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
                 {% else %}
                    <td></td>
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

Toutes les présentations sur le LTCC sont répertoriées dans [Exposés sur le compteur Cherenkov à bas seuil](/home/showcase/ltcc).

<br/><br/>

# Geant4

Tutoriels et présentations choisis destinés aux utilisateurs de Geant4 à JLab et lors d'ateliers connexes.

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Événement </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.geant4_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
                 {% else %}
                    <td></td>
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

Toutes les présentations Geant4 sont répertoriées dans [Exposés et tutoriels Geant4](/home/showcase/geant4).

<br/><br/>

# GEMC

Exposés choisis sur GEMC, les simulations CLAS12 et les flux de travail de simulation pilotés par des bases de données.

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Événement </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.gemc_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
                 {% else %}
                    <td></td>
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

Toutes les présentations GEMC sont répertoriées dans [Exposés et présentations GEMC](/home/showcase/gemc).

<br/><br/>

# Open Science Grid

Présentations sur les flux de travail de simulation CLAS12 et les ressources de calcul distribué.

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Événement </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.osg_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
                 {% else %}
                    <td></td>
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


<br/><br/>

# Notes techniques CLAS/CLAS12 choisies

Notes techniques choisies pour les travaux sur les détecteurs et la simulation de CLAS et CLAS12.

<table class="alternate">
	<tr>
		<td> Titre </td>
		<td> PDF </td>
		<td> Date </td>
	</tr>	

	{% for note in site.data.selected_notes %}
        <tr>
            <td> {{ note.title }} </td>

            {% if note.source == "soon" %}
                <td> Bientôt disponible </td>
            {% else %}
                <td> <a href="{{ note.pdf }}"  target="_blank"> PDF </a> </td>
			{% endif %}

            <td> {{ note.year }} </td>


        </tr>
	{% endfor %}
</table>


Toutes les notes techniques CLAS et CLAS12 sont répertoriées dans [Notes techniques CLAS et CLAS12](/home/showcase/clas_notes).
