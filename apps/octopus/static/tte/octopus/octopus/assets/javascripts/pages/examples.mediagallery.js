(function( $ ) {

	/*
	Thumbnail: Select
	*/
	$('.mg-option input[type=checkbox]').on('change', function( ev ) {
		var wrapper = $(this).parents('.thumbnail');
		if($(this).is(':checked')) {
			wrapper.addClass('thumbnail-selected');
		} else {
			wrapper.removeClass('thumbnail-selected');
		}
	});

	$('.mg-option input[type=checkbox]:checked').trigger('change');

	/*
	Toolbar: Select All
	*/
	$('#mgSelectAll').on('click', function( ev ) {
		ev.preventDefault();
		var $this = $(this),
			$label = $this.find('> span');
			$checks = $('.mg-option input[type=checkbox]');

		if($this.attr('data-all-selected')) {
			$this.removeAttr('data-all-selected');
			$checks.prop('checked', false).trigger('change');
			$label.html($label.data('all-text'));
		} else {
			$this.attr('data-all-selected', 'true');
			$checks.prop('checked', true).trigger('change');
			$label.html($label.data('none-text'));
		}
	});

	/*
	Image Preview: Lightbox
	*/
	$('.thumb-preview a[href]').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		mainClass: 'mfp-img-mobile',
		image: {
			verticalFit: true
		}
	});

	$('.thumb-preview .mg-zoom').on('click.lightbox', function( ev ) {
		ev.preventDefault();
		$(this).closest('.thumb-preview').find('a.thumb-image').triggerHandler('click');
	});

	/*
	Thumnail: Dropdown Options
	*/
	$('.thumbnail .mg-toggle').parent()
		.on('show.bs.dropdown', function( ev ) {
			$(this).closest('.mg-thumb-options').css('overflow', 'visible');
		})
		.on('hidden.bs.dropdown', function( ev ) {
			$(this).closest('.mg-thumb-options').css('overflow', '');
		});

	$('.thumbnail').on('mouseenter', function() {
		var toggle = $(this).find('.mg-toggle');
		if ( toggle.parent().hasClass('open') ) {
			toggle.dropdown('toggle');
		}
	});

	/*
	Isotope: Sort Thumbnails
	*/
	$("[data-sort-source]").each(function() {

		var source = $(this);
		var destination = $("[data-sort-destination][data-sort-id=" + $(this).attr("data-sort-id") + "]");

		if(destination.get(0)) {

			$(window).load(function() {

				destination.isotope({
					itemSelector: ".isotope-item",
					layoutMode: 'fitRows'
				});

				$(window).on('sidebar-left-toggle inner-menu-toggle', function() {
					destination.isotope();
				});

				source.find("a[data-option-value]").click(function(e) {

					e.preventDefault();

					var $this = $(this),
						filter = $this.attr("data-option-value");

					source.find(".active").removeClass("active");
					$this.closest("li").addClass("active");

					destination.isotope({
						filter: filter
					});

					if(window.location.hash != "" || filter.replace(".","") != "*") {
						window.location.hash = filter.replace(".","");
					}

					return false;

				});

				$(window).bind("hashchange", function(e) {

					var hashFilter = "." + location.hash.replace("#",""),
						hash = (hashFilter == "." || hashFilter == ".*" ? "*" : hashFilter);

					source.find(".active").removeClass("active");
					source.find("[data-option-value='" + hash + "']").closest("li").addClass("active");

					destination.isotope({
						filter: hash
					});

				});

				var hashFilter = "." + (location.hash.replace("#","") || "*");
				var initFilterEl = source.find("a[data-option-value='" + hashFilter + "']");

				if(initFilterEl.get(0)) {
					source.find("[data-option-value='" + hashFilter + "']").click();
				} else {
					source.find(".active a").click();
				}

			});

		}

	});

}(jQuery));