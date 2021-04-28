

(function( $ ) {

	'use strict';

	var datatableInit = function() {

		$('#datatable-default').dataTable();

	};

	$(function() {
		datatableInit();
	});

}).apply( this, [ jQuery ]);