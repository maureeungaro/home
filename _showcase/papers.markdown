---
layout: default
title: Mauri's Papers
datatable: true 
---

Check [jquery tables](https://idratherbewriting.com/documentation-theme-jekyll/mydoc_tables.html) and its [datatables](https://www.datatables.net) to check if it's feasible

<div class="datatable-begin"></div>

Food    | Description                           | Category | Sample type
------- | ------------------------------------- | -------- | -----------
Apples  | A small, somewhat round ...           | Fruit    | Fuji
Bananas | A long and curved, often-yellow ...   | Fruit    | Snow
Kiwis   | A small, hairy-skinned sweet ...      | Fruit    | Golden
Oranges | A spherical, orange-colored sweet ... | Fruit    | Navel

<div class="datatable-end"></div>

<table>
 
   <tr>
        <th>Title</th>
        <th>pdf</th>
        <th>ePrint</th>
        <th>Collaboration</th>
        <th>Journal</th>
   </tr>   

	{% for paper in site.data.selected_papers %}
		<tr>
            <td> {{ paper.title }} </td>
            <td> <a href="{{ paper.pdf }}"> pdf </a> </td>
            <td> <a href="{{ paper.eprint }}"> ePrint </a> </td>
            <td> {{paper.collaboration}} </td>
            <td> <a href="{{ paper.journalurl }}"> {{ paper.journal }} </a> </td>
        </tr>
	{% endfor %}
</table>
