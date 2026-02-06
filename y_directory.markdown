---
layout: default
title: Directory
permalink: /directory/
---

{% assign NUM_COLUMNS = 5 %}
{% assign items = site.data.bookmarks | group_by: "category" %}

<div class="directory-page">


  <ul class="link-list">
    {% for group in items %}
      <li class="section">
        <div class="section-title">{{ group.name | escape }}</div>

        <ul class="section-links">
          {% for item in group.items %}

            {%- assign has_multi = false -%}
            {%- if item.tit1 and item.link1 -%}
              {%- assign has_multi = true -%}
            {%- endif -%}

            {%- if has_multi -%}
              <li>
                {{ item.title | escape }}:
                {%- for i in (1..10) -%}
                  {%- assign titk = 'tit' | append: i -%}
                  {%- assign linkk = 'link' | append: i -%}
                  {%- if item[titk] and item[linkk] -%}
                    <a href="{{ item[linkk] | escape }}" target="_blank">[ {{ item[titk] | escape }} ]</a>
                  {%- endif -%}
                {%- endfor -%}
              </li>
            {%- else -%}
              <li>
                <a href="{{ item.link1 | escape }}" target="_blank">[ {{ item.title | escape }} ]</a>
              </li>
            {%- endif -%}

          {% endfor %}
        </ul>
      </li>

    {% endfor %}
  </ul>


</div>
