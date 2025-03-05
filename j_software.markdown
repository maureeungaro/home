---
layout: default
title: Software
permalink: /software/
---


 
<table class="alternate">
	{% for code in site.data.software %}
		<tr>
            <td style="width: 30%; padding: 2%; text-align: center" > <a href="{{ code.link }}"><img src="../{{ code.image }}" > </a></td>
            <td> <a href="{{ code.link }}" > {{ code.name }} </a> <br/><br/>  {{ code.description }} </td>
        </tr>
	{% endfor %}

</table>
<br/><br/><br/>
