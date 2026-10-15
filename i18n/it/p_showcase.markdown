---
layout: default
title: "Ricerca e presentazioni"
description: Selected papers, talks, tutorials, and technical notes on Geant4, GEMC, CLAS12 simulations, detector work, and nucleon-structure research.
permalink: /showcase/
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
pub_baseurl: "https://userweb.jlab.org/~ungaro/pubs/"
lang: it
human_reviewed: false
---

<br/>

# Presentazioni e note recenti

Seminari, tutorial, note tecniche e aggiornamenti recenti della collaborazione su Geant4, GEMC, simulazioni CLAS12 e attività sui rivelatori.

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Evento </td>
		<td> Data </td>
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

# Articoli selezionati

Articoli rappresentativi del mio lavoro su simulazioni, rivelatori ed elettroproduzione di mesoni.

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Rivista </td>
	</tr>
	{% for paper in site.data.selected_papers %}
		<tr>
            <td> <a href="{{ paper.inspire }}"> {{ paper.title }}</a> </td>
            <td> <a href="{{ paper.pdf }}"> PDF </a> </td>
            <td> {{ paper.journal }} </td>
        </tr>
	{% endfor %}
</table>


Tutti gli articoli di ricerca sono elencati nel [profilo INSPIRE di Maurizio Ungaro](https://inspirehep.net/authors/1322331){:target="_blank"}.

<br/><br/>

# Presentazioni sull'elettroproduzione di mesoni

Presentazioni selezionate:

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Evento </td>
		<td> Data </td>
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

Tutte le presentazioni sull'elettroproduzione di mesoni sono elencate in [Presentazioni sull'elettroproduzione di mesoni](/home/showcase/meson).

<br/><br/>

# Contatore Cherenkov a bassa soglia (LTCC)

Presentazioni selezionate sul funzionamento, la calibrazione e le prestazioni del rivelatore LTCC.

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Evento </td>
		<td> Data </td>
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

Tutte le presentazioni sul LTCC sono elencate in [Presentazioni sul contatore Cherenkov a bassa soglia](/home/showcase/ltcc).

<br/><br/>

# Geant4

Tutorial e presentazioni selezionati per gli utenti di Geant4 al JLab e nei workshop correlati.

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Evento </td>
		<td> Data </td>
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

Tutte le presentazioni su Geant4 sono elencate in [Presentazioni e tutorial su Geant4](/home/showcase/geant4).

<br/><br/>

# GEMC

Presentazioni selezionate su GEMC, simulazioni CLAS12 e flussi di lavoro di simulazione basati su database.

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Evento </td>
		<td> Data </td>
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

Tutte le presentazioni su GEMC sono elencate in [Interventi e presentazioni su GEMC](/home/showcase/gemc).

<br/><br/>

# Open Science Grid

Presentazioni sui flussi di lavoro di simulazione CLAS12 e sulle risorse di calcolo distribuito.

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Evento </td>
		<td> Data </td>
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

# Note tecniche selezionate su CLAS/CLAS12

Note tecniche selezionate per il lavoro sui rivelatori e sulle simulazioni CLAS e CLAS12.

<table class="alternate">
	<tr>
		<td> Titolo </td>
		<td> PDF </td>
		<td> Data </td>
	</tr>	

	{% for note in site.data.selected_notes %}
        <tr>
            <td> {{ note.title }} </td>

            {% if note.source == "soon" %}
                <td> In arrivo a breve </td>
            {% else %}
                <td> <a href="{{ note.pdf }}"  target="_blank"> PDF </a> </td>
			{% endif %}

            <td> {{ note.year }} </td>


        </tr>
	{% endfor %}
</table>


Tutte le note tecniche su CLAS e CLAS12 sono elencate in [Note tecniche su CLAS e CLAS12](/home/showcase/clas_notes).
