---
layout: default
title: Blog
permalink: /Blog/
---

# Mauri's Blog

<script>

function my_select(mysel) {
    var frame_id = mysel + '_content'
    console.log(frame_id)

    button_src  =  document.getElementById(frame_id).contentWindow.document.getElementById('html_button_selector').innerHTML;
    document.getElementById("html_button_selector").innerHTML = button_src;
    //document.getElementById("myTextField").focus();

    content_src =  document.getElementById(frame_id).contentWindow.document.getElementById('html_content_selector').innerHTML;
    document.getElementById("html_content_selector").innerHTML = content_src;

}
</script>




<div id="html_button_selector">
<div class="button-group">
<button onclick="my_select('all')      ; " style="outline: 2px solid #2a7ae2;" > All      </button>
<button onclick="my_select('geant4')   ; "                                     > Geant4   </button>
<button onclick="my_select('gemc')     ; "                                     > GEMC     </button>
<button onclick="my_select('physics')  ; "                                     > Physics  </button>
<button onclick="my_select('software') ; "                                     > Software </button>
<button onclick="my_select('personal') ; "                                     > Personal </button>
</div>
</div>

<br/>
<br/>


<div id="html_content_selector">

{%- for post in site.posts -%}
{%- assign cats = post.categories | join: " " -%}


{%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
<span class="post-meta">{{ post.date | date: date_format }}<br></span>
<span class="post-meta">Category: {{ post.categories }}</span>

<br/>
<a href="{{ post.url | relative_url }}">{{post.title}}</a>
{{ post.excerpt }}
<br/>


{%- endfor -%}

</div>

<iframe id="all_content"       src="../search/all.html"        style="display:none"></iframe>
<iframe id="geant4_content"    src="../search/geant4.html"     style="display:none"></iframe>
<iframe id="gemc_content"      src="../search/gemc.html"       style="display:none"></iframe>
<iframe id="physics_content"   src="../search/physics.html"    style="display:none"></iframe>
<iframe id="software_content"  src="../search/software.html"   style="display:none"></iframe>
<iframe id="personal_content"  src="../search/personal.html"   style="display:none"></iframe>
