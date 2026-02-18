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
  var CONFIG_CACHE = {};
  var ACTIVE_THEME = null;
  var ACTIVE_THEME_CONFIG = null;
  var DEFAULT_THEME_CONFIG = {
    favicon: "themes/AlienDark/favicon.ico",
    widget: "themes/AlienDark/widget.gif",
    appFavicon: "",
    description: "",
    version: "",
    author: "",
    homepage: "",
    screenshot: ""
  };

  function resolveAssetUrl(path) {
    try {
      return new URL(path, document.baseURI).toString();
    } catch (err) {
      return path;
    }
  }

  function applyThemeToAppIcons(parent, config) {
    if (!config || !config.appFavicon) {
      return;
    }
    var appIconUrl = resolveAssetUrl(config.appFavicon);
    var scope = parent && typeof parent.querySelectorAll === "function" ? parent : document;
    var icons = scope.querySelectorAll("button.btn-app img[src*='favicon']");
    for (var i = 0; i < icons.length; i += 1) {
      var icon = icons[i];
      if (!icon.getAttribute("data-original-src")) {
        icon.setAttribute("data-original-src", icon.getAttribute("src"));
      }
      if (icon.getAttribute("src") !== appIconUrl) {
        icon.setAttribute("src", appIconUrl);
      }
    }
  }

  function parseThemeToml(text) {
    var config = {};
    var lines = text.split(/\r?\n/);
    for (var i = 0; i < lines.length; i += 1) {
      var line = lines[i].trim();
      if (!line || line[0] === "#") {
        continue;
      }
      var parts = line.split("=");
      if (parts.length < 2) {
        continue;
      }
      var key = parts[0].trim();
      var raw = parts.slice(1).join("=").trim();
      if ((raw[0] === '"' && raw[raw.length - 1] === '"') || (raw[0] === "'" && raw[raw.length - 1] === "'")) {
        raw = raw.slice(1, -1);
      }
      config[key] = raw;
    }
    return config;
  }

  function loadThemeConfig(theme) {
    if (CONFIG_CACHE[theme]) {
      return Promise.resolve(CONFIG_CACHE[theme]);
    }
    return fetch("themes/" + theme + "/theme.toml", { cache: "no-cache" })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Theme config not found");
        }
        return response.text();
      })
      .then(function (text) {
        var parsed = parseThemeToml(text);
        var merged = Object.assign({}, DEFAULT_THEME_CONFIG, parsed);
        if (!parsed.favicon) {
          merged.favicon = "themes/" + theme + "/favicon.ico";
        }
        if (!parsed.widget) {
          merged.widget = "themes/" + theme + "/widget.gif";
        }
        if (!parsed.appFavicon) {
          merged.appFavicon = "themes/" + theme + "/favicon.ico";
        }
        CONFIG_CACHE[theme] = merged;
        return merged;
      })
      .catch(function () {
        CONFIG_CACHE[theme] = DEFAULT_THEME_CONFIG;
        return DEFAULT_THEME_CONFIG;
      });
  }

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
    if (themes.length === 0) {
      return null;
    }
    // Prefer AlienDark if available, otherwise use first alphabetically
    if (themes.indexOf("AlienDark") !== -1) {
      return "AlienDark";
    }
    var fallback = themes.length > 0 ? themes[0] : "AlienDark";
    return fallback;
  }

  /**
   * Retrieves the previously stored theme, prioritizing backend settings.
   * Order of preference:
   * 1. SELECTED_THEME from backend (set in user_settings.toml)
   * 2. localStorage (browser fallback)
   * 3. null (will use default theme)
   * 
   * @returns {string|null} The stored theme name if valid, null otherwise
   */
  function getStoredTheme() {
    var themes = getAvailableThemes();
    
    // First check backend-provided theme (from user_settings.toml)
    if (typeof SELECTED_THEME !== 'undefined' && SELECTED_THEME) {
      if (themes.indexOf(SELECTED_THEME) !== -1) {
        return SELECTED_THEME;
      }
    }
    
    // Fallback to localStorage
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      if (stored && themes.indexOf(stored) !== -1) {
        return stored;
      }
    } catch (err) {
      return null;
    }
    return null;
  }

  /**
   * Dynamically loads theme-specific JavaScript file if it exists.
   * Themes can provide custom JavaScript code that executes when the theme is activated.
   * This allows themes to modify behavior, initialize custom components, etc.
   * 
   * @param {string} theme - The theme name to load JavaScript for
   */
  function loadThemeScript(theme) {
    var scriptPath = "themes/" + theme + "/theme.js";
    
    // Check if the script is already loaded to avoid duplicates
    var existingScript = document.querySelector('script[data-theme-script="' + theme + '"]');
    if (existingScript) {
      // Script already loaded, don't load again
      return;
    }
    
    // Remove any previously loaded theme scripts (from other themes)
    var oldScripts = document.querySelectorAll('script[data-theme-script]');
    for (var i = 0; i < oldScripts.length; i += 1) {
      var oldScript = oldScripts[i];
      if (oldScript.getAttribute("data-theme-script") !== theme) {
        oldScript.parentNode.removeChild(oldScript);
      }
    }
    
    // Create and inject the script
    var script = document.createElement('script');
    script.setAttribute('data-theme-script', theme);
    script.src = scriptPath + "?t=" + new Date().getTime(); // Cache bust
    script.defer = false;
    
    // Optionally handle script load/error events
    script.onload = function () {
      // Theme script loaded successfully
    };
    
    script.onerror = function () {
      // Theme script doesn't exist or failed to load - that's OK, not all themes have JS
    };
    
    document.head.appendChild(script);
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
    
    loadThemeConfig(selected).then(function (config) {
      // Load theme CSS file by updating the link element href
      var link = document.getElementById("dashboard-theme");
      if (link) {
        var newHref = "themes/" + selected + "/theme.css?v=" + new Date().getTime();
        link.setAttribute("href", newHref);
      }
      
      // Update browser favicon based on theme config
      var favicon = document.querySelector("link[rel='shortcut icon']");
      if (favicon) {
        var faviconUrl = config.favicon || DEFAULT_THEME_CONFIG.favicon;
        favicon.setAttribute("href", faviconUrl);
      }

      // Update the top-left spinner image based on theme config
      var spinner = document.querySelector("img.spinner-top");
      if (spinner) {
        var originalSpinnerSrc = spinner.getAttribute("data-original-src");
        if (!originalSpinnerSrc) {
          originalSpinnerSrc = spinner.getAttribute("src");
          spinner.setAttribute("data-original-src", originalSpinnerSrc);
        }
        var spinnerUrl = config.widget || originalSpinnerSrc;
        spinner.setAttribute("src", spinnerUrl);
      }

      ACTIVE_THEME = selected;
      ACTIVE_THEME_CONFIG = config;
      applyThemeToAppIcons(document, config);
      
      // Set data attribute for CSS selectors that might use it
      document.documentElement.setAttribute("data-theme", selected);

      // Dynamically load theme-specific JavaScript if it exists
      loadThemeScript(selected);
      
      // Persist theme selection to localStorage (for immediate fallback)
      try {
        localStorage.setItem(STORAGE_KEY, selected);
      } catch (err) {
      }
      
      // Persist theme selection to backend (user_settings.toml)
      saveThemeToBackend(selected);
      
      // Update all theme selector dropdowns to reflect current theme
      syncSelectors(selected);
      if (typeof SELECTED_THEME !== 'undefined') {
        SELECTED_THEME = selected;
      }
    });
  }

  /**
   * Saves theme selection to backend via save_theme endpoint.
   * Silently fails if backend is unavailable or user not logged in.
   * 
   * @param {string} theme - The theme name to save
   */
  function saveThemeToBackend(theme) {
    // Only save if user is logged in (USER_ID is defined)
    if (typeof USER_ID === 'undefined' || !USER_ID) {
      return;
    }
    
    fetch('../save_theme', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ theme: theme })
    }).catch(function () {
      // Silently ignore errors (e.g., not logged in, network issues)
    });
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
   * Watches for dynamically-rendered icons (from Vue) and initializes them.
   * Loads the previously saved theme, or applies the default if none saved.
   */
  function init() {
    var themes = getAvailableThemes();
    if (themes.length === 0) {
      throw new Error("No dashboard themes found. Add a theme folder under static/themes.");
    }
    
    // Helper function to initialize favicon icons with proper tracking
    var initFaviconIcons = function(parent) {
      var appIcons = parent.querySelectorAll("img[src*='favicon']");
      for (var i = 0; i < appIcons.length; i += 1) {
        var img = appIcons[i];
        var currentSrc = img.getAttribute("src");
        // Ensure data-original-src is set (either from attribute or from current src)
        if (!img.getAttribute("data-original-src") && currentSrc) {
          img.setAttribute("data-original-src", currentSrc);
        }
      }
    };
    
    // Initialize static icons
    initFaviconIcons(document);
    
    // Watch for dynamically-rendered icons and initialize them
    // This handles Vue.js rendering the app list after the script loads
    if (typeof MutationObserver !== 'undefined') {
      var observer = new MutationObserver(function(mutations) {
        // Check if any added nodes contain favicon images
        for (var i = 0; i < mutations.length; i += 1) {
          var mutation = mutations[i];
          if (mutation.addedNodes.length > 0) {
            for (var j = 0; j < mutation.addedNodes.length; j += 1) {
              var node = mutation.addedNodes[j];
              // Only process element nodes
              if (node.nodeType === 1) {
                // Check if the node itself is an img with favicon
                if (node.tagName === 'IMG' && node.src && node.src.includes('favicon')) {
                  if (!node.getAttribute('data-original-src')) {
                    node.setAttribute('data-original-src', node.getAttribute('src'));
                  }
                  if (ACTIVE_THEME_CONFIG) {
                    applyThemeToAppIcons(node.parentNode || document, ACTIVE_THEME_CONFIG);
                  }
                }
                // Check if the node contains img children with favicon
                if (typeof node.querySelectorAll === 'function') {
                  initFaviconIcons(node);
                  if (ACTIVE_THEME_CONFIG) {
                    applyThemeToAppIcons(node, ACTIVE_THEME_CONFIG);
                  }
                }
              }
            }
          }
        }
      });
      
      // Watch the document body for changes
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    }
    
    var initial = getStoredTheme() || getDefaultTheme();
    if (!initial) {
      throw new Error("Unable to determine a default dashboard theme.");
    }
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
