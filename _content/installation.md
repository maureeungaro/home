---
layout: base
title: Installation
gemcv: 3.0beta

tables:
  gemcInstallationTypes:
    headers: [Type, OS, Requirements, GUI]
    rows:
      - [
      "Docker",
      "Linux, Mac",
      "<a href=\"https://www.docker.com\">docker</a><br/> optional: <a href=\"https://www.realvnc.com/en/connect/\">vnc</a>",
      "web browser, <a href=\"https://www.realvnc.com/en/connect/\">vnc</a>"
      ]
---

<table border="1" width="60%" class="table-info">
	<tr>
		{% for header in page.tables.gemcInstallationTypes.headers %}	
		<th>{{ header }}</th>
		{% endfor %}
	</tr>
	{% for row in page.tables.gemcInstallationTypes.rows %}
		<tr>
			{% for item in row %}
				<td> {{ item }} </td>
			{% endfor %}
		</tr>
	{% endfor %}
</table>

<br/>
<br/>

<!--# DMG <a href="https://www.jlab.org/12gev_phys/packages/dmg/gemc-{{ page.gemcv }}.dmg"> <span data-feather="download"></span> </a> -->
<!--After installation use the line below to load the environment. -->
<!-- source /Applications/gemc-{{ page.gemcv }}.app/environment.sh-->
<!---->

<br/>
<br/>

# Docker 

Pull the latest image:
> docker pull jeffersonlab/gemc:3.0 

It is recommended to mount a working directory to save store your work.
From here on we refer to it as `~/mywork`.

#### run docker in batch mode[^1]:
> docker run -it \-\-rm  -v ~/mywork:/jlab/work/mywork jeffersonlab/gemc:3.0 bash

<br/>

#### run docker and use a browser for the graphical interface:
> docker run -it \-\-rm  -v ~/mywork:/jlab/work/mywork  -p 127.0.0.1:6080:6080  jeffersonlab/gemc:3.0 

<br/>

#### run docker and use vnc[^2] for the graphical interface:
> docker run -it \-\-rm  -v ~/mywork:/jlab/work/mywork  -p 127.0.0.1:6080:6080  -p 5901:5901 jeffersonlab/gemc:3.0 

<br/>

<br/> <br/> <br/> <br/>


[^1]: on linux permissions problems for /var/run/docker.sock may be solved with  ```sudo chmod 666 /var/run/docker.sock```
[^2]: recommended: <a href='https://www.realvnc.com/en/connect/download/viewer/'>realvnc vnc viewer</a>
