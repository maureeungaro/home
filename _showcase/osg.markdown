---
layout: default
title: OSG Talks and Presentations
description: Talks on the Open Science Grid deployment of CLAS12 simulations
permalink: /showcase/osg
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# OSG Presentations

Talks on the Open Science Grid deployment of CLAS12 simulations

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> Format </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.osg_presentations %}
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
