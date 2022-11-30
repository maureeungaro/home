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

## [CLAS12 Technical Notes](https://misportal.jlab.org/mis/physics/clas12/index.cfm)

### 2021 

- [Nuclear target test report](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2021-001.pdf?documentId=72)
- [Improving GEMC model of CLAS12 using electron radiation](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2021-004.pdf?documentId=76)
- [LTCC pion efficiency analysis](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2021-006.pdf?documentId=77)


### 2019

- [Study of tungsten shielding around the target to limit background rates and radiation dose in the CLAS12 BST](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2019-002.pdf?documentId=63)

### 2018

- [Background Merging Mechanism in GEMC](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2018-002.pdf?documentId=56)
- [Study of tungsten shielding around the target](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2018-005.pdf?documentId=59)
- [Study of Tungsten Shielding Before CTOF to Limit its PMT Currents](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2018-006.pdf?documentId=60)

### 2017

- [CALCOM Calibration Challenge Report](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-002.pdf?documentId=37)
- [Geometry and Alignment Software for the CLAS12 Silicon Vertex Tracker](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-008.pdf?documentId=43)
- [CALCOM Calibration Challenge Report - Second Challenge Exercise](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-010.pdf?documentId=45)
- [Corrections to CLAS12 vacuum beamline](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-012.pdf?documentId=47)
- [Corrections to CLAS12 target design](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-013.pdf?documentId=48)
- [Study of the electromagnetic background rates in CLAS12](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-016.pdf?documentId=52)
- [Importing CLAS12 CAD models of target and beamline in the GEMC simulation.](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-017.pdf?documentId=53)
- [Beam position study on a 3.5 mm shifted target cell](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2017-018.pdf?documentId=54)


### 2016

- [Moller shield simulations: comparison of the GEMC-optimized layout and engineering design](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2016-006.pdf?documentId=32)
- [Study of the electromagnetic background with varying solenoid field](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2016-008.pdf?documentId=34)

### 2014

- [Common Environment for Software Packages](https://misportal.jlab.org/mis/physics/clas12/viewFile.cfm/2014-002.pdf?documentId=10)


## [CLAS Technical Notes](https://misportal.jlab.org/ul/Physics/Hall-B/clas/index.cfm)

### 2011

- [Simulation of the Electromagnetic Calorimeter in CLAS12](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2011-019.pdf?documentId=655)
- [Simulated CLAS12 Neutron Detection Efficiency in the Forward Time-of-Flight System](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2011-015.pdf?documentId=649)

### 2010

- [Meson electro-production Radiative Corrections based on Exclurad](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2010-006.pdf?documentId=591)



### 2009

- [Program to Add Helicity Information to Cooked BOS Files](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2009-005.pdf?documentId=525)
- [Banks: a library to handle the CLAS12 EVIO format](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2009-012.pdf?documentId=534)

### 2005

- [g11 data processing](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2005-014.pdf?documentId=188)

### 2004

- [Interactive Monitoring Histograms Generator](https://misportal.jlab.org/ul/Physics/Hall-B/clas/viewFile.cfm/2004-028.pdf?documentId=99)

### 2003

- [Procedure for Drift Chamber Inefficiencies](https://www.jlab.org/Hall-B/notes/clas_notes03/03-006.pdf)
