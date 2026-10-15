---
layout: default
title: "研究与报告"
description: Selected papers, talks, tutorials, and technical notes on Geant4, GEMC, CLAS12 simulations, detector work, and nucleon-structure research.
permalink: /showcase/
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
pub_baseurl: "https://userweb.jlab.org/~ungaro/pubs/"
lang: zh
human_reviewed: false
---

<br/>

# 近期报告与笔记

涵盖 Geant4、GEMC、CLAS12 模拟和探测器工作的近期研讨会、教程、技术笔记及合作组动态。

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 活动 </td>
		<td> 日期 </td>
	</tr>

	{% for presentation in site.data.recent_and_upcoming_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
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
<br/><br/>

# 精选论文

与我的模拟、探测器及介子电产生研究相关的代表性论文。

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 期刊 </td>
	</tr>
	{% for paper in site.data.selected_papers %}
		<tr>
            <td> <a href="{{ paper.inspire }}"> {{ paper.title }}</a> </td>
            <td> <a href="{{ paper.pdf }}"> PDF </a> </td>
            <td> {{ paper.journal }} </td>
        </tr>
	{% endfor %}
</table>


所有研究论文均列于 [Maurizio Ungaro 的 INSPIRE 主页](https://inspirehep.net/authors/1322331){:target="_blank"}。

<br/><br/>

# 介子电产生报告

精选报告：

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 活动 </td>
		<td> 日期 </td>
	</tr>
	{% for presentation in site.data.meson_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf" target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"          target="_blank"> PDF </a> </td>
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

所有介子电产生报告均列于 [介子电产生报告](/home/showcase/meson)。

<br/><br/>

# 低阈值切伦科夫计数器（LTCC）

与 LTCC 运行、刻度和探测器性能相关的精选报告。

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 活动 </td>
		<td> 日期 </td>
	</tr>	
	{% for presentation in site.data.ltcc_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
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

所有 LTCC 报告均列于 [低阈值切伦科夫计数器报告](/home/showcase/ltcc)。

<br/><br/>

# Geant4

面向 JLab 的 Geant4 用户及相关研讨会参与者的精选教程与报告。

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 活动 </td>
		<td> 日期 </td>
	</tr>	
	{% for presentation in site.data.geant4_selected_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
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

所有 Geant4 报告均列于 [Geant4 报告与教程](/home/showcase/geant4)。

<br/><br/>

# GEMC

关于 GEMC、CLAS12 模拟及数据库驱动的模拟工作流的精选报告。

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 活动 </td>
		<td> 日期 </td>
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


                 {% if presentation.occasion_url == "NA" %}
                    <td>{{presentation.occasion}} </td>
                {% else %}
                     <td> <a href="{{ presentation.occasion_url }}"  target="_blank"> {{presentation.occasion}} </a> </td>
                {% endif %}

            <td> {{presentation.date}} </td>

        </tr>
	{% endfor %}

</table>

所有 GEMC 报告均列于 [GEMC 讲座与报告](/home/showcase/gemc)。

<br/><br/>

# 开放科学网格（Open Science Grid）

关于 CLAS12 模拟工作流与分布式计算资源的报告。

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 活动 </td>
		<td> 日期 </td>
	</tr>	
	{% for presentation in site.data.osg_presentations %}
		<tr>
            <td> {{ presentation.title }} </td>

                {% if presentation.pdf == "yes" %}
                    <td> <a href="{{ page.p_baseurl }}/{{presentation.filename}}.pdf"  target="_blank"> PDF </a> </td>
                {% elsif presentation.pdf == "no_animation" %}
                    <td> <a href="{{ page.p_baseurl }}/no_pdf_animation.pdf"           target="_blank"> PDF </a> </td>
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


<br/><br/>

# 精选 CLAS/CLAS12 技术笔记

用于 CLAS 和 CLAS12 探测器及模拟工作的精选技术笔记。

<table class="alternate">
	<tr>
		<td> 标题 </td>
		<td> PDF </td>
		<td> 日期 </td>
	</tr>	

	{% for note in site.data.selected_notes %}
        <tr>
            <td> {{ note.title }} </td>

            {% if note.source == "soon" %}
                <td> 即将发布 </td>
            {% else %}
                <td> <a href="{{ note.pdf }}"  target="_blank"> PDF </a> </td>
			{% endif %}

            <td> {{ note.year }} </td>


        </tr>
	{% endfor %}
</table>


所有 CLAS 和 CLAS12 技术笔记均列于 [CLAS 与 CLAS12 技术笔记](/home/showcase/clas_notes)。
