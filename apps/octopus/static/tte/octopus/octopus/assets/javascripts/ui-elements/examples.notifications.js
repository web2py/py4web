

(function( $ ) {

	'use strict';

	/*
	Default Notifications
	*/
	$('#default-primary').click(function() {
		new PNotify({
			title: 'Regular Notice',
			text: 'Check me out! I\'m a notice.',
			type: 'custom',
			addclass: 'notification-primary',
			icon: 'fa fa-twitter'
		});
	});

	$('#default-notice').click(function() {
		new PNotify({
			title: 'Regular Notice',
			text: 'Check me out! I\'m a notice.'
		});
	});

	$('#default-success').click(function() {
		new PNotify({
			title: 'Regular Notice',
			text: 'Check me out! I\'m a notice.',
			type: 'success'
		});
	});

	$('#default-info').click(function() {
		new PNotify({
			title: 'Regular Notice',
			text: 'Check me out! I\'m a notice.',
			type: 'info'
		});
	});

	$('#default-error').click(function() {
		new PNotify({
			title: 'Regular Notice',
			text: 'Check me out! I\'m a notice.',
			type: 'error'
		});
	});

	$('#default-dark').click(function() {
		new PNotify({
			title: 'Regular Notice',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-dark',
			icon: 'fa fa-user'
		});
	});

	/*
	Shadowed Notifications
	*/
	$('#shadow-primary').click(function() {
		new PNotify({
			title: 'With Shadow',
			text: 'Check me out! I\'m a notice.',
			shadow: true,
			addclass: 'notification-primary',
			icon: 'fa fa-twitter'
		});
	});

	$('#shadow-notice').click(function() {
		new PNotify({
			title: 'With Shadow',
			text: 'Check me out! I\'m a notice.',
			shadow: true
		});
	});

	$('#shadow-success').click(function() {
		new PNotify({
			title: 'With Shadow',
			text: 'Check me out! I\'m a notice.',
			type: 'success',
			shadow: true
		});
	});

	$('#shadow-info').click(function() {
		new PNotify({
			title: 'With Shadow',
			text: 'Check me out! I\'m a notice.',
			type: 'info',
			shadow: true
		});
	});

	$('#shadow-error').click(function() {
		new PNotify({
			title: 'With Shadow',
			text: 'Check me out! I\'m a notice.',
			type: 'error',
			shadow: true
		});
	});

	$('#shadow-dark').click(function() {
		new PNotify({
			title: 'With Shadow',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-dark',
			icon: 'fa fa-user',
			shadow: true
		});
	});

	/*
	No Icon Notification
	*/
	$('#no-icon-primary').click(function() {
		new PNotify({
			title: 'Without Icon',
			text: 'Check me out! I\'m a notice.',
			addclass: 'ui-pnotify-no-icon notification-primary',
			icon: false
		});
	});

	$('#no-icon-notice').click(function() {
		new PNotify({
			title: 'Without Icon',
			text: 'Check me out! I\'m a notice.',
			addclass: 'ui-pnotify-no-icon',
			icon: false
		});
	});

	$('#no-icon-success').click(function() {
		new PNotify({
			title: 'Without Icon',
			text: 'Check me out! I\'m a notice.',
			type: 'success',
			addclass: 'ui-pnotify-no-icon',
			icon: false
		});
	});

	$('#no-icon-info').click(function() {
		new PNotify({
			title: 'Without Icon',
			text: 'Check me out! I\'m a notice.',
			type: 'info',
			addclass: 'ui-pnotify-no-icon',
			icon: false
		});
	});

	$('#no-icon-error').click(function() {
		new PNotify({
			title: 'Without Icon',
			text: 'Check me out! I\'m a notice.',
			type: 'error',
			addclass: 'ui-pnotify-no-icon',
			icon: false
		});
	});

	$('#no-icon-dark').click(function() {
		new PNotify({
			title: 'Without Icon',
			text: 'Check me out! I\'m a notice.',
			addclass: 'ui-pnotify-no-icon notification-dark',
			icon: false
		});
	});

	/*
	No Border Radius Notification
	*/
	$('#no-radious-primary').click(function() {
		new PNotify({
			title: 'border-radius: 0;',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-primary',
			cornerclass: 'ui-pnotify-sharp',
			icon: 'fa fa-twitter'
		});
	});

	$('#no-radious-notice').click(function() {
		new PNotify({
			title: 'border-radius: 0;',
			text: 'Check me out! I\'m a notice.',
			cornerclass: 'ui-pnotify-sharp'
		});
	});

	$('#no-radious-success').click(function() {
		new PNotify({
			title: 'border-radius: 0;',
			text: 'Check me out! I\'m a notice.',
			type: 'success',
			cornerclass: 'ui-pnotify-sharp'
		});
	});

	$('#no-radious-info').click(function() {
		new PNotify({
			title: 'border-radius: 0;',
			text: 'Check me out! I\'m a notice.',
			type: 'info',
			cornerclass: 'ui-pnotify-sharp'
		});
	});

	$('#no-radious-error').click(function() {
		new PNotify({
			title: 'border-radius: 0;',
			text: 'Check me out! I\'m a notice.',
			type: 'error',
			cornerclass: 'ui-pnotify-sharp'
		});
	});

	$('#no-radious-dark').click(function() {
		new PNotify({
			title: 'border-radius: 0;',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-dark',
			icon: 'fa fa-user',
			cornerclass: 'ui-pnotify-sharp'
		});
	});

	/*
	Custom Icon Notification
	*/
	$('#custom-icon-primary').click(function() {
		new PNotify({
			title: 'Custom Icon',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-primary',
			icon: 'fa fa-home'
		});
	});

	$('#custom-icon-notice').click(function() {
		new PNotify({
			title: 'Custom Icon',
			text: 'Check me out! I\'m a notice.',
			icon: 'fa fa-home'
		});
	});

	$('#custom-icon-success').click(function() {
		new PNotify({
			title: 'Custom Icon',
			text: 'Check me out! I\'m a notice.',
			type: 'success',
			icon: 'fa fa-home'
		});
	});

	$('#custom-icon-info').click(function() {
		new PNotify({
			title: 'Custom Icon',
			text: 'Check me out! I\'m a notice.',
			type: 'info',
			icon: 'fa fa-home'
		});
	});

	$('#custom-icon-error').click(function() {
		new PNotify({
			title: 'Custom Icon',
			text: 'Check me out! I\'m a notice.',
			type: 'error',
			icon: 'fa fa-home'
		});
	});

	$('#custom-icon-dark').click(function() {
		new PNotify({
			title: 'Custom Icon',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-dark',
			icon: 'fa fa-home'
		});
	});

	/*
	Icon without border notification
	*/
	$('#icon-without-border-primary').click(function() {
		new PNotify({
			title: 'Icon Without Border',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-primary icon-nb',
			icon: 'fa fa-twitter'
		});
	});

	$('#icon-without-border-notice').click(function() {
		new PNotify({
			title: 'Icon Without Border',
			text: 'Check me out! I\'m a notice.',
			addclass: 'icon-nb'
		});
	});

	$('#icon-without-border-success').click(function() {
		new PNotify({
			title: 'Icon Without Border',
			text: 'Check me out! I\'m a notice.',
			type: 'success',
			addclass: 'icon-nb'
		});
	});

	$('#icon-without-border-info').click(function() {
		new PNotify({
			title: 'Icon Without Border',
			text: 'Check me out! I\'m a notice.',
			type: 'info',
			addclass: 'icon-nb'
		});
	});

	$('#icon-without-border-error').click(function() {
		new PNotify({
			title: 'Icon Without Border',
			text: 'Check me out! I\'m a notice.',
			type: 'error',
			addclass: 'icon-nb'
		});
	});

	$('#icon-without-border-dark').click(function() {
		new PNotify({
			title: 'Icon Without Border',
			text: 'Check me out! I\'m a notice.',
			addclass: 'notification-dark icon-nb',
			icon: 'fa fa-user'
		});
	});

	/*
	Non-blocking notifications
	*/
	$('#non-blocking-primary').click(function() {
		new PNotify({
			title: 'Non-Blocking',
			text: 'I\'m a special kind of notice called "non-blocking". When you hover over me I\'ll fade to show the elements underneath. Feel free to click any of them just like I wasn\'t even here.\n\nNote: HTML links don\'t trigger in some browsers, due to security settings.',
			addclass: 'notification-primary',
			icon: 'fa fa-twitter',
			nonblock: {
				nonblock: true,
				nonblock_opacity: .2
		   }
		});
	});

	$('#non-blocking-notice').click(function() {
		new PNotify({
			title: 'Non-Blocking',
			text: 'I\'m a special kind of notice called "non-blocking". When you hover over me I\'ll fade to show the elements underneath. Feel free to click any of them just like I wasn\'t even here.\n\nNote: HTML links don\'t trigger in some browsers, due to security settings.',
			nonblock: {
				nonblock: true,
				nonblock_opacity: .2
			}
		});
	});

	$('#non-blocking-success').click(function() {
		new PNotify({
			title: 'Non-Blocking',
			text: 'I\'m a special kind of notice called "non-blocking". When you hover over me I\'ll fade to show the elements underneath. Feel free to click any of them just like I wasn\'t even here.\n\nNote: HTML links don\'t trigger in some browsers, due to security settings.',
			type: 'success',
			nonblock: {
				nonblock: true,
				nonblock_opacity: .2
			}
		});
	});

	$('#non-blocking-info').click(function() {
		new PNotify({
			title: 'Non-Blocking',
			text: 'I\'m a special kind of notice called "non-blocking". When you hover over me I\'ll fade to show the elements underneath. Feel free to click any of them just like I wasn\'t even here.\n\nNote: HTML links don\'t trigger in some browsers, due to security settings.',
			type: 'info',
			nonblock: {
				nonblock: true,
				nonblock_opacity: .2
			}
		});
	});

	$('#non-blocking-error').click(function() {
		new PNotify({
			title: 'Non-Blocking',
			text: 'I\'m a special kind of notice called "non-blocking". When you hover over me I\'ll fade to show the elements underneath. Feel free to click any of them just like I wasn\'t even here.\n\nNote: HTML links don\'t trigger in some browsers, due to security settings.',
			type: 'error',
			nonblock: {
				nonblock: true,
				nonblock_opacity: .2
			}
		});
	});

	$('#non-blocking-dark').click(function() {
		new PNotify({
			title: 'Non-Blocking',
			text: 'I\'m a special kind of notice called "non-blocking". When you hover over me I\'ll fade to show the elements underneath. Feel free to click any of them just like I wasn\'t even here.\n\nNote: HTML links don\'t trigger in some browsers, due to security settings.',
			addclass: 'notification-dark',
			icon: 'fa fa-user',
			nonblock: {
				nonblock: true,
				nonblock_opacity: .2
			}
		});
	});

	/*
	Sticky notifications
	*/
	$('#sticky-primary').click(function() {
		new PNotify({
			title: 'Sticky',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to close me yourself.',
			addclass: 'notification-primary',
			icon: 'fa fa-twitter',
			hide: false,
			buttons: {
				sticker: false
			}
		});
	});

	$('#sticky-notice').click(function() {
		new PNotify({
			title: 'Sticky',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to close me yourself.',
			hide: false,
			buttons: {
				sticker: false
			}
		});
	});

	$('#sticky-success').click(function() {
		new PNotify({
			title: 'Sticky',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to close me yourself.',
			type: 'success',
			hide: false,
			buttons: {
				sticker: false
			}
		});
	});

	$('#sticky-info').click(function() {
		new PNotify({
			title: 'Sticky',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to close me yourself.',
			type: 'info',
			hide: false,
			buttons: {
				sticker: false
			}
		});
	});

	$('#sticky-error').click(function() {
		new PNotify({
			title: 'Sticky',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to close me yourself.',
			type: 'error',
			hide: false,
			buttons: {
				sticker: false
			}
		});
	});

	$('#sticky-dark').click(function() {
		new PNotify({
			title: 'Sticky',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to close me yourself.',
			addclass: 'notification-dark',
			icon: 'fa fa-user',
			hide: false,
			buttons: {
				sticker: false
			}
		});
	});

	/*
	Click to close notifications
	*/
	$('#click-to-close-primary').click(function() {
		var notice = new PNotify({
			title: 'Click to Close',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to click me to close.',
			addclass: 'notification-primary click-2-close',
			icon: 'fa fa-twitter',
			hide: false,
			buttons: {
				closer: false,
				sticker: false
			}
		});

		notice.get().click(function() {
			notice.remove();
		});
	});

	$('#click-to-close-notice').click(function() {
		var notice = new PNotify({
			title: 'Click to Close',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to click me to close.',
			addclass: 'click-2-close',
			hide: false,
			buttons: {
				closer: false,
				sticker: false
			}
		});

		notice.get().click(function() {
			notice.remove();
		});
	});

	$('#click-to-close-success').click(function() {
		var notice = new PNotify({
			title: 'Click to Close',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to click me to close.',
			type: 'success',
			addclass: 'click-2-close',
			hide: false,
			buttons: {
				closer: false,
				sticker: false
			}
		});

		notice.get().click(function() {
			notice.remove();
		});
	});

	$('#click-to-close-info').click(function() {
		var notice = new PNotify({
			title: 'Click to Close',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to click me to close.',
			type: 'info',
			addclass: 'click-2-close',
			hide: false,
			buttons: {
				closer: false,
				sticker: false
			}
		});

		notice.get().click(function() {
			notice.remove();
		});
	});

	$('#click-to-close-error').click(function() {
		var notice = new PNotify({
			title: 'Click to Close',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to click me to close.',
			type: 'error',
			addclass: 'click-2-close',
			hide: false,
			buttons: {
				closer: false,
				sticker: false
			}
		});

		notice.get().click(function() {
			notice.remove();
		});
	});

	$('#click-to-close-dark').click(function() {
		var notice = new PNotify({
			title: 'Click to Close',
			text: 'Check me out! I\'m a sticky notice. You\'ll have to click me to close.',
			addclass: 'notification-dark click-2-close',
			icon: 'fa fa-user',
			hide: false,
			buttons: {
				closer: false,
				sticker: false
			}
		});

		notice.get().click(function() {
			notice.remove();
		});
	});

	/*
	Positions
	*/
	var stack_topleft = {"dir1": "down", "dir2": "right", "push": "top"};
	var stack_bottomleft = {"dir1": "right", "dir2": "up", "push": "top"};
	var stack_bottomright = {"dir1": "up", "dir2": "left", "firstpos1": 15, "firstpos2": 15};
	var stack_bar_top = {"dir1": "down", "dir2": "right", "push": "top", "spacing1": 0, "spacing2": 0};
	var stack_bar_bottom = {"dir1": "up", "dir2": "right", "spacing1": 0, "spacing2": 0};

	$('#position-1-primary').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-primary stack-topleft',
			icon: 'fa fa-twitter'
		});
	});

	$('#position-1-notice').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'stack-topleft'
		});
	});

	$('#position-1-success').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'success',
			addclass: 'stack-topleft'
		});
	});

	$('#position-1-info').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'info',
			addclass: 'stack-topleft'
		});
	});

	$('#position-1-error').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'error',
			addclass: 'stack-topleft'
		});
	});

	$('#position-1-dark').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-dark stack-topleft',
			icon: 'fa fa-user'
		});
	});

	$('#position-2-primary').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-primary stack-bottomleft',
			icon: 'fa fa-twitter',
			stack: stack_bottomleft
		});
	});

	$('#position-2-notice').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'stack-bottomleft',
			stack: stack_bottomleft
		});
	});

	$('#position-2-success').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'success',
			addclass: 'stack-bottomleft',
			stack: stack_bottomleft
		});
	});

	$('#position-2-info').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'info',
			addclass: 'stack-bottomleft',
			stack: stack_bottomleft
		});
	});

	$('#position-2-error').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'error',
			addclass: 'stack-bottomleft',
			stack: stack_bottomleft
		});
	});

	$('#position-2-dark').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-dark stack-bottomleft',
			icon: 'fa fa-user',
			stack: stack_bottomleft
		});
	});

	$('#position-3-primary').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-primary stack-bottomright',
			icon: 'fa fa-twitter',
			stack: stack_bottomright
		});
	});

	$('#position-3-notice').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'stack-bottomright',
			stack: stack_bottomright
		});
	});

	$('#position-3-success').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'success',
			addclass: 'stack-bottomright',
			stack: stack_bottomright
		});
	});

	$('#position-3-info').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'info',
			addclass: 'stack-bottomright',
			stack: stack_bottomright
		});
	});

	$('#position-3-error').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'error',
			addclass: 'stack-bottomright',
			stack: stack_bottomright
		});
	});

	$('#position-3-dark').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-dark stack-bottomright',
			icon: 'fa fa-user',
			stack: stack_bottomright
		});
	});

	$('#position-4-primary').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-primary stack-bar-top',
			icon: 'fa fa-twitter',
			stack: stack_bar_top,
			width: "100%"
		});
	});

	$('#position-4-notice').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'stack-bar-top',
			stack: stack_bar_top,
			width: "100%"
		});
	});

	$('#position-4-success').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'success',
			addclass: 'stack-bar-top',
			stack: stack_bar_top,
			width: "100%"
		});
	});

	$('#position-4-info').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'info',
			addclass: 'stack-bar-top',
			stack: stack_bar_top,
			width: "100%"
		});
	});

	$('#position-4-error').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'error',
			addclass: 'stack-bar-top',
			stack: stack_bar_top,
			width: "100%"
		});
	});

	$('#position-4-dark').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-dark stack-bar-top',
			icon: 'fa fa-user',
			stack: stack_bar_top,
			width: "100%"
		});
	});

	$('#position-5-primary').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-primary stack-bar-bottom',
			icon: 'fa fa-twitter',
			stack: stack_bar_bottom,
			width: "70%"
		});
	});

	$('#position-5-notice').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'stack-bar-bottom',
			stack: stack_bar_bottom,
			width: "70%"
		});
	});

	$('#position-5-success').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'success',
			addclass: 'stack-bar-bottom',
			stack: stack_bar_bottom,
			width: "70%"
		});
	});

	$('#position-5-info').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'info',
			addclass: 'stack-bar-bottom',
			stack: stack_bar_bottom,
			width: "70%"
		});
	});

	$('#position-5-error').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			type: 'error',
			addclass: 'stack-bar-bottom',
			stack: stack_bar_bottom,
			width: "70%"
		});
	});

	$('#position-5-dark').click(function() {
		var notice = new PNotify({
			title: 'Notification',
			text: 'Some notification text.',
			addclass: 'notification-dark stack-bar-bottom',
			icon: 'fa fa-user',
			stack: stack_bar_bottom,
			width: "70%"
		});
	});

	/*
	Desktop Notifications Code
	*/
	$.each(['notice', 'error', 'info', 'success'], function( i, type ) {
		$( '#desktop-' + type ).click(function() {
			PNotify.desktop.permission();
			(new PNotify({
				title: 'Desktop ' + type.charAt(0).toUpperCase() + type.slice(1),
				text: 'If you\'ve given me permission, I\'ll appear as a desktop notification. If you haven\'t, I\'ll still appear as a regular notice.',
				type: type,
				desktop: {
					desktop: true
				}
			})).get().click(function() {
				alert('Hey! You clicked the desktop notification!');
			});
		});
	});

	$('#desktop-sticky').click(function() {
		PNotify.desktop.permission();
		(new PNotify({
			title: 'Sticky Desktop Notice',
			text: 'I\'m a sticky notice, so you\'ll have to close me yourself. (Some systems don\'t allow sticky notifications.) If you\'ve given me permission, I\'ll appear as a desktop notification. If you haven\'t, I\'ll still appear as a regular notice.',
			hide: false,
			desktop: {
				desktop: true
			}
		})).get().click(function() {
			alert('Hey! You clicked the desktop notification!');
		});
	});

	$('#desktop-custom').click(function() {
		PNotify.desktop.permission();
		(new PNotify({
			title: 'Desktop Custom Icon',
			text: 'If you\'ve given me permission, I\'ll appear as a desktop notification. If you haven\'t, I\'ll still appear as a regular notice.',
			desktop: {
				desktop: true,
				icon: 'assets/images/!happy-face.png'
			}
		})).get().click(function() {
			alert('Hey! You clicked the desktop notification!');
		});
	});

}).apply( this, [ jQuery ]);