---
layout: default
title: "作業日誌"
description: Weekly summaries of my work on Geant4/GEMC simulations, CLAS12 software, and Open Science Grid
  production workflows, compiled every Friday.
permalink: /weekly/
lang: ja
human_reviewed: false
---

毎週取り組んだ内容を簡潔にまとめた概要です。毎週金曜日に日々のメモをもとに作成しています。

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
