---
layout: default
title: "Docker"
permalink: /software/docker
last_updated: "May 15, 2026"
---

<br/> <br/> 

Last updated: {{ page.last_updated }}

<br/>

A collection of Docker images used in my research.

<br/> <br/> 

## Usage:

<br/> 

batch mode: `docker run -it --rm container_name bash`

interactive (browser): `docker run -it --rm -p 8080:8080 container_name`

<br/> 

- If running on macOS, use the additional flag: `--platform linux/amd64`
- To mount a local directory, use the additional flag: `-v /local/path:/container/path`


{% assign groups = "" | split: ' ' %}
{% for container in site.data.docker_containers %}
{% assign groups = groups | push: container.group %}
{% endfor %}
{% assign groups = groups | uniq %}

<br/> <br/> 


{% for group in groups %}

## {{ group }}

<table class="alternate">

{% for container in site.data.docker_containers %}
{% if container.group == group %}
<tr>
        <td style="width: 400px" > <a href="{{ container.hub_link }}"> {{ container.name }} </a></td>
        <td>  {{ container.description }} </td>
</tr>
{% endif %}
{% endfor %}
</table>


<br/><br/>

{% endfor %}

<br/><br/><br/>
