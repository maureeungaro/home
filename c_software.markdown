---
layout: default
title: Software
permalink: /Software/
---

A collection of 
 
<table class="alternate">
	{% for code in site.data.software %}
		<tr>
            <td> <a href="{{ code.name }}" > {{ code.name }} </a> </td>
            <td> <img src="{{ code.image }}"> </td>
            <td> {{ code.description }} </td>
        </tr>
	{% endfor %}

</table>
<br/><br/><br/>