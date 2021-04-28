
(function( $ ) {

	'use strict';

	/*
	Flot: Basic
	*/
	(function() {
		var plot = $.plot('#flotBasic', flotBasicData, {
			series: {
				lines: {
					show: true,
					fill: true,
					lineWidth: 1,
					fillColor: {
						colors: [{
							opacity: 0.45
						}, {
							opacity: 0.45
						}]
					}
				},
				points: {
					show: true
				},
				shadowSize: 0
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: 'rgba(0,0,0,0.1)',
				borderWidth: 1,
				labelMargin: 15,
				backgroundColor: 'transparent'
			},
			yaxis: {
				min: 0,
				max: 200,
				color: 'rgba(0,0,0,0.1)'
			},
			xaxis: {
				color: 'rgba(0,0,0,0.1)'
			},
			tooltip: true,
			tooltipOpts: {
				content: '%s: Value of %x is %y',
				shifts: {
					x: -60,
					y: 25
				},
				defaultTheme: false
			}
		});
	})();

	/*
	Flot: Real-Time
	*/
	(function() {
		var data = [],
			totalPoints = 300;

		function getRandomData() {

			if (data.length > 0)
				data = data.slice(1);

			// Do a random walk
			while (data.length < totalPoints) {

				var prev = data.length > 0 ? data[data.length - 1] : 50,
					y = prev + Math.random() * 10 - 5;

				if (y < 0) {
					y = 0;
				} else if (y > 100) {
					y = 100;
				}

				data.push(y);
			}

			// Zip the generated y values with the x values
			var res = [];
			for (var i = 0; i < data.length; ++i) {
				res.push([i, data[i]])
			}

			return res;
		}

		var plot = $.plot('#flotRealTime', [getRandomData()], {
			colors: ['#8CC9E8'],
			series: {
				lines: {
					show: true,
					fill: true,
					lineWidth: 1,
					fillColor: {
						colors: [{
							opacity: 0.45
						}, {
							opacity: 0.45
						}]
					}
				},
				points: {
					show: false
				},
				shadowSize: 0
			},
			grid: {
				borderColor: 'rgba(0,0,0,0.1)',
				borderWidth: 1,
				labelMargin: 15,
				backgroundColor: 'transparent'
			},
			yaxis: {
				min: 0,
				max: 100,
				color: 'rgba(0,0,0,0.1)'
			},
			xaxis: {
				show: false
			}
		});

		function update() {

			plot.setData([getRandomData()]);

			// Since the axes don't change, we don't need to call plot.setupGrid()
			plot.draw();
			setTimeout(update, $( 'html' ).hasClass( 'mobile-device' ) ? 1000 : 30 );
		}

		update();
	})();

	/*
	Flot: Bars
	*/
	(function() {
		var plot = $.plot('#flotBars', [flotBarsData], {
			colors: ['#8CC9E8'],
			series: {
				bars: {
					show: true,
					barWidth: 0.8,
					align: 'center'
				}
			},
			xaxis: {
				mode: 'categories',
				tickLength: 0
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: 'rgba(0,0,0,0.1)',
				borderWidth: 1,
				labelMargin: 15,
				backgroundColor: 'transparent'
			},
			tooltip: true,
			tooltipOpts: {
				content: '%y',
				shifts: {
					x: -10,
					y: 20
				},
				defaultTheme: false
			}
		});
	})();

	/*
	Flot: Pie
	*/
	(function() {
		var plot = $.plot('#flotPie', flotPieData, {
			series: {
				pie: {
					show: true,
					combine: {
						color: '#999',
						threshold: 0.1
					}
				}
			},
			legend: {
				show: false
			},
			grid: {
				hoverable: true,
				clickable: true
			}
		});
	})();


	/*
	Morris: Line
	*/
	Morris.Line({
		resize: true,
		element: 'morrisLine',
		data: morrisLineData,
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Series A', 'Series B'],
		hideHover: true,
		lineColors: ['#0088cc', '#734ba9'],
	});

	/*
	Morris: Donut
	*/
	Morris.Donut({
		resize: true,
		element: 'morrisDonut',
		data: morrisDonutData,
		colors: ['#0088cc', '#734ba9', '#E36159']
	});

	/*
	Morris: Bar
	*/
	Morris.Bar({
		resize: true,
		element: 'morrisBar',
		data: morrisBarData,
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Series A', 'Series B'],
		hideHover: true,
		barColors: ['#0088cc', '#2baab1']
	});

	/*
	Morris: Area
	*/
	Morris.Area({
		resize: true,
		element: 'morrisArea',
		data: morrisAreaData,
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Series A', 'Series B'],
		lineColors: ['#0088cc', '#2baab1'],
		fillOpacity: 0.7,
		hideHover: true
	});

	/*
	Morris: Stacked
	*/
	Morris.Bar({
		resize: true,
		element: 'morrisStacked',
		data: morrisStackedData,
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Series A', 'Series B'],
		barColors: ['#0088cc', '#2baab1'],
		fillOpacity: 0.7,
		smooth: false,
		stacked: true,
		hideHover: true
	});

	/*
	Gauge: Basic
	*/
	(function() {
		var target = $('#gaugeBasic'),
			opts = $.extend(true, {}, {
				lines: 12, // The number of lines to draw
				angle: 0.12, // The length of each line
				lineWidth: 0.5, // The line thickness
				pointer: {
					length: 0.7, // The radius of the inner circle
					strokeWidth: 0.05, // The rotation offset
					color: '#444' // Fill color
				},
				limitMax: 'true', // If true, the pointer will not go past the end of the gauge
				colorStart: '#0088CC', // Colors
				colorStop: '#0088CC', // just experiment with them
				strokeColor: '#F1F1F1', // to see which ones work best for you
				generateGradient: true
			}, target.data('plugin-options'));

			var gauge = new Gauge(target.get(0)).setOptions(opts);

		gauge.maxValue = opts.maxValue; // set max gauge value
		gauge.animationSpeed = 32; // set animation speed (32 is default value)
		gauge.set(opts.value); // set actual value
		gauge.setTextField(document.getElementById("gaugeBasicTextfield"));
	})();

	/*
	Gauge: Alternative
	*/
	(function() {
		var target = $('#gaugeAlternative'),
			opts = $.extend(true, {}, {
				lines: 12, // The number of lines to draw
				angle: 0.12, // The length of each line
				lineWidth: 0.5, // The line thickness
				pointer: {
					length: 0.7, // The radius of the inner circle
					strokeWidth: 0.05, // The rotation offset
					color: '#444' // Fill color
				},
				limitMax: 'true', // If true, the pointer will not go past the end of the gauge
				colorStart: '#2BAAB1', // Colors
				colorStop: '#2BAAB1', // just experiment with them
				strokeColor: '#F1F1F1', // to see which ones work best for you
				generateGradient: true
			}, target.data('plugin-options'));

			var gauge = new Gauge(target.get(0)).setOptions(opts);

		gauge.maxValue = opts.maxValue; // set max gauge value
		gauge.animationSpeed = 32; // set animation speed (32 is default value)
		gauge.set(opts.value); // set actual value
		gauge.setTextField(document.getElementById("gaugeAlternativeTextfield"));
	})();

	/*
	Liquid Meter
	*/
	$('#meter').liquidMeter({
		shape: 'circle',
		color: '#0088CC',
		background: '#F9F9F9',
		fontSize: '24px',
		fontWeight: '600',
		stroke: '#F2F2F2',
		textColor: '#333',
		liquidOpacity: 0.9,
		liquidPalette: ['#333'],
		speed: 3000,
		animate: !$.browser.mobile
	});

	/*
	Liquid Meter Dark
	*/
	$('#meterDark').liquidMeter({
		shape: 'circle',
		color: '#0088CC',
		background: '#272A31',
		stroke: '#33363F',
		fontSize: '24px',
		fontWeight: '600',
		textColor: '#FFFFFF',
		liquidOpacity: 0.9,
		liquidPalette: ['#0088CC'],
		speed: 3000,
		animate: !$.browser.mobile
	});

	/*
	Sparkline: Line
	*/
	$("#sparklineLine").sparkline(sparklineLineData, {
		type: 'line',
		width: '80',
		height: '30',
		lineColor: '#0088cc'
	});

	/*
	Sparkline: Bar
	*/
	$("#sparklineBar").sparkline(sparklineBarData, {
		type: 'bar',
		width: '80',
		height: '30',
		barColor: '#0088cc',
		negBarColor: '#B20000'
	});

	/*
	Sparkline: Tristate
	*/
	$("#sparklineTristate").sparkline(sparklineTristateData, {
		type: 'tristate',
		width: '80',
		height: '30',
		posBarColor: '#0088cc',
		negBarColor: '#B20000'
	});

	/*
	Sparkline: Discrete
	*/
	$("#sparklineDiscrete").sparkline(sparklineDiscreteData, {
		type: 'discrete',
		width: '80',
		height: '30',
		lineColor: '#0088cc'
	});

	/*
	Sparkline: Bullet
	*/
	$("#sparklineBullet").sparkline(sparklineBulletData, {
		type: 'bullet',
		width: '80',
		height: '30',
		targetColor: '#ff7f00',
		performanceColor: '#0088cc'
	});

	/*
	Sparkline: Pie
	*/
	$("#sparklinePie").sparkline(sparklinePieData, {
		type: 'pie',
		height: '30',
		barColor: '#0088cc'
	});

}).apply( this, [ jQuery ]);