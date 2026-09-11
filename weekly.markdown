---
layout: default
title: Work Journal
description: Weekly summaries of my work on Geant4/GEMC simulations, CLAS12 software, and Open Science Grid
  production workflows, compiled every Friday.
permalink: /weekly/
---

Short, high-level summaries of what I worked on each week — compiled from my daily notes every Friday.

<br/>

{% assign weeks = site.weekly | sort: "date" | reverse %}
{% assign months = weeks | group_by: "month" %}

<div class="directory-page directory-container">
	{% for group in months %}
		<div class="directory-section" {% unless forloop.last %}style="margin-bottom: 2em;"{% endunless %}>
			<div class="section-title">{{ group.name | escape }}</div>
			<div class="directory-links directory-links--4" style="--directory-columns: 4;">
				{% for week in group.items %}
					<div class="directory-entry">
						<a href="{{ week.url | relative_url }}">[&nbsp;{{ week.title | escape }}&nbsp;]</a>
					</div>
				{% endfor %}
			</div>
		</div>
	{% endfor %}
</div>
