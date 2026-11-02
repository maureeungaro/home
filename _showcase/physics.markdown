---
layout: default
title: Physics Talks and Presentations
description: Physics talks on meson electro-production, CLAS nucleon-structure measurements, nucleon-resonance electro-excitation, transition form factors, resonance-region analyses, and the Heavy Photon Search.
permalink: /showcase/physics
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# Physics Presentations

Physics presentations on meson electro-production, nucleon-structure measurements, nucleon-resonance studies
with CLAS, and the Heavy Photon Search.

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> Format </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	

	{% for presentation in site.data.physics_presentations %}
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
