/**
 * Dashboard Theme Selector Module
 * 
 * Manages dynamic theme switching for the py4web dashboard with browser storage persistence.
 * Themes are dynamically discovered from the select element, allowing new themes to be added
 * without code changes. Theme selection is persisted using localStorage.
 * 
 * Features:
 * - Dynamic theme detection from DOM select element
 * - localStorage persistence across sessions
 * - Automatic synchronization of multiple theme selectors
 * - Intelligent default theme selection (AlienDark if available, else first alphabetically)
 * - Graceful fallback handling for storage errors
 */
(function () {
  "use strict";

  var STORAGE_KEY = "py4web-dashboard-theme";

  /**
   * Retrieves all available themes by reading options from the theme selector dropdown.
   * This method dynamically discovers themes without requiring hardcoded lists.
   * 
   * @returns {Array<string>} Array of theme names (e.g., ["AlienDark", "AlienLight"])
   *                          Returns ["AlienDark"] as fallback if selector not found
   */
  function getAvailableThemes() {
    var selector = document.getElementById("dashboard-theme-select");
    if (selector) {
      var themes = [];
      for (var i = 0; i < selector.options.length; i += 1) {
        themes.push(selector.options[i].value);
      }
      return themes.length > 0 ? themes : ["AlienDark", "AlienLight"];
    }
    // Fallback to known themes if selector not found (useful during page load)
    return ["AlienDark", "AlienLight"];
  }

  /**
   * Determines the default theme to use when no theme is stored or invalid theme is requested.
   * 
   * Selection logic:
   * 1. If "AlienDark" is available, use it (preferred default)
   * 2. Otherwise use the first available theme (alphabetically sorted)
   * 3. Fallback to "AlienDark" if no themes available
   * 
   * @returns {string} The default theme name
   */
  function getDefaultTheme() {
    var themes = getAvailableThemes();
    // Prefer AlienDark if available, otherwise use first alphabetically
    if (themes.indexOf("AlienDark") !== -1) {
      return "AlienDark";
    }
    return themes.length > 0 ? themes[0] : "AlienDark";
  }

  /**
   * Retrieves the previously stored theme from browser localStorage, if valid.
   * Validates that the stored theme is still in the available themes list
   * (handles case where a theme was removed after being selected).
   * 
   * @returns {string|null} The stored theme name if valid and localStorage accessible,
   *                        null otherwise (will fallback to default theme)
   */
  function getStoredTheme() {
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      var themes = getAvailableThemes();
      if (stored && themes.indexOf(stored) !== -1) {
        return stored;
      }
    } catch (err) {
      return null;
    }
    return null;
  }

  /**
   * Applies a theme by:
   * 1. Validating the requested theme against available options
   * 2. Updating the theme CSS link href
   * 3. Setting data-theme attribute on document root
   * 4. Updating the favicon based on theme
   * 5. Updating app icons based on theme
   * 6. Persisting the selection to localStorage
   * 7. Syncing all theme selector dropdowns
   * 
   * @param {string} theme - The theme name to apply
   */
  function applyTheme(theme) {
    var themes = getAvailableThemes();
    var defaultTheme = getDefaultTheme();
    var selected = themes.indexOf(theme) !== -1 ? theme : defaultTheme;
    
    // Load theme CSS file by updating the link element href
    var link = document.getElementById("dashboard-theme");
    if (link) {
      link.setAttribute("href", "themes/" + selected + "/theme.css");
    }
    
    // Update browser favicon based on theme
    var favicon = document.querySelector("link[rel='shortcut icon']");
    if (favicon) {
      if (selected === "AlienLight") {
        favicon.setAttribute("href", "favicon_green.ico");
      } else {
        favicon.setAttribute("href", "favicon.ico");
      }
    }

    // Update the top-left spinner image for light theme
    var spinner = document.querySelector("img.spinner-top");
    if (spinner) {
      var originalSpinnerSrc = spinner.getAttribute("data-original-src");
      if (!originalSpinnerSrc) {
        originalSpinnerSrc = spinner.getAttribute("src");
        spinner.setAttribute("data-original-src", originalSpinnerSrc);
      }
      if (selected === "AlienLight") {
        spinner.setAttribute("src", "images/widget-transparent.gif");
      } else {
        spinner.setAttribute("src", originalSpinnerSrc);
      }
    }
    
    // Update app icons based on theme (images with favicon.ico src)
    var appIcons = document.querySelectorAll("img[src*='favicon']");
    for (var i = 0; i < appIcons.length; i += 1) {
      var img = appIcons[i];
      var currentSrc = img.getAttribute("src");
      
      // Skip if not a favicon icon
      if (!currentSrc.includes("favicon")) continue;
      
      if (selected === "AlienLight") {
        // Store original src if not already stored
        if (!img.getAttribute("data-original-src")) {
          img.setAttribute("data-original-src", currentSrc);
        }
        // Point all app icons to the dashboard's green favicon
        img.setAttribute("src", "/_dashboard/static/favicon_green.ico");
      } else {
        // Restore original favicon path
        var originalSrc = img.getAttribute("data-original-src");
        if (originalSrc && originalSrc !== "/_dashboard/static/favicon_green.ico") {
          // Use stored original
          img.setAttribute("src", originalSrc);
        } else if (currentSrc.includes("_dashboard") && currentSrc.includes("favicon_green")) {
          // Currently pointing to green, extract the original app path
          // For dashboard: /static/favicon.ico or /{app}/static/favicon.ico
          var parts = document.location.pathname.split("/");
          if (parts[1] && parts[1] !== "_dashboard") {
            img.setAttribute("src", "/" + parts[1] + "/static/favicon.ico");
          } else {
            img.setAttribute("src", "/static/favicon.ico");
          }
        } else if (currentSrc.includes("favicon_green")) {
          // Try to reconstruct original from URL pattern
          img.setAttribute("src", "/static/favicon.ico");
        }
      }
    }
    
    // Set data attribute for CSS selectors that might use it
    document.documentElement.setAttribute("data-theme", selected);
    
    // Persist theme selection to localStorage
    try {
      localStorage.setItem(STORAGE_KEY, selected);
    } catch (err) {
      // Ignore storage errors (private browsing, full storage, etc.)
    }
    
    // Update all theme selector dropdowns to reflect current theme
    syncSelectors(selected);
  }

  /**
   * Synchronizes all theme selector dropdowns on the page to the same value.
   * Allows multiple theme selectors (e.g., on different pages) to stay in sync.
   * 
   * @param {string} theme - The theme value to set on all selectors
   */
  function syncSelectors(theme) {
    var selectors = document.querySelectorAll("[data-theme-selector]");
    for (var i = 0; i < selectors.length; i += 1) {
      selectors[i].value = theme;
    }
  }

  /**
   * Initializes the theme system on page load.
   * Stores original favicon src values before applying any theme.
   * Loads the previously saved theme, or applies the default if none saved.
   */
  function init() {
    // Store all original favicon srcs before applying theme
    var appIcons = document.querySelectorAll("img[src*='favicon']");
    for (var i = 0; i < appIcons.length; i += 1) {
      var img = appIcons[i];
      var currentSrc = img.getAttribute("src");
      if (currentSrc && !img.getAttribute("data-original-src")) {
        img.setAttribute("data-original-src", currentSrc);
      }
    }
    
    var initial = getStoredTheme() || getDefaultTheme();
    applyTheme(initial);
  }

  /**
   * Public API: Exposed globally to allow HTML onclick handlers and external code
   * to trigger theme changes. Called by the theme selector dropdown's onchange event.
   * 
   * Usage: setDashboardTheme("AlienDark")
   */
  window.setDashboardTheme = applyTheme;

  // Initialize theme on page load
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
