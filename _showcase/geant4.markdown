---
layout: default
title: Mauri's Geant4 presentations
permalink: /showcase/geant4
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# Geant4 Presentations

Geant4 tutorials, user support material, and selected physics-list or simulation updates.

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> PDF </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	

	{% for presentation in site.data.geant4_presentations %}
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
