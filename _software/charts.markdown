---
layout: default
title: "Charts"
permalink: /software/charts
---

Select or drag and drop a csv file in the button below.

This page load the csv and plot all the data in the chart on top, and the individual variables (up to 10) in the plots below.

<br/>

<script src="/home/assets/jq.js"></script>
<script src="/home/assets/hchart.js"></script>

<div>
    <input type="file" accept=".csv" onchange="readCSVFile()"  onload="readCSVFile()"/>
    <p class="content"></p>

	
	Only for the individual plots:<br/>
	<button onclick="switch_average_on_off(); readCSVFile();"> Switch Average ON/OFF</button> 


</div>

<br/><br/>


<h1> All Data in one plots</h1>
<div id="container" style="min-width: 310px; height: 600px; margin: 0 auto"> </div><br/>
<h1 id="individual"> </h1>
<div id="container1" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container2" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container3" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container4" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container5" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container6" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container7" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container8" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container9" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>
<div id="container10" style="min-width: 310px; height: 400px; margin: 0 auto"> </div><br/>

<script type="text/javascript">

function readCSVFile() {

	const content = document.querySelector(".content");
	const [file] = document.querySelector("input[type=file]").files;
	const reader = new FileReader();

	// fill id = "individual" with the titles of the plots

	for ( var i = 1; i < 11; i++) {
		container = "#container" + i;
		// hide container
		$(container).hide();
	}

	reader.addEventListener(
		"load",
		() => {
			// reader.result is not null here
			numbers_of_plots = countPlots(reader.result);
			titles = plot_titles(reader.result);
			xdata = plot_data_for_column(0, reader.result);

			update(titles, reader.result);

			// run addDataToChart for each plot
			for (var i = 0; i < numbers_of_plots; i++) {
				ydata = plot_data_for_column(i+1, reader.result);
				addDataToChart( i+1, titles[i], xdata, ydata);
			}
		},
		false,
	);

	if (file) {
		reader.readAsText(file);
		document.getElementById("individual").innerHTML = "Individual plots " ;
	}

}

var average = -999;
var fit = -999;

function switch_average_on_off() {
	if (average == -999) {
		average = 999;
	} else {
		average = -999;
	}
}

function switch_fit_on_off() {
	if (fit == -999) {
		fit = 999;
	} else {
		fit = -999;
	}
}


function calculate_average(data) {

	avrg = 0;
	for (var i = 0; i < data.length-1; i++) {
//alert(data[i]);
		avrg += parseFloat(data[i]);
	}
	avrg = avrg / data.length;
	return avrg;
	
}

function countPlots(data) {
	if (data == null) {
		return "No data";
	}
	var lines = data.split('\n');
	var columns = lines[0].split(',');
	return columns.length - 1;
}

function plot_titles(data) {
	if (data == null) {
		return "No data";
	}
	var lines = data.split('\n');
	var columns = lines[0].split(',').slice(1);
	return columns;
}

function plot_data_for_column(column, data) {
	if (data == null) {
		return "No data";
	}
	// remove dollar sign from data
	data = data.replace(/\$/g, '');

	var lines = data.split('\n');
	var column_data = [];
	for (var i = 0; i < lines.length; i++) {
		var line = lines[i].split(',');

		column_data.push(line[column]);
	}


	// if column is 0, return column_data;
	if (column == 0) {
		return column_data;
	} else {
		return column_data.slice(1);
	}

}

function calculate_regression_parameters(ydata) {

	var xsum = 0;
    var ysum = 0;

	var size = ydata.length - 1;

    for (var i = 0; i <size; i ++) {
        xsum += parseFloat(i);
        ysum += parseFloat(ydata[i]);
    }

    var xmean = xsum / size;
    var ymean = ysum / size;
 
    var num = 0;
    var denom = 0;

    for (var i = 0; i < size; i ++) {
        var x = parseFloat(i);
        var y = parseFloat(ydata[i]);
        num += (x - xmean) * (y - ymean);
        denom += (x - xmean) * (x - xmean);
    }

    m = num / denom;
    b = ymean - (m * xmean);

	return [m, b];

}

function addDataToChart(cid, title, xdata, ydata) {
	
	container = "#container" + cid;

	average_value = average;

	// calculate average if average is not -999
	if (average != -999) {
		average_value = calculate_average(ydata);
	}

	// xdata starts with a comma for some reason
	var row = [];
	for (i = 1; i <xdata.length; i++) {
		row.push(xdata[i]);
	}

 	
	// remove all series first
	$(container).show();

    $(container).highcharts ({

        title: {
                text: title,
                x: -20 // center
            },

            xAxis: {
                categories: row
            },

            yAxis: {
                title: {
                    text: ''
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                },
				{
      			  	color: 'red',
        			value: average_value, // Insert your average here
        			width: '1',
        			zIndex: 4 // To not get stuck below the regular plot lines or series
    			}]
            },
            series: [ {
                name: title,
                data: ydata.map(Number)
            }]
        });
}


function update(title, data) {

 	var seriesLength = chart.series.length;
	for(var i = seriesLength - 1; i > -1; i--) { 
		chart.series[i].remove();
	}

	// colors is an array size 10 
	var colors = ['black',  'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray'];

	chart.setTitle({text: 'All Data in one plots'});
	chart.setSubtitle({text: ''});
    chart.yAxis[0].setTitle({text: ''});

	numbers_of_plots = countPlots(data);

	for (var p = 0; p < numbers_of_plots; p++) {

		column_data = plot_data_for_column(p+1, data);

		// Create a new series row
		var row = [];
		for (i = 0; i <column_data.length-1; i++) {
			row.push(parseFloat(column_data[i]));
		}

		pars = calculate_regression_parameters(row);
		var size = row.length ;
		first_point = pars[0] * 0 + pars[1];
		last_point  = pars[0] * (size-1) + pars[1];
		//alert(first_point + "        " + last_point);

		// Append new series to the chart
		chart.addSeries( { name:title[p], data:row, color: colors[p] } );
		
		chart.addSeries(
						{ type: 'line', name: title + ' fit', data: [[0, first_point], [size-1, last_point]], color: colors[p]}
						);
	}
}

var chart = null;


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

tokyo = [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6];
newyork = [1.9, 2.2, 3.7, 6.5, 9.9, 13.2, 15.0, 14.6, 12.2, 8.3, 4.6, 2.8];
berlin = [-0.9, 1.2, 2.7, 5.5, 8.9, 12.2, 14.0, 13.6, 11.2, 7.3, 3.6, 1.8];
london = [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8];

chart = Highcharts.chart('container', {
    title: {
        text: 'Monthly Average Temperature',
        x: -20 //center
    },
    subtitle: {
        text: 'Source: WorldClimate.com',
        x: -20
    },
    xAxis: {
        categories: months
    },
    yAxis: {
        title: {
            text: 'Temperature (°C)'
        },
        plotLines: [{
            value: 0,
            width: 1,
            color: '#808080'
        }]
    },
    tooltip: {
        valueSuffix: '°C'
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle',
        borderWidth: 0
    },
    series: [{
        name: 'Tokyo',
        data: tokyo
    }, {
        name: 'New York',
        data: newyork
    }, {
        name: 'Berlin',
        data: berlin
    }, {
        name: 'London',
        data: london
    }]
});





</script>
