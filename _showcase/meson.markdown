---
layout: default
title: Meson Electro-Production Talks
description: Presentations on single-meson electro-production, CLAS nucleon-structure measurements, pion production, form factors, and resonance-region analyses.
permalink: /showcase/meson
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# Meson Electro-Production Presentations

Presentations on single-meson electro-production and nucleon-structure measurements.

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> Format </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	

	{% for presentation in site.data.meson_presentations %}
		<tr>
		<td> {{ presentation.title }} </td>
            <td>{% include presentation-formats.html presentation=presentation %}</td>
                {% if presentation.occasion_url == "NA" %}
                    <td>{{presentation.occasion}} </td>
                {% else %}
                     <td> <a href="{{ presentation.occasion_url }}"  target="_blank"> {{presentation.occasion}} </a> </td>
                {% endif %}
            <td> {{presentation.date}} </td>
        </tr>
	{% endfor %}

</table>
