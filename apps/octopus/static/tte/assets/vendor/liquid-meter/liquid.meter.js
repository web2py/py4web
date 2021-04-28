/**
 * @package  Liquid Meter
 * @author   Okler Themes
 * @license  Licensed under CC BY-NC-ND
 *
 * Copyright (c) 2014
 * Inspired on dribble shot:
 * http://dribbble.com/shots/1069484-Charging-Animation
 */

(function($) {

	'use strict';

	var defaultOptions = {
		shape: 'circle',
		color: '#82BF41',
		background: '#4C4C52',
		stroke: '#23282F',
		textColor: '#FFFFFF',
		fontFamily: 'Open Sans',
		fontSize: '24px',
		fontWeight: '600',
		liquidOpacity: 0.9,
		liquidPalette: ['#82BF41'],
		speed: 3000,
		animate: true
	};

	var LiquidMeter = function(el, options) {

		if (typeof Snap == 'undefined') {
			throw 'Snap.js not found.';
		}

		this.meter = $(el);
		this.options = options;
		this.options.text = this.meter.text();
		this.init();

	};

	LiquidMeter.prototype = {

		init: function(el, options) {

			this.wrapper = this.meter.parent('.liquid-meter');
			if ( !this.wrapper.get(0) ) {
				var wrapper = $('<div>').attr({ 'class': 'liquid-meter' });
				this.wrapper = this.meter.wrap( wrapper ).parent();
			}

			var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
			svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
			svg.setAttribute('viewBox', '0 0 220 220');
			this.wrapper.prepend(svg);

			this.svg = $(svg).attr({
				width: '100%',
				height: '100%'
			});

			this.frames = [
				[6, -6, -10, 6, 13, -10],		// 1
				[6, -5, -13, 4, 31, -5],		// 2
				[7, -5, -9, 0, 31, -5],			// 3
				[7, -5, -9, -6, 30, -6],		// 4
				[6, -10, -10, -10, 33, -4],		// 5
				[8, -4, -8, -13, 38, 7],		// 6
				[8, -8, -5, -15, 55, 11],		// 7
				[7, -19, -2, -16, 33, 16],		// 8
				[3, -23, -2, -16, 42, 21],		// 9
				[3, -22, 7, -18, 27, 21],		// 10
				[2, -26, 15, -18, 25, 20] ,		// 11
				[-3, -23, 18, -18, 26, 19] ,	// 12
				[-6, -40, 18, -18, 22, 22] ,	// 13
				[-15, -16, 23, -13, 37, 22],	// 14
				[-15, -16, 23, -13, 37, 22],	// 15
				[-17, -16, 23, -10, 33, 22],	// 16
				[-18, -16, 23, -10, 35, 21],	// 17
				[-20, -12, 23, -5, 34, 20],		// 18
				[-22, -13, 20, -1, 35, 22],		// 19
				[-22, -13, 20, 5, 32, 21],		// 20
				[-21, -16, 19, 8, 34, 15],		// 21
				[-23, -16, 16, 10, 36, 9],		// 22
				[-22, -23, 13, 10, 48, 0],		// 23
				[-23, -20, 13, 8, 45, -6],		// 24
				[-20, -22, 7, 10, 44, -6],		// 25
				[-20, -22, 5, 10, 42, -7],		// 26
				[-18, -20, 0, 10, 41, -8],		// 27
				[-15, -22, -7, 10, 41, -8],		// 28
				[-11, -33, -8, 10, 41, -8],		// 29
				[-7, -36, -6, 10, 15, -11],		// 30
				[0, -39, -8, 10, 15, -11],		// 31
				[0, -36, -8, 7, 15, -11],		// 32
			];

			this.paper = Snap(svg);

			this.draw();
			this.observe();
			if ( this.options.animate ) {
				this.animate();
			} else {
				this.drawFrame(1);
			}

			this.wrapper.addClass( 'liquid-meter-loaded' );

			return this;
		},

		draw: function() {
			this.value = parseInt(this.meter.val() || this.meter.attr('value'), 10);

			var paper = this.paper;

			this.recipient = paper.circle(110, 110, 95);

			var background = this.makeGradient(this.options.background);

			this.recipient.attr({
				fill: background,
				stroke: this.options.stroke,
				strokeWidth: 15
			});

			var mask = paper.circle(110, 110, 87);
			mask.attr({
				fill: '#FFFFFF'
			});

			this.liquid = paper.path();

			this.liquid.attr({
				id: 'front',
				fill: this.options.color,
				mask: mask,
				stroke: lighten(this.options.color, 20),
				strokeWidth: 1
			});

			this.label = paper.text('50%', '50%', [this.value, '%']);
			this.label.attr({
				fill: this.options.textColor,
				dy: '.4em',
				'font-family': this.options.fontFamily,
				'font-size': this.options.fontSize,
				'font-weight': this.options.fontWeight,
				'text-anchor': 'middle',
				stroke: this.options.textColor
			});
			this.label.selectAll('tspan:nth-child(2)').attr({
				'font-size': '24',
				stroke: 'none'
			});

			return this;

		},

		observe: function() {
			var _self = this;

			this.meter.on('change', function() {
				_self.set( $(this).val() );
			});
		},

		set: function( val ) {
			var value = parseInt( val, 10 );
			this.meter.val( value );
			this.value = value;
			this.label.node.textContent = value + '%';
		},

		liquidPalette: function( val ) {
			this.options.liquidPalette = val;
		},

		background: function( val ) {
			this.options.background = val;
		},

		stroke: function( val ) {
			this.options.stroke = val;
		},

		color: function( val ) {
			this.options.color = val;

			this.liquid.attr({
				fill: this.options.color,
				stroke: lighten(this.options.color, 20)
			});
		},

		makeGradient: function(color) {
			return this.paper.gradient(Snap.format('L(0, 0, 100, 100){color.top}-{color.bottom}', {
				color: {
					top: lighten(color, 6),
					bottom: color
				}
			}));
		},

		makePath: function(value, t1, x1, y1, t2, x2, y2) {
			var top = ((100 - value) * 1.76) + 22;
			return Snap.format('M0,{left} C{curve.x1},{curve.y1} {curve.x2},{curve.y2} 220,{right} L220,220 L0,220 z', {
				left: top - (t1 || 0),
				right: top - (t2 || 0),
				curve: {
					x1: x1 + top,
					y1: y1 + top,
					x2: x2 + top,
					y2: y2 + top
				}
			});
		},

		drawFrame: function(number) {
			var frame = this.frames[number - 1],
				t1 = frame[0],
				x1 = frame[1],
				y1 = frame[2],
				t2 = frame[3],
				x2 = frame[4],
				y2 = frame[5];
			this.liquid.attr({ d: this.makePath( this.value, t1, x1, y1, t2, x2, y2 )});
		},

		animate: function() {
			var requestAnimationFrame = window.requestAnimationFrame       ||
										window.webkitRequestAnimationFrame ||
										window.mozRequestAnimationFrame    ||
										window.oRequestAnimationFrame      ||
										window.msRequestAnimationFrame     ||
										function (callback) {
											setTimeout(callback, 0);
										},
				frames = this.frames.length,
				interval = this.options.speed / frames,
				currentFrame = 1,
				drawFrame = this.drawFrame.bind(this);

				function loop() {
					requestAnimationFrame(function() {
						draw();
					});
					setTimeout(loop, interval);
				}

				function draw() {
					drawFrame(currentFrame);
					currentFrame++;
					if (currentFrame >= frames) {
						currentFrame = 1;
					}
				}

				loop();

			return this;
		}

	};

	/**
	* liquidMeter jQuery plugin - public method
	* @param  - {Object} options - Passed options extending defaultOptions
	* @return - {Selector}       - Array of elements
	*/
	$.fn.liquidMeter = function(options, value) {
		var isSetter = (typeof options === 'string' && !!value);

		if ( !isSetter ) {
			options = $.extend({}, defaultOptions, options);
		}
		return this.map(function () {

			// preventing against multiple instantiations
			var instance = $(this).data('liquid-meter');
			if (!instance) {
				instance = new LiquidMeter(this, options);
				$(this).data('liquid-meter', instance);
			}
			if ( isSetter ) {
				instance[ options ]( value );
			}
			return instance;

		});
	};

	/**
	 * Util function for lightening the colour with a %
	 * @param - string - colour with leading #
	 * @param - number - percentage to lighten by
	 */
	function lighten(color, percent) {
		var n = parseInt(color.slice(1), 16),
		a = Math.round(2.55 * percent || 0),
		// Bitshift 16 bits to the left
		r = (n >> 16) + a,
		// Bitshift 8 bits to the left based on blue
		b = (n >> 8 & 0x00FF) + a,
		//
		g = (n & 0x0000FF) + a;
		// Calculate
		return '#' + (
				0x1000000 + (r < 255 ? r < 1 ? 0 : r : 255) * 0x10000 +
				(b < 255 ? b < 1 ? 0 : b : 255) * 0x100 + (g < 255 ? g < 1 ? 0 : g : 255)
			).toString(16).slice(1).toUpperCase();
	};

}(jQuery));