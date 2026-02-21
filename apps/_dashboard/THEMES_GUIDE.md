# PY4WEB Dashboard Themes Guide

## Overview

The `_dashboard` app supports dynamic theme switching with persisted user preference.
Themes are discovered from `static/themes/` and can be switched without a page reload.

Current built-in themes:
- **AlienDark** (default dark UI)
- **AlienLight** (light UI)

---

## How It Works

### Runtime Flow

1. Backend loads `selected_theme` from `user_settings.toml`
2. Backend normalizes it against currently available themes
3. Template renders:
   - `themes` list
   - `selected_theme`
   - `SELECTED_THEME` JavaScript global
4. `static/js/theme-selector.js` initializes and applies the selected theme
5. Selection is stored in:
   - backend (`user_settings.toml`)
   - browser (`localStorage`)

### Theme Discovery

Themes are discovered by scanning folders in:

`apps/_dashboard/static/themes/`

Any subdirectory (not starting with `.`) is treated as a theme and appears in the selector.

---

## Theme Folder Structure

A minimal theme folder:

```text
static/themes/MyTheme/
├── theme.toml
├── theme.css
├── theme.js        # optional
├── favicon.ico     # optional
└── widget.gif      # optional
```

### `theme.toml`

Example:

```toml
name = "MyTheme"
description = "Custom dashboard theme"
version = "1.0.0"
author = "Your Name"
homepage = "https://example.com"
screenshot = "widget.gif"
```

Optional keys used by the selector if present:
- `favicon`
- `widget`
- `appFavicon`

If omitted, defaults are inferred from the current theme folder.

### `theme.css`

Use CSS custom properties for consistency:

```css
:root {
  --bg-primary: #ffffff;
  --text-primary: #222;
  --accent: #0074d9;
  --accent-dark: #0052a3;
  --bg-secondary: #f5f5f5;
  --border-color: #d1d1d1;
}
```

### `theme.js` (optional)

Loaded dynamically when the theme is activated.
Use this for behavior that cannot be expressed in CSS (for example ACE editor integration).

---

## Frontend Components

Main file: `apps/_dashboard/static/js/theme-selector.js`

Key responsibilities:
- detect available themes from the selector
- determine initial theme (`SELECTED_THEME` → localStorage → default)
- load `theme.toml`
- swap `theme.css` at runtime
- update favicon/spinner/app icons
- load optional `theme.js`
- persist selection via `POST ../save_theme`
- keep all selectors (`[data-theme-selector]`) synchronized

Public API:
- `window.setDashboardTheme(theme)`

---

## Backend Components

Main file: `apps/_dashboard/__init__.py`

Key functions:
- `get_available_themes()`
- `normalize_selected_theme(selected_theme, available_themes=None)`
- `load_user_settings()` / `save_user_settings()`
- `@action("save_theme", method="POST")`

### Theme Validation

Backend normalization guarantees that stale values (for example removed themes) do not break rendering.
If a stored theme is unavailable:
1. use `AlienDark` if present
2. otherwise use the first available theme
3. otherwise fall back to `AlienDark`

`save_theme` also validates that the requested theme exists.

---

## Template Requirements

In dashboard templates, keep these elements:

```html
<script>
  var SELECTED_THEME = '[[= selected_theme or "AlienDark" ]]';
</script>

<link id="dashboard-theme" rel="stylesheet" href="themes/[[= selected_theme or 'AlienDark' ]]/theme.css">

<select id="dashboard-theme-select" data-theme-selector onchange="setDashboardTheme(this.value)">
  [[for theme in themes:]]
    <option value="[[=theme]]" [[='selected' if theme == selected_theme else '']]>[[=theme]]</option>
  [[pass]]
</select>
```

Important: always bind the CSS link to `selected_theme` from backend context; do not hardcode a theme path.

---

## Creating a Custom Theme

1. Create `static/themes/MyTheme/`
2. Add `theme.toml`
3. Add `theme.css`
4. Optionally add `theme.js`, `favicon.ico`, `widget.gif`
5. Refresh dashboard and select the theme

No backend code changes are required.

---

## Troubleshooting

### Theme not in dropdown
- verify folder exists under `static/themes/`
- verify folder name does not start with `.`
- hard refresh browser

### Theme not applied on first load
- verify template CSS link uses `selected_theme`
- check rendered HTML for `id="dashboard-theme"`

### Theme selection not persisted
- ensure user is logged in
- verify `POST ../save_theme` succeeds
- check `apps/_dashboard/user_settings.toml` is writable

### Theme script not running
- verify `theme.js` exists and has valid JavaScript
- check browser console for syntax/runtime errors

---

## Notes

- The current dashboard implementation uses a single base layout.
- Theme-specific visual customization is expected to be done primarily through CSS variables and optional `theme.js` behavior.
