---
layout: default
title: Showcase
permalink: /showcase/
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
pub_baseurl: "https://userweb.jlab.org/~ungaro/pubs/"
---

<br/>

# Recent and Upcoming talks

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
<br/><br/>

# Selected Papers

<table class="alternate">
	{% for paper in site.data.selected_papers %}
		<tr>
            <td> <a href="{{ paper.inspire }}"> {{ paper.title }}</a> </td>
            <td> <a href="{{ paper.pdf }}"> pdf </a> </td>
            <td> {{ paper.journal }} </td>
        </tr>
	{% endfor %}
</table>


A list of all Mauri's research papers can be found at [Mauri's profile on Inspire](https://inspirehep.net/authors/1322331){:target="_blank"}

<br/><br/>

# Meson Electro-production Presentations

Selected Presentations:

<table class="alternate">
	{% for presentation in site.data.meson_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf" target="_blank"> pdf </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"          target="_blank"> pdf </a> </td>
                {% else %}
                    <td> na </td>
                {% endif %}

                {% if presentation.key == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.key" target="_blank"> key </a> </td>
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

A list of all meson electro-production presentations can be found at [mauri's meson electro-production presentations](/home/showcase/meson).

<br/><br/>

# Low Threshold Cherenkov Counter (LTCC)

<table class="alternate">
	{% for presentation in site.data.ltcc_selected_presentations %}
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

A list of all the ltcc presentations can be found at [mauri's ltcc presentations](/home/showcase/ltcc).

<br/><br/>

# GEANT4

<table class="alternate">
	{% for presentation in site.data.geant4_selected_presentations %}
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

A list of all the geant4 presentations can be found at [mauri's geant4 presentations](/home/showcase/geant4).

<br/><br/>

# GEMC

<table class="alternate">
	{% for presentation in site.data.gemc_selected_presentations %}
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

A list of all the gemc presentations can be found at [mauri's gemc presentations](/home/showcase/gemc).

<br/><br/>

# Open Science Grid

<table class="alternate">
	{% for presentation in site.data.osg_presentations %}
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


<br/><br/>

# Selected CLAS/CLAS12 Technical Notes

<table class="alternate">
	{% for note in site.data.selected_notes %}
        <tr>
            <td> {{ note.title }} </td>

            <td> <a href="{{ note.pdf }}"  target="_blank"> pdf </a> </td>
                
            <td> {{ note.year }} </td>

            {% if note.source == "na" %}
                <td> na </td>
            {% else %}
                {% assign ext5 = note.source | slice: -5, 5 %}
                {% assign ext6 = note.source | slice: -6, 6 %}
                {% if ext5 == ".docx" %}
                    <td> <a href="{{ page.pub_baseurl }}/{{ note.source }}" target="_blank"> docx </a> </td>
                {% elsif ext6 == ".pages" %}
                    <td> <a href="{{ page.pub_baseurl }}/{{ note.source }}" target="_blank"> pages </a> </td>
                {% else %}
                    <td> <a href="{{ page.pub_baseurl }}/{{ note.source }}" target="_blank"> source </a> </td>
                {% endif %}
            {% endif %}

        </tr>
	{% endfor %}
</table>


A list of all tecnhical CLAS and CLAS12 notes can be found at [mauri's techical notes](/home/showcase/clas_notes).


