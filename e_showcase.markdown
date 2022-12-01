---
layout: default
title: Showcase
permalink: /Showcase/
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

# Papers



Selected Papers:

<table>
 
	{% for paper in site.data.selected_papers %}
		<tr>
            <td> <a href="{{ paper.inspire }}"> {{ paper.title }}</a> </td>
            <td> <a href="{{ paper.pdf }}"> pdf </a> </td>
            <td> {{ paper.journal }} </td>
        </tr>
	{% endfor %}
</table>


A list of all Mauri's research papers can be found at [Mauri's profile on Inspire](https://inspirehep.net/authors/1322331)

<br/>


# Meson Electro-production Presentations

Selected Presentations:

<table>
	{% for presentation in site.data.selected_meson_presentations %}
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

A list of all meson electro-production presentations can be found at [mauri's meson electro-production presentations](/home/showcase/meson).


<br/>

# CLAS/CLAS12 Technical Notes

Selected Notes:


- [Background Merging Mechanism in GEMC](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2018-002.pdf?documentId=56)
- [Study of the electromagnetic background rates in CLAS12](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-016.pdf?documentId=52)
- [Importing CLAS12 CAD models of target and beamline in the GEMC simulation](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-017.pdf?documentId=53)
- [Meson electro-production Radiative Corrections based on Exclurad](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2010-006.pdf?documentId=591)
- [g11 data processing](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2005-014.pdf?documentId=188)
- [Procedure for Drift Chamber Inefficiencies](https://www.jlab.org/Hall-B/notes/clas_notes03/03-006.pdf)

A list of all tecnhical notes can be found at [mauri' CLAS12 techical notes](/home/showcase/clas12_notes) and at [mauri's CLAS techical notes](/home/showcase/clas_notes) 


