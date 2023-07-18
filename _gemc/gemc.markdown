---
layout: default
title: "GEMC"
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
---

<br/>

# GEMC Simulation Framework

GEMC (**GE**ant **M**onte-**C**arlo) is a database-driven Monte Carlo simulation program based on Geant4.<br/>

The goal is have a turn-key program that allows
to create and run realistic setups w/o programming knowledge, in particular:
- No need to write/compile the code
- No need to know C++ or Geant4
- Automatic handling of multi-threads handling of events and hit collection
- Pre-defined digitization such as `flux` and `dosimeter`
- Built-in `text` and `ROOT` output


## [Homepage](https://gemc.github.io/home/)


<br/>

<div class="colored_band">

<br/><br/><br/>

<p style="text-align:center">
<span style="color:#444;font-weight:300;font-size:54px">Selected talks</span>
</p>

<br/><br/>
<table class="alternate">
	{% for presentation in site.data.gemc_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> pdf </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> pdf </a> </td>
                 {% else %}
                    <td> na </td>
                {% endif %}

                {% if presentation.key == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.key"  target="_blank"> key </a> </td>
                {% else %}
                    <td> na </td>
                {% endif %}

                {% if presentation.pptx == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pptx" target="_blank"> ppt </a> </td>
                {% else %}
                    <td> na </td>
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
</div>

