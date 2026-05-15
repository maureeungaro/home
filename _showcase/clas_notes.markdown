---
layout: default
title: Mauri's Technical Notes
permalink: /showcase/clas_notes
pub_baseurl: "https://userweb.jlab.org/~ungaro/pubs/"
---

<br/>

# CLAS Notes

Technical notes for CLAS and CLAS12 detector, reconstruction, and simulation work.

<table class="alternate">
	<tr>
		<td> Title </td>
		<td> PDF </td>
		<td> Date </td>
	</tr>	

	{% for note in site.data.all_notes %}
        <tr>
            <td> {{ note.title }} </td>

            {% if note.source == "soon" %}
                <td> Coming soon </td>
            {% else %}
                <td> <a href="{{ note.pdf }}"  target="_blank"> PDF </a> </td>
			{% endif %}

            <td> {{ note.year }} </td>

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
