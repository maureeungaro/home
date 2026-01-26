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

    {%- assign has_multi = false -%}
    {%- if item.tit1 and item.link1 -%}
      {%- assign has_multi = true -%}
    {%- endif -%}

    {%- if has_multi -%}
      <span class="link-item">
        <b> {{ item.title }}</b>:  
        {%- for i in (1..10) -%}
          {%- assign titk = 'tit' | append: i -%}
          {%- assign linkk = 'link' | append: i -%}
          {%- if item[titk] and item[linkk] -%}
            [<a href="{{ item[linkk] }}">{{ item[titk] }}</a>]
          {%- endif -%}
        {%- endfor -%}
      </span>
    {%- else -%}
      <span class="link-item">[<a href="{{ item.link1 }}">{{ item.title }}</a>]</span>
    {%- endif -%}

  {% endfor %}
</div>
<br/>

{% endfor %}

<br/><br/>
