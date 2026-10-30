---
layout: default
title: GEMC Talks and Presentations
description: GEMC talks and presentations on Geant4 detector simulation, CLAS12 workflows, database-driven geometry, and Jefferson Lab simulation production.
permalink: /showcase/gemc
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# GEMC Presentations

Talks on GEMC development, CLAS12 simulations, and database-driven detector descriptions.

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> Format </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.gemc_presentations %}
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
