---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# See https://github.com/jekyll/minima#readme

# Table: add first row (3 |) for autoformatting

layout: default
title: Maurizio Ungaro
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

lang: ja
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
src="assets/images/home/mauri.png"
alt="Portrait of Maurizio Ungaro"
width="170"
%}

<div style="text-align: center">
<h2>Maurizio Ungaro</h2> 
<p>原子核物理学者・シミュレーションソフトウェア開発者</p>
</div>

|                     `Staff Scientist`                      |
|:----------------------------------------------------------:|
|        [ジェファーソン研究所](https://www.jlab.org)        |
| [実験ホール B](https://www.jlab.org/physics/hall-b) |

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

## 自己紹介

私は [ジェファーソン研究所](https://www.jlab.org) の [Hall-B](https://www.jlab.org/physics/hall-b)
に所属するスタッフ研究員、Maurizio（Mauri）Ungaro です。原子核物理、検出器システム、シミュレーションソフトウェアに取り組んでいます。

現在は、GEMC を用いた Geant4 ベースのシミュレーション、Open Science Grid 上での
CLAS12 シミュレーションの大量生成ワークフロー、CLAS12 低閾値チェレンコフ検出器の
運用・較正・性能評価に取り組んでいます。研究では、中間子電気生成を通じて核子構造を探究しています。

ここでは、共同研究者や学生に向けたソフトウェア、講演、技術ノート、実践的な例を紹介しています。

余暇には、自分よりずっと速く滑る我が子の姿を楽しみながら、ホッケーを習っています。

<table class="zebra compact-table">
  <tr>
    <th>主なリンク</th>
    <td><a href="/home/profile/">プロフィール</a></td>
    <td><a href="https://gemc.github.io/home/">GEMC</a></td>
    <td><a href="/home/showcase/">研究と講演</a></td>
    <td><a href="/home/mynotes/">ノート</a></td>
  </tr>
</table>

共同研究や、シミュレーション・検出器関連の支援については、[メールでご連絡ください](mailto:ungaro@jlab.org)。
以下のプロフィールから、私の論文やコードもご覧いただけます。
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
    <td><a href="{{ email_link }}"><img src="{{ email_img }}" alt="Email"></a><br/><a href="{{ email_link }}">メール</a></td>
  </tr>
</table>

<br/><br/>

## 最新ニュースと今後の取り組み

<table class="alternate">
  <thead>
    <tr><th scope="col">ニュース</th><th scope="col">日付 / 状況</th></tr>
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

公開予定の CLAS12 ノートでは、simGrid OSG フレームワークについて、アーキテクチャと
ジョブワークフローの図を交えて解説します。ノートが公開されるまでは、
ニュースのリンク先は [OSG 上での CLAS12 の概要]({{ '/osg/osg' | relative_url }}) です。

<br/>

## はじめに

| お探しの内容                                 | 最初にご覧いただくページ                                 |
|:---------------------------------------------|:---------------------------------------------------------|
| 略歴、CV、履歴書、専門活動に関するリンク       | [プロフィール](/home/profile/)                           |
| Geant4 の例、チュートリアル、JLab でのサポート | [JLab における Geant4](https://jeffersonlab.github.io/g4home/) |
| GEMC シミュレーションワークフロー             | [GEMC](https://gemc.github.io/home/)                     |
| CLAS12 シミュレーションのリリース             | [CLAS12 シミュレーション](https://github.com/gemc/clas12Tags) |
| 分散環境でのシミュレーションの大量生成       | [OSG 上での CLAS12](/home/osg/osg)                       |
| 研究講演、論文、技術ノート                    | [研究と講演](/home/showcase/)                            |
| 実践的なコンピューティングノート              | [ノート](/home/mynotes/)                                 |

<br/><br/>

## 取り組んでいる分野

- **原子核物理:** 核子構造、共鳴領域の解析、ハドロン描像とパートン描像の間の遷移。
  [N → Δ (1232) 遷移](/home/meson/pi0_delta/pi0_delta) や
  [高 Q<sup>2</sup> における中間子電気生成](/home/meson/pi0_resonance/pi0_resonance) を含みます。
- **検出器システム:** 運用、保守、較正、性能評価。対象は
  [CLAS12 低閾値チェレンコフ検出器](/home/ltcc/ltcc) です。
- **シミュレーションソフトウェア:** [GEMC および GEMC3](https://gemc.github.io/home/)、
  [CLAS12 シミュレーション](https://github.com/gemc/clas12Tags)、
  [Open Science Grid 上での大量生成ワークフロー](/home/osg/osg) の開発。
- **科学計算とサポート:** [JLab における Geant4](https://jeffersonlab.github.io/g4home/)、
  再現可能なシミュレーションワークフロー、チュートリアル、例、ユーザー向けドキュメント。

<br/>

## 最近および今後の講演とノート

<br/>

<table class="alternate">

	<tr>
		<th scope="col">タイトル</th>
		<th scope="col">PDF</th>
		<th scope="col">イベント</th>
		<th scope="col">日付</th>
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

その他の講演、論文、ノートは [研究と講演](/home/showcase/) に掲載しています。

<br/>

## 技術スキル

| 分野                           | ツールと経験                                                                                                                  |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| シミュレーションと解析          | Geant4、GEMC、CLAS12 シミュレーション、ROOT、検出器ジオメトリ、イベント生成、デジタイゼーションワークフロー                      |
| プログラミングとインフラ        | C++、Python、シェルスクリプト、Git、GitHub、継続的インテグレーション、Docker、Environment Modules、HTCondor、Meson、CMake、SCons |
| 科学コミュニケーション          | LaTeX、Markdown、HTML、CSS、JavaScript、Highcharts、技術ドキュメント、チュートリアル、プレゼンテーション                         |
| 言語                           | 英語、イタリア語                                                                                                              |

<br/>

{% capture left2 %}

## 関心分野

<div class="no-bullets-list">
  {{ page.interest | markdownify }}
</div>

{% endcapture %}

{% capture right2 %}

## 職歴と学歴

<br/>

<div class="no-bullets-list">

{{ page.education | markdownify }}
</div>

{% endcapture %}

{% include two_col_md.html left="40%" right="60%" left_content=left2 right_content=right2 %}

<br/>

## ギャラリー

<link type="text/css" rel="stylesheet" href="/home/assets/lightslider.css" />
<script src="/home/assets/jq.js"></script>
<script src="/home/assets/lightslider.js"></script>

<div>
	<br/>

	<ul style="text-align:center"  id="light-slider" >
    	<li data-thumb="assets/images/empty.png">
			<img src="assets/images/home/quote1.png" alt="Quote" height="500px" width="90%"/><br/><br/><br/>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/software/charts">CSV グラフ表示ツール<br/><img src="assets/images/software/charts_big.png" alt="Chart CSV displayer screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/meson/pi0_delta/pi0_delta">N → Δ(1232) 遷移 <br/><img src="assets/images/pi0/pi0_delta_results.png" alt="N to Delta transition results" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="/home/wfd/">What's For Dinner 献立プランナー<br/><img src="assets/images/home/wfd.png" alt="What's For Dinner meal planner screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="https://gemc.github.io/home/">GEMC ホームページ<br/><img src="assets/images/home/gemc_home.png" alt="GEMC home page screenshot" height="500px" width="90%"/></a>
    	</li>
    	<li data-thumb="assets/images/empty.png">
			<a href="https://gemc.jlab.org/web_interface/index.php">GEMC シミュレーション用 Web インターフェース<br/><img src="assets/images/home/osg.png" alt="GEMC simulation web interface screenshot" height="500px" width="90%"/></a>
    	</li>
	</ul>

</div>


<br/><br/><br/>

{:.zebra}

| ホームページのデプロイ | [![CI][CI-badge]][CI]  |


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


[code]: assets/images/home/code.png

[software]: assets/images/home/software.png

[languages]: assets/images/home/languages.png

[quote1]: assets/images/home/quote1.png
