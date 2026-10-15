---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# See https://github.com/jekyll/minima#readme

# Table: add first row (3 |) for autoformatting

layout: default
permalink: /
title: "Maurizio Ungaro"
description: >-
  Nuclear physicist and simulation software developer at Jefferson Lab working on Geant4, GEMC,
  CLAS12 detector systems, nucleon structure, and scientific computing workflows.
image: /assets/images/home/mauri.png
nav_exclude: true

interest: |
  - ▸ Quark Structure
  - ▸ Monte Carlo Simulations
  - ▸ Large Language Models
  - ▸ Data Analysis
  - ▸ Geant4
  - ▸ Cherenkov Counters
  - ▸ Software Development

education: |
  - <span class="large-emoji">🔬</span> **Staff Scientist**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Jefferson Laboratory](https://www.jlab.org), VA, USA, 2011-present <br/><br/>

  - <span class="large-emoji">🎓 🔬</span>  **Postdoctoral Researcher and Research Associate**<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[University of Connecticut](https://uconn.edu), USA, 2004-2011 <br/><br/>

  - <span class="large-emoji">🎓</span>  **Ph.D. in Nuclear Physics**<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Rensselaer Polytechnic Institute](https://www.rpi.edu), Troy, NY, USA, 2003 <br/><br/>

  - <span class="large-emoji">🎓</span>  **Laurea in Fisica**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    [Università degli Studi di Genova](https://unige.it/), Italy, 1999 <br/><br/>

p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"

lang: zh
human_reviewed: false
---

{% assign gscholar_img = '/assets/images/home/gscholar.png' | relative_url %}
{% assign gscholar_link = 'https://scholar.google.com/citations?user=zkWYILYAAAAJ&hl=en' %}
{% assign github_img = '/assets/images/home/github.png' | relative_url %}
{% assign github_link = 'https://github.com/maureeungaro' %}
{% assign inspire_img = '/assets/images/home/inspire.png' | relative_url %}
{% assign inspire_link = 'https://inspirehep.net/authors/1322331' %}
{% assign researchgate_img = '/assets/images/home/researchgate.svg' | relative_url %}
{% assign researchgate_link = 'https://www.researchgate.net/profile/Maurizio-Ungaro' %}
{% assign scopus_img = '/assets/images/home/scopus.svg' | relative_url %}
{% assign scopus_link = 'https://www.scopus.com/authid/detail.uri?authorId=35228099400' %}
{% assign email_img = '/assets/images/home/email.png' | relative_url %}
{% assign email_link = 'mailto:ungaro@jlab.org' %}
{% assign orcid_img = '/assets/images/home/orcid.svg' | relative_url %}
{% assign orcid_link = 'https://orcid.org/0000-0001-6982-3310' %}
{% assign linkedin_img = '/assets/images/home/linkedin.svg' | relative_url %}
{% assign linkedin_link = 'https://www.linkedin.com/in/maurizio-ungaro-37992062/' %}
{% assign physics_img = '/assets/images/home/physics.png' | relative_url %}
{% assign degree_img = '/assets/images/home/degree.png' | relative_url %}

{% capture left %}

{% include figure.html
src="/assets/images/home/mauri.png"
alt="Portrait of Maurizio Ungaro"
width="170"
%}

<div style="text-align: center">
<h2>Maurizio Ungaro</h2> 
<p>核物理学家与仿真软件开发者</p>
</div>

|                     `Staff Scientist`                      |
|:----------------------------------------------------------:|
|        [杰斐逊实验室](https://www.jlab.org)        |
| [B 实验厅](https://www.jlab.org/physics/hall-b) |

[gscholar-img]: {{ gscholar_img }}
[gscholar-link]: {{ gscholar_link }}
[github-img]: {{ github_img }}
[github-link]: {{ github_link }}
[inspire-img]: {{ inspire_img }}
[inspire-link]: {{ inspire_link }}
[researchgate-img]: {{ researchgate_img }}
[researchgate-link]: {{ researchgate_link }}
[scopus-img]: {{ scopus_img }}
[scopus-link]: {{ scopus_link }}
[email-img]: {{ email_img }}
[email-link]: {{ email_link }}
[orcid-img]: {{ orcid_img }}
[orcid-link]: {{ orcid_link }}
[linkedin-img]: {{ linkedin_img }}
[linkedin-link]: {{ linkedin_link }}

{% endcapture %}

{% capture right %}

<br/>

## 关于我

我是 Maurizio（Mauri）Ungaro，在[杰斐逊实验室](https://www.jlab.org)的
[B 实验厅](https://www.jlab.org/physics/hall-b)担任专职科研人员。我的工作涉及核物理、探测器系统和仿真软件。

我目前的工作包括使用 GEMC 进行基于 Geant4 的仿真、在
开放科学网格（Open Science Grid）上开展 CLAS12 仿真生产工作流，以及 CLAS12 低阈值
切伦科夫计数器的运行、标定和性能研究。我的研究通过介子电致产生探索核子结构。

在这里，你可以找到面向合作者和学生的软件、报告、技术说明和实用示例。

闲暇时，我正在学习打冰球，也很享受看着我的孩子在冰上滑得比我快得多。

<table class="zebra compact-table">
  <tr>
    <th>主要链接</th>
    <td><a href="/home/profile/">个人简介</a></td>
    <td><a href="https://gemc.github.io/home/">GEMC</a></td>
    <td><a href="/home/showcase/">研究与报告</a></td>
    <td><a href="/home/mynotes/">笔记</a></td>
  </tr>
</table>

如需合作，或在仿真和探测器工作方面需要帮助，请[给我发邮件](mailto:ungaro@jlab.org)。
你也可以通过下面的各个主页找到我的论文和代码。
<br/>
<br/>

{% endcapture %}

{% include two_col_md.html left="30%" right="70%" left_content=left right_content=right %}

<br/>


<table class="small-icons">
  <tr>
    <td><a href="{{ gscholar_link }}"><img src="{{ gscholar_img }}" alt="Google Scholar"></a><br/><a href="{{ gscholar_link }}">Google Scholar</a></td>
    <td><a href="{{ inspire_link }}"><img src="{{ inspire_img }}" alt="INSPIRE"></a><br/><a href="{{ inspire_link }}">INSPIRE</a></td>
    <td>
      <a href="{{ scopus_link }}"><img src="{{ scopus_img }}" alt="Scopus"></a><br/>
      <a href="{{ scopus_link }}">Scopus</a>
    </td>
    <td>
      <a href="{{ researchgate_link }}"><img src="{{ researchgate_img }}" alt="ResearchGate"></a><br/>
      <a href="{{ researchgate_link }}">ResearchGate</a>
    </td>
    <td><a href="{{ github_link }}"><img src="{{ github_img }}" alt="GitHub"></a><br/><a href="{{ github_link }}">GitHub</a></td>
    <td><a href="{{ orcid_link }}"><img src="{{ orcid_img }}" alt="ORCID"></a><br/><a href="{{ orcid_link }}">ORCID</a></td>
    <td><a href="{{ linkedin_link }}"><img src="{{ linkedin_img }}" alt="LinkedIn"></a><br/><a href="{{ linkedin_link }}">LinkedIn</a></td>
    <td><a href="{{ email_link }}"><img src="{{ email_img }}" alt="Email"></a><br/><a href="{{ email_link }}">电子邮件</a></td>
  </tr>
</table>

<br/><br/>

## 最新动态与即将开展的工作

<table class="alternate">
  <thead>
    <tr><th scope="col">动态</th><th scope="col">日期 / 状态</th></tr>
  </thead>
  <tbody>
    {% for news in site.data.news %}
    <tr>
      <td>
        <a href="{{ news.link }}">
          <img src="{{ news.image }}" alt="" width="100"> {{ news.title }}
        </a>
      </td>
      <td>{{ news.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

即将发布的 CLAS12 技术说明介绍了 simGrid OSG 框架，并附有其架构
和作业工作流的示意图。在该技术说明发布之前，
该动态链接指向 [CLAS12 在 OSG 上的运行概览]({{ '/osg/osg' | relative_url }})。

<br/>

## 从这里开始

| 如果你正在寻找……                             | 请从这里开始                                             |
|:---------------------------------------------|:---------------------------------------------------------|
| 个人简介、学术简历、求职简历或专业主页链接 | [个人简介](/home/profile/)                                |
| Geant4 示例、教程或 JLab 支持  | [JLab 的 Geant4 资源](https://jeffersonlab.github.io/g4home/) |
| GEMC 仿真工作流                    | [GEMC](https://gemc.github.io/home/)                     |
| CLAS12 仿真发行版                   | [CLAS12 仿真](https://github.com/gemc/clas12Tags) |
| 分布式仿真生产            | [CLAS12 在 OSG 上的运行](/home/osg/osg)                           |
| 研究报告、论文和技术说明  | [研究与报告](/home/showcase/)                      |
| 实用计算笔记                    | [笔记](/home/mynotes/)                                  |

<br/><br/>

## 我的工作内容

- **核物理：** 核子结构、共振区分析，以及强子描述与部分子描述之间的过渡，包括
  [N → Δ (1232) 跃迁](/home/meson/pi0_delta/pi0_delta)
  和[高 Q<sup>2</sup> 下的介子电致产生](/home/meson/pi0_resonance/pi0_resonance)。
- **探测器系统：** 运行、维护、标定和性能研究，研究对象为
  [CLAS12 低阈值切伦科夫计数器](/home/ltcc/ltcc)。
- **仿真软件：** 开发 [GEMC 和 GEMC3](https://gemc.github.io/home/)、
  [CLAS12 仿真](https://github.com/gemc/clas12Tags)，以及
  [开放科学网格（Open Science Grid）仿真生产工作流](/home/osg/osg)。
- **科学计算与支持：** [JLab 的 Geant4 资源](https://jeffersonlab.github.io/g4home/)、
  可复现的仿真工作流、教程、示例以及面向用户的文档。

<br/>

## 近期及即将推出的报告与技术说明

<br/>

<table class="alternate">

	<tr>
		<th scope="col">标题</th>
		<th scope="col">PDF</th>
		<th scope="col">场合</th>
		<th scope="col">日期</th>
	</tr>	

	{% for presentation in site.data.recent_and_upcoming_presentations limit: 6 %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td>
                      <a href="{{ page.p_baseurl }}{{ presentation.filename }}.pdf" target="_blank">PDF</a>
                    </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td>
                      <a href="{{ page.p_baseurl }}no_pdf_animation.pdf" target="_blank">PDF</a>
                    </td>
                 {% else %}
                    <td>  </td>
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

更多报告、论文和技术说明请参见[研究与报告](/home/showcase/)。

<br/>

## 技术技能

| 领域                           | 工具与经验                                                                                                          |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| 仿真与分析        | Geant4、GEMC、CLAS12 仿真、ROOT、探测器几何、事件生成、数字化工作流                           |
| 编程与基础设施 | C++、Python、shell 脚本、Git、GitHub、持续集成、Docker、Environment Modules、HTCondor、Meson、CMake、SCons |
| 科学交流       | LaTeX、Markdown、HTML、CSS、JavaScript、Highcharts、技术文档、教程、演示报告                         |
| 语言                      | 英语、意大利语                                                                                                              |

<br/>

{% capture left2 %}

## 兴趣

<div class="no-bullets-list">
  {{ page.interest | markdownify }}
</div>

{% endcapture %}

{% capture right2 %}

## 工作经历与教育背景

<br/>

<div class="no-bullets-list">

{{ page.education | markdownify }}
</div>

{% endcapture %}

{% include two_col_md.html left="40%" right="60%" left_content=left2 right_content=right2 %}

<br/>

## 画廊

<link type="text/css" rel="stylesheet" href="/home/assets/lightslider.css" />
<script src="/home/assets/jq.js"></script>
<script src="/home/assets/lightslider.js"></script>

<div>
	<br/>

	<ul style="text-align:center"  id="light-slider" >
    	<li data-thumb="/home/assets/images/empty.png">
			<img src="/home/assets/images/home/quote1.png" alt="Quote" height="500px" width="90%"/><br/><br/><br/>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="/home/software/charts">CSV 图表显示工具<br/><img src="/home/assets/images/software/charts_big.png" alt="Chart CSV displayer screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="/home/meson/pi0_delta/pi0_delta">N → Δ(1232) 跃迁 <br/><img src="/home/assets/images/pi0/pi0_delta_results.png" alt="N to Delta transition results" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="/home/wfd/">What's For Dinner 膳食规划工具<br/><img src="/home/assets/images/home/wfd.png" alt="What's For Dinner meal planner screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="https://gemc.github.io/home/">GEMC 主页<br/><img src="/home/assets/images/home/gemc_home.png" alt="GEMC home page screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="/home/assets/images/empty.png">
			<a href="https://gemc.jlab.org/web_interface/index.php">GEMC 仿真 Web 界面<br/><img src="/home/assets/images/home/osg.png" alt="GEMC simulation web interface screenshot" height="500px" width="90%"/></a>
    	</li>
	</ul>

</div>


<br/><br/><br/>

{:.zebra}

| 主页部署 | [![CI][CI-badge]][CI]  |


[CI]: https://github.com/maureeungaro/home/actions/workflows/jekyll.yml
[CI-badge]: https://github.com/maureeungaro/home/actions/workflows/jekyll.yml/badge.svg


<br/><br/><br/>

<script type="text/javascript">
    $(document).ready(function() {
            $('#light-slider').lightSlider({
                gallery:true,
                item:1,
                thumbItem:2,
                slideMargin: 1,
                speed:500,
		        pause: 5000,
                auto:true,
                loop:true,
                onSliderLoad: function() {
                    $('#light-slider').removeClass('cS-hidden');
                }  
		});
});
</script>


[code]: /home/assets/images/home/code.png

[software]: /home/assets/images/home/software.png

[languages]: /home/assets/images/home/languages.png

[quote1]: /home/assets/images/home/quote1.png
