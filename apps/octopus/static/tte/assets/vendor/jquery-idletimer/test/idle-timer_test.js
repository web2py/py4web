(function($) {
/*
		======== A Handy Little QUnit Reference ========
		http://docs.jquery.com/QUnit

		Test methods:
			expect(numAssertions)
			stop(increment)
			start(decrement)
		Test assertions:
			ok(value, [message])
			equal(actual, expected, [message])
			notEqual(actual, expected, [message])
			deepEqual(actual, expected, [message])
			notDeepEqual(actual, expected, [message])
			strictEqual(actual, expected, [message])
			notStrictEqual(actual, expected, [message])
			raises(block, [expected], [message])
*/
    //Name | expects | test
	module("Events Auto Binding");
	asyncTest("idle Event Triggered", 2, function () {
		$(document).on("idle.idleTimer", function (event, elem, obj) {

			ok(true, "idle fires at document");
			ok(obj.idle, "object returned properly");

			$.idleTimer("destroy");
			$(document).off();

			start();
		});
		$.idleTimer( 100 );
	});
	asyncTest( "active Event Triggered", 2, function() {
		$( document ).on( "active.idleTimer", function(event, elem, obj){

			ok(true, "active fires at document");
			ok(!obj.idle, "object returned properly");

			$.idleTimer("destroy");
			$(document).off();

			start();
		});
		$.idleTimer({idle:true});
		setTimeout( function(){
			$( "#qunit-fixture" ).trigger( "keydown" );
		}, 100 );
	});




	module("Events Element Binding");
	asyncTest("idle Triggered", 2, function () {
		$("#qunit-fixture").on("idle.idleTimer", function (event, elem, obj) {

			ok(true, "idle fires at document");
			ok(obj.idle, "object returned properly");

			$("#qunit-fixture").idleTimer("destroy");

			start();
		});
		$("#qunit-fixture").idleTimer(100);
	});
	asyncTest("active Triggered", 2, function () {
		$("#qunit-fixture").on("active.idleTimer", function (event, elem, obj) {

			ok(true, "active fires at document");
			ok(!obj.idle, "object returned properly");

			$("#qunit-fixture").idleTimer("destroy");

			start();
		});
		$("#qunit-fixture").idleTimer({ idle: true });
		setTimeout(function () {
			$("#qunit-fixture").trigger("keydown");
		}, 100);
	});

	
	
	/*
	Need to actually test pause/resume/reset, not just thier return type
	*/
	module("Functional");
	asyncTest("Pause works and is a jQuery instance", 4, function () {

		$.idleTimer(100);
		equal(typeof $.idleTimer( "pause" ).jquery  , "string", "pause should be jquery" );

		$.idleTimer("resume");
		equal(typeof $(document).idleTimer("pause").jquery, "string", "pause should be jquery");

		setTimeout(function () {
			ok(!$.idleTimer("isIdle"), "timer still active");
			ok(!$(document).idleTimer("isIdle"), "timer still active");

			$.idleTimer("destroy");
			$(document).off();

			start();
		}, 200);
	});



	asyncTest("Resume works and is a jQuery instance", 4, function () {

		$.idleTimer(100);

		$.idleTimer("pause");
		equal(typeof $.idleTimer("resume").jquery, "string", "resume should be jquery");

		$.idleTimer("pause");
		equal(typeof $(document).idleTimer("resume").jquery, "string", "resume should be jquery");

		setTimeout(function () {
			ok($.idleTimer("isIdle"), "timer inactive");
			ok($(document).idleTimer("isIdle"), "timer inactive");

			$.idleTimer("destroy");
			$(document).off();

			start();
		}, 200);
	});

	test("Elapsed time is a number", 2, function () {

		$.idleTimer(100);

		equal(typeof $.idleTimer("getElapsedTime"), "number", "Elapsed time should be a number");
		equal(typeof $(document).idleTimer("getElapsedTime"), "number", "Elapsed time should be a number");
	});

	test("Init works and is a jQuery instance", 4, function () {

		equal(typeof $.idleTimer(100).jquery, "string", "Init should be jquery");
		equal(typeof $("#qunit-fixture").idleTimer(100).jquery, "string", "Destroy should be jquery");

		equal(typeof $(document).data("idleTimerObj").idle, "boolean", "Init data added");
		equal(typeof $("#qunit-fixture").data("idleTimerObj").idle, "boolean", "Init data added");
	});

	test("Destroy works and is a jQuery instance", 4, function () {

		$.idleTimer(100);
		$("#qunit-fixture").idleTimer(100);

		equal(typeof $.idleTimer("destroy").jquery, "string", "Destroy should be jquery");
		equal(typeof $("#qunit-fixture").idleTimer("destroy").jquery, "string", "Destroy should be jquery");

		equal(typeof $(document).data("idleTimerObj"), "undefined", "destroy removed data");
		equal(typeof $("#qunit-fixture").data("idleTimerObj"), "undefined", "destroy removed data");
	});

	asyncTest("Reset is a jQuery instance", 6, function () {

		//start the timer
		$.idleTimer(200);
		$.idleTimer("pause");
		$("#qunit-fixture").idleTimer(200);
		$("#qunit-fixture").idleTimer("pause");

        //After a bit, reset it 
		setTimeout(function () {
			equal(typeof $.idleTimer("reset").jquery, "string", "reset should be jquery");
			equal(typeof $("#qunit-fixture").idleTimer("reset").jquery, "string", "reset should be jquery");

			ok($(document).data("idleTimerObj").remaining===null, "reset remaining");
			ok($("#qunit-fixture").data("idleTimerObj").remaining === null, "reset remaining");
		}, 100);

		setTimeout(function () {
			ok($.idleTimer("isIdle"), "timer inactive");
			ok($("#qunit-fixture").idleTimer("isIdle"), "timer inactive");

			$.idleTimer("destroy");
			$("#qunit-fixture").idleTimer("destroy");
			$(document).off();

			start();
		}, 400);
	
	});
	
	test("Last Active time is a number", 2, function () {

		$.idleTimer(100);

		equal(typeof $.idleTimer("getLastActiveTime"), "number", "Last Active time should be a number");
		equal(typeof $(document).idleTimer("getLastActiveTime"), "number", "Last Active time should be a number");

		$.idleTimer("destroy");
	});
	
	test("Remaining time is a number", 2, function () {

		$.idleTimer(100);

		equal( typeof $.idleTimer( "getRemainingTime" ), "number", "Remaining time should be a number" );
		equal(typeof $(document).idleTimer("getRemainingTime"), "number", "Remaining time should be a number");

		$.idleTimer("destroy");
	});
	test("isIdle is a boolean", 2, function () {

		$.idleTimer(100);

		equal(typeof $.idleTimer("isIdle"), "boolean", "isIdle should be a boolean");
		equal(typeof $(document).idleTimer("isIdle"), "boolean", "isIdle should be a boolean");

		$.idleTimer("destroy");
	});

}(jQuery));
