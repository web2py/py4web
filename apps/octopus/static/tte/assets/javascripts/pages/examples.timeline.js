

(function( $ ) {

	'use strict';

	var initLightbox = function() {
		$('.timeline .thumbnail-gallery').magnificPopup({
			delegate: 'a',
			type: 'image',
			tLoading: 'Loading image #%curr%...',
			mainClass: 'mfp-img-mobile',
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0,1] // Will preload 0 - before current, and 1 after the current image
			},
			image: {
				tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
			}
		});
	};

	var initGoogleMaps = function() {
		var map = new GMaps({
			div: '#gmap-checkin-example',
			lat: 40.7533405,
			lng: -73.982253,
			markers: [{
				lat: 40.7533405,
				lng: -73.982253,
				infoWindow: {
					content: '<p>New York Public Library</p>'
				}
			}],
			scrollwheel: false
		});

		map.addMarker({
			lat: 40.7533405,
			lng: -73.982253,
			infoWindow: {
				content: '<p>New York Public Library</p>'
			}
		});
	};

	$(function() {
		initLightbox();
		initGoogleMaps();
	});

}).apply(this, [ jQuery ]);