---
layout: default
title: Mauri's LTCC Work
permalink: /showcase/ltcc
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> pdf </td>
		<td> Occasion </td>
		<td> Date </td>
	</tr>	
	{% for presentation in site.data.ltcc_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>
                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> pdf </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> pdf </a> </td>
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