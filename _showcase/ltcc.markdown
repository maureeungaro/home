---
layout: default
title: Low Threshold Cherenkov Counter Talks
description: LTCC talks and presentations on the CLAS12 Low Threshold Cherenkov Counter, pion/kaon discrimination, refurbishment, operation, calibration, and detector performance in Hall-B.
permalink: /showcase/ltcc
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# Low Threshold Cherenkov Presentations

Talks related to CLAS12 LTCC refurbishment, operation, calibration, detector performance,
and pion/kaon discrimination in the Hall-B forward detector.

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> PDF </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.ltcc_presentations %}
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
