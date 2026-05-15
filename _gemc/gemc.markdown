---
layout: default
title: "GEMC"
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
last_updated: "May 15, 2026"
---

<br/>

# GEMC Simulation Framework

Last updated: {{ page.last_updated }}

<br/>

GEMC (**GE**ant **M**onte-**C**arlo) is a database-driven Monte Carlo simulation program based on Geant4.<br/>

The goal is to provide a turnkey application that allows users
to create and run realistic simulations without programming knowledge, in particular:

- No need to know, write or compile C++ or Geant4
- Automatic handling of multi-threaded hit collections and digitizations
- Pre-defined digitizations such as `flux` and `dosimeter`
- Built-in `text`, 'CSV' and `ROOT` output


<br/>

## [GEMC Homepage](https://gemc.github.io/home/)


<br/>


<br/><br/><br/>

<p style="text-align:center">
<span style="color:#444;font-weight:300;font-size:54px">Selected Talks</span>
</p>

<br/><br/>
<table class="alternate">
    <tr>
        <td> Title </td>
        <td> PDF </td>
        <td> Keynote </td>
        <td> PPTX </td>
        <td> Occasion </td>
        <td> Date </td>
    </tr>
	{% for presentation in site.data.gemc_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
                 {% else %}
                    <td></td>
                {% endif %}

                {% if presentation.key == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.key"  target="_blank"> Keynote </a> </td>
                {% else %}
                    <td></td>
                {% endif %}

                {% if presentation.pptx == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pptx" target="_blank"> PPTX </a> </td>
                {% else %}
                    <td></td>
                {% endif %}

                 {% if presentation.occasion_url == "NA" %}
                    <td>{{presentation.occasion}} </td>
                {% else %}
                     <td> <a href="{{ presentation.occasion_url }}"  target="_blank"> {{presentation.occasion}} </a> </td>
                {% endif %}

            <td> {{presentation.date}} </td>

        </tr>
	{% endfor %}

</table>
<br/><br/><br/>
