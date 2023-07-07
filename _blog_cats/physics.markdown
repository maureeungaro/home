---
layout: default
title: physics
permalink: /search/physics
---


<div id="html_button_selector">
<div class="button-group">
<button onclick="my_select('all')      ; "                                     > All      </button>
<button onclick="my_select('geant4')   ; "                                     > Geant4   </button>
<button onclick="my_select('gemc')     ; "                                     > GEMC     </button>
<button onclick="my_select('physics')  ; " style="outline: 2px solid #2a7ae2;" > Physics  </button>
<button onclick="my_select('software') ; "                                     > Software </button>
<button onclick="my_select('personal') ; "                                     > Personal </button>
</div>
</div>

<div id="html_content_selector">

{%- for post in site.posts -%}
{%- assign cats = post.categories | join: " " -%}
{%- if cats contains "physics" -%}

{%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
<span class="post-meta">{{ post.date | date: date_format }}<br></span>
<span class="post-meta">Category: {{ post.categories }}</span>

<br/>
<a href="{{ post.url | relative_url }}">{{post.title}}</a>
{{ post.excerpt }}
<br/>
{%- endif -%}

{%- endfor -%}

</div>

