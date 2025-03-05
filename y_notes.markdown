---
layout: default
title: Notes
permalink: /mynotes/
---

<table class="alternate">
	{% for note in site.data.mynotes %}
	    {% assign mod_result = forloop.index | minus: 1 | modulo: 12 %}
	    {% if mod_result == 0 %}
	        <tr>
	    {% endif %}
            <td> <a href="{{ note.link }}">{{ note.title }}</a> </td>
	    {% if mod_result == 11 or forloop.last %}
	        </tr>
	    {% endif %}
	{% endfor %}
</table>

