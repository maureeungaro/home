---
layout: default
title: Directory
permalink: /directory/
---

{% assign items = site.data.bookmarks | group_by: "category" %}

{% for group in items %}
## {{ group.name }}

<div class="link-grid">
  {% for item in group.items %}
    <span class="link-item">[<a href="{{ item.link }}">{{ item.title }}</a>]</span>
  {% endfor %}
</div>
<br/>

{% endfor %}


<br/><br/>