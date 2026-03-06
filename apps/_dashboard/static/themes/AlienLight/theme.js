/* AlienLight Theme JavaScript
   
   This file can contain theme-specific JavaScript code that needs to run
   when the AlienLight theme is active. Currently, it's a placeholder for
   future functionality.
   
   To enable theme-specific code:
   1. Add your JavaScript here
   2. The theme-selector.js will automatically load this file when AlienLight
      is selected as the active theme
*/

(function() {
  var ACE_THEME = "ace/theme/chrome";

  var applyAceTheme = function() {
    if (!window.app || !app.vue) {
      return false;
    }

    if (app.vue.editor && typeof app.vue.editor.setTheme === "function") {
      app.vue.editor.setTheme(ACE_THEME);
    }

    if (!app.vue.__alienLightAceHooked && typeof app.vue.activate_editor === "function") {
      var originalActivate = app.vue.activate_editor.bind(app.vue);
      app.vue.activate_editor = function(path, payload) {
        originalActivate(path, payload);
        if (app.vue.editor && typeof app.vue.editor.setTheme === "function") {
          app.vue.editor.setTheme(ACE_THEME);
        }
      };
      app.vue.__alienLightAceHooked = true;
    }

    return true;
  };

  var attempts = 0;
  var maxAttempts = 20;
  var retry = function() {
    attempts += 1;
    if (applyAceTheme() || attempts >= maxAttempts) {
      return;
    }
    setTimeout(retry, 150);
  };

  retry();
})();
