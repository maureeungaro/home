---
layout: default
title: Mauri's LTCC Work
permalink: /showcase/ltcc
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

<table>
	{% for presentation in site.data.meson_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>
                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf" target=_blank> pdf </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf" target=_blank> pdf </a> </td>
                {% endif %}
                {% if presentation.key == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.key" target=_blank> key </a> </td>
                {% endif %}
                {% if presentation.pptx == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pptx" target=_blank> ppt </a> </td>
                {% endif %}
                 {% if presentation.pptx == "no" %}
                    <td> na </td>
                {% endif %}
           <td>{{presentation.occasion}} </td>
            <td> {{presentation.date}} </td>
        </tr>
	{% endfor %}
</table>
