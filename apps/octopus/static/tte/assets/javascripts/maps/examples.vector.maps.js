

(function( $ ) {

	'use strict';

	var initMap = function( $el, options ) {
		var defaults = {
			backgroundColor: null,
			color: '#FFFFFF',
			hoverOpacity: 0.7,
			selectedColor: '#005599',
			enableZoom: true,
			borderWidth:1,
			showTooltip: true,
			values: sample_data,
			scaleColors: ['#1AA2E6', '#0088CC'],
			normalizeFunction: 'polynomial'
		};

		$el.vectorMap( $.extend( defaults, options ) );
	};

	$(function() {
		$( '[data-vector-map]' ).each(function() {
			var $this = $(this);
			initMap( $this, ($this.data( 'plugin-options' ) || {}) )
		});
	});

}).apply( this, [ jQuery ]);