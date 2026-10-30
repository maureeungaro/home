---
layout: default
title: Geant4 Talks and Tutorials
description: Geant4 talks, tutorials, and user-support material for Jefferson Lab users, including simulation examples, physics updates, and training material.
permalink: /showcase/geant4
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# Geant4 Presentations

Geant4 tutorials, user support material, and selected physics-list or simulation updates.

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> Format </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	

	{% for presentation in site.data.geant4_presentations %}
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
