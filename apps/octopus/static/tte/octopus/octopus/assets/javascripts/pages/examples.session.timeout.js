

(function( $ ) {

	'use strict';

	var SessionTimeout = {

		options: {
			keepAliveUrl: '',
			alertOn: 15000, // ms
			timeoutOn: 20000 // ms
		},

		alertTimer: null,
		timeoutTimer: null,

		initialize: function() {
			this
				.start()
				.setup();
		},

		start: function() {
			var _self = this;

			this.alertTimer = setTimeout(function() {
				_self.onAlert();
			}, this.options.alertOn );

			this.timeoutTimer = setTimeout(function() {
				_self.onTimeout();
			}, this.options.timeoutOn );

			return this;
		},

		// bind success callback for all ajax requests
		setup: function() {
			var _self = this;

			// if server returns successfuly,
			// then the session is renewed.
			// thats why we reset here the counter
			$( document ).ajaxSuccess(function() {
				_self.reset();
			});

			return this;
		},

		reset: function() {
			clearTimeout(this.alertTimer);
			clearTimeout(this.timeoutTimer);
			this.start();

			return this;
		},

		keepAlive: function() {
			// we don't have session on demo,
			// so the code above prevent a request to be made
			// in your project, please remove the next 3 lines of code
			if ( !this.options.keepAliveUrl ) {
				this.reset();
				return;
			}

			var _self = this;

			$.post( this.options.keepAliveUrl, function( data ) {
				_self.reset();
			});
		},

		// ------------------------------------------------------------------------
		// CUSTOMIZE HERE
		// ------------------------------------------------------------------------
		onAlert: function() {
			// if you want to show some warning
			// TODO: remove this confirm (it breaks the logic and it's ugly)
			var renew = confirm( 'Your session is about to expire, do you want to renew?' );

			if ( renew ) {
				this.keepAlive();
			}

			// if you want session to not expire
			// this.keepAlive();
		},

		onTimeout: function() {
			self.location.href = 'pages-signin.html';
		}

	};

	$(function() {
		SessionTimeout.initialize();
	});

}).apply(this, [ jQuery ]);