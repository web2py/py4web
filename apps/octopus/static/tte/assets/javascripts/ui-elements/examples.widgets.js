

(function( $ ) {

	'use strict';

	$(function() {

		/*
		Flot
		*/
		var plot = $.plot('#flotWidgetsSales1', flotWidgetsSales1Data, {
			series: {
				lines: {
					show: true,
					lineWidth: 2
				},
				points: {
					show: true
				},
				shadowSize: 0
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: 'transparent',
				borderWidth: 1,
				labelMargin: 15,
				backgroundColor: 'transparent'
			},
			yaxis: {
				min: 0,
				color: 'transparent'
			},
			xaxis: {
				mode: 'categories',
				color: 'transparent'
			},
			legend: {
				show: false
			},
			tooltip: true,
			tooltipOpts: {
				content: '%x: %y',
				shifts: {
					x: -30,
					y: 25
				},
				defaultTheme: false
			}
		});

		/*
		Morris
		*/
		Morris.Line({
			resize: true,
			element: 'morrisLine',
			data: morrisLineData,
			grid: false,
			xkey: 'y',
			ykeys: ['a'],
			labels: ['Series A'],
			hideHover: 'always',
			lineColors: ['#FFF'],
			gridTextColor: 'rgba(255,255,255,0.4)'
		});

		/*
		Sparkline: Bar
		*/
		$("#sparklineBar").sparkline(sparklineBarData, {
			type: 'bar',
			width: '80',
			height: '50',
			barColor: '#0088cc',
			negBarColor: '#B20000'
		});

		$('.circular-bar-chart').appear();

	});

}).apply(this, [ jQuery ]);