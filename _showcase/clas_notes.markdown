---
layout: default
title: Mauri's Technical Notes
permalink: /showcase/clas_notes
pub_baseurl: "https://userweb.jlab.org/~ungaro/pubs/"
---

<br/>

<table class="alternate">
	{% for note in site.data.all_notes %}
        <tr>
            <td> {{ note.title }} </td>

            {% if note.source == "soon" %}
            	<td> <a href="coming soon"  target="_blank"> pdf </a> </td>
            {% else %}
            	<td> <a href="{{ note.pdf }}"  target="_blank"> pdf </a> </td>
			{% endif %}

            <td> {{ note.year }} </td>

            {% if note.source == "na" %}
                <td> na </td>
            {% else %}
                {% assign ext5 = note.source | slice: -5, 5 %}
                {% assign ext6 = note.source | slice: -6, 6 %}
                {% if ext5 == ".docx" %}
                    <td> <a href="{{ page.pub_baseurl }}/{{ note.source }}" target="_blank"> docx </a> </td>
                {% elsif ext6 == ".pages" %}
                    <td> <a href="{{ page.pub_baseurl }}/{{ note.source }}" target="_blank"> pages </a> </td>
                {% else %}
                    <td> <a href="{{ page.pub_baseurl }}/{{ note.source }}" target="_blank"> source </a> </td>
                {% endif %}
            {% endif %}

        </tr>
	{% endfor %}

</table>

<br/>

---

<br/>

## CLAS Notes Databases:

- [CLAS12 Technical Notes](https://misportal.jlab.org/mis/physics/clas12/index.cfm){:target="_blank"}
- [CLAS Technical Notes](https://misportal.jlab.org/ul/Physics/Hall-B/clas/index.cfm){:target="_blank"}

<br/>

---

<br/>
