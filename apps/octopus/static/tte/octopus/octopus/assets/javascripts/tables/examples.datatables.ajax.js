
(function( $ ) {

	'use strict';

	var datatableInit = function() {

		var $table = $('#datatable-ajax');
		$table.dataTable({
			bProcessing: true,
			sAjaxSource: $table.data('url')
		});

	};

	$(function() {
		datatableInit();
	});

}).apply( this, [ jQuery ]);