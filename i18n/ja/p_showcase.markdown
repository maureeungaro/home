---
layout: default
title: Research & Talks
description: Selected papers, talks, tutorials, and technical notes on Geant4, GEMC, CLAS12 simulations, detector work, and nucleon-structure research.
permalink: /showcase/
p_baseurl: "https://userweb.jlab.org/~ungaro/slides/"
pub_baseurl: "https://userweb.jlab.org/~ungaro/pubs/"
lang: ja
human_reviewed: false
---

<br/>

# 最近の講演とノート

Geant4、GEMC、CLAS12 シミュレーション、検出器研究に関する最近のセミナー、チュートリアル、技術ノート、共同研究の最新情報。

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 発表の場 </td>
		<td> 日付 </td>
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

# 主な論文

私のシミュレーション、検出器、中間子電気生成の研究に関連する代表的な論文。

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 掲載誌 </td>
	</tr>
	{% for paper in site.data.selected_papers %}
		<tr>
            <td> <a href="{{ paper.inspire }}"> {{ paper.title }}</a> </td>
            <td> <a href="{{ paper.pdf }}"> PDF </a> </td>
            <td> {{ paper.journal }} </td>
        </tr>
	{% endfor %}
</table>


すべての研究論文は [Maurizio Ungaro の INSPIRE プロフィール](https://inspirehep.net/authors/1322331){:target="_blank"} に掲載されています。

<br/><br/>

# 中間子電気生成に関する発表

主な発表:

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 発表の場 </td>
		<td> 日付 </td>
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

すべての中間子電気生成に関する発表は [中間子電気生成に関する講演](/home/showcase/meson) に掲載されています。

<br/><br/>

# 低閾値チェレンコフカウンター (LTCC)

LTCC の運用、較正、検出器性能に関連する主な講演。

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 発表の場 </td>
		<td> 日付 </td>
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

すべての LTCC に関する発表は [低閾値チェレンコフカウンターの講演](/home/showcase/ltcc) に掲載されています。

<br/><br/>

# Geant4

JLab および関連ワークショップでの Geant4 ユーザー向けの主なチュートリアルと発表。

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 発表の場 </td>
		<td> 日付 </td>
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

すべての Geant4 に関する発表は [Geant4 の講演とチュートリアル](/home/showcase/geant4) に掲載されています。

<br/><br/>

# GEMC

GEMC、CLAS12 シミュレーション、データベース駆動のシミュレーションワークフローに関する主な講演。

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 発表の場 </td>
		<td> 日付 </td>
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

すべての GEMC に関する発表は [GEMC の講演とプレゼンテーション](/home/showcase/gemc) に掲載されています。

<br/><br/>

# Open Science Grid

CLAS12 シミュレーションワークフローと分散コンピューティングリソースに関する発表。

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 発表の場 </td>
		<td> 日付 </td>
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

# 主な CLAS/CLAS12 技術ノート

CLAS および CLAS12 の検出器・シミュレーション研究に関する主な技術ノート。

<table class="alternate">
	<tr>
		<td> タイトル </td>
		<td> PDF </td>
		<td> 日付 </td>
	</tr>	

	{% for note in site.data.selected_notes %}
        <tr>
            <td> {{ note.title }} </td>

            {% if note.source == "soon" %}
                <td> 近日公開 </td>
            {% else %}
                <td> <a href="{{ note.pdf }}"  target="_blank"> PDF </a> </td>
			{% endif %}

            <td> {{ note.year }} </td>


        </tr>
	{% endfor %}
</table>


すべての CLAS および CLAS12 技術ノートは [CLAS および CLAS12 技術ノート](/home/showcase/clas_notes) に掲載されています。
