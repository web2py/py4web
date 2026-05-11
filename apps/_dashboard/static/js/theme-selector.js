/**
 * Dashboard Theme Toggle
 *
 * Sets data-theme="light" or data-theme="dark" on <html> (Pico.css convention).
 * Persists the user's choice in localStorage; otherwise honors the OS preference.
 *
 * Public API:
 *   setDashboardTheme("light" | "dark" | "auto")
 *   toggleDashboardTheme()
 */
(function () {
  "use strict";

  var STORAGE_KEY = "py4web-dashboard-theme";
  var THEMES = ["light", "dark", "auto"];

  function systemTheme() {
    if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
      return "dark";
    }
    return "light";
  }

  function storedTheme() {
    try {
      var v = localStorage.getItem(STORAGE_KEY);
      return THEMES.indexOf(v) !== -1 ? v : null;
    } catch (err) {
      return null;
    }
  }

  function persist(theme) {
    try { localStorage.setItem(STORAGE_KEY, theme); } catch (err) { /* ignore */ }
  }

  function effectiveTheme(choice) {
    return choice === "auto" ? systemTheme() : choice;
  }

  function applyTheme(choice) {
    var selected = THEMES.indexOf(choice) !== -1 ? choice : "auto";
    document.documentElement.setAttribute("data-theme", effectiveTheme(selected));
    persist(selected);
    syncButtons(selected);
  }

  function syncButtons(choice) {
    var buttons = document.querySelectorAll("[data-theme-toggle]");
    var effective = effectiveTheme(choice);
    for (var i = 0; i < buttons.length; i += 1) {
      var b = buttons[i];
      b.setAttribute("aria-label", "Switch to " + (effective === "dark" ? "light" : "dark") + " mode");
      b.setAttribute("data-current-theme", effective);
      // If the button contains a label span, update its text
      var label = b.querySelector("[data-theme-label]");
      if (label) {
        label.textContent = effective === "dark" ? "☀ Light" : "☾ Dark";
      }
    }
  }

  function toggle() {
    var current = effectiveTheme(storedTheme() || "auto");
    applyTheme(current === "dark" ? "light" : "dark");
  }

  function init() {
    applyTheme(storedTheme() || "auto");

    // React to system theme changes when in auto mode
    if (window.matchMedia) {
      var mq = window.matchMedia("(prefers-color-scheme: dark)");
      var listener = function () {
        if ((storedTheme() || "auto") === "auto") applyTheme("auto");
      };
      if (mq.addEventListener) mq.addEventListener("change", listener);
      else if (mq.addListener) mq.addListener(listener);
    }
  }

  window.setDashboardTheme = applyTheme;
  window.toggleDashboardTheme = toggle;

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
