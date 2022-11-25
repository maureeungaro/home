---
layout: default
title: Showcase
permalink: /Showcase/
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

## Meson Electro-production

<table>
	{% for presentation in site.data.meson_electroproduction %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"> pdf </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"> pdf </a> </td>
                {% endif %}
                {% if presentation.key == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.key"> key </a> </td>
                {% endif %}
                {% if presentation.pptx == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pptx"> ppt </a> </td>
                {% endif %}

            <td>{{presentation.occasion}} </td>
            <td> {{presentation.date}} </td>

        </tr>
	{% endfor %}
</table>

