---
layout: base
title: Gemc Tutorials
---

## GEMC Tutorials

<br>

<ul>

	{% assign pages_list = site.tutorials | sort: 'order' %}
	{% for post in pages_list %}
		{% if post.url contains 'Tuts' %}
			{% continue %}
		{% endif %}
	<li>
		<h5><a href="/home/{{ post.url }}">{{ post.title }}</a></h5>
		{{ post.description }}<br/><br/>
	</li>
	{% endfor %}
	
	
</ul>
