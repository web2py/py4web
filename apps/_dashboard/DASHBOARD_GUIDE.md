# PY4WEB Dashboard Guide

## Overview

The `_dashboard` app is a special administrative application that provides a web-based interface for managing all py4web applications. It has elevated privileges and follows a modular structure similar to standard py4web apps, but with intentional differences due to its administrative role.

## Table of Contents

- [Architecture](#architecture)
- [Key Differences from Standard Apps](#key-differences-from-standard-apps)
- [File Structure](#file-structure)
- [Theming](#theming)
- [Authentication & Authorization](#authentication--authorization)
- [API Endpoints](#api-endpoints)
- [Development Guide](#development-guide)
- [Security Considerations](#security-considerations)

---

## Architecture

The dashboard follows py4web's modular app structure but keeps most logic in a
single module because it is an administrative surface:

```
_dashboard/
├── __init__.py          # App initialization, fixtures, actions, APIs
├── settings.py          # Configuration (MODE, FOLDER, etc.)
├── utils.py             # File operations, git helpers, safe joins
├── diff2kryten.py       # Git diff visualization
├── templates/           # YATL templates
├── static/              # Frontend assets (CSS, JS)
└── translations/        # i18n files
```

### Import Dependency Graph

```
__init__.py
    ↓ ↓ ↓
settings.py  diff2kryten.py  utils.py
```

**No circular imports** - The import chain is a clean directed acyclic graph (DAG).

---

## Key Differences from Standard Apps

The dashboard intentionally differs from typical py4web apps due to its administrative nature:

### 1. **No Database Instance**

Unlike standard apps that define `db = DAL(...)` in `common.py`, the dashboard has **no database of its own**. Instead, it:

- Accesses other apps' databases dynamically via `Reloader.MODULES`
- Uses `error_logger.database_logger.db` for ticket management
- Wraps external databases with `make_safe()` to prevent forbidden method access

### 2. **Custom Authentication**

The dashboard uses a **custom `Logged` fixture** instead of the standard `Auth` framework:

- **Why:** Dashboard manages all apps including those with Auth, so it can't depend on any app's Auth
- **How:** Password-based authentication using `PY4WEB_PASSWORD_FILE` environment variable
- **Where:** Defined in `__init__.py`

### 3. **Minimal Fixtures**

Standard apps typically have: `db`, `session`, `auth`, `cache`, `flash`, `T`

Dashboard only has: `session`, `T` (translator), and `Logged` (custom auth)

**Reason:** Dashboard is primarily an API/admin interface that doesn't need form helpers, caching, or flash messages.

### 4. **Single-Module Actions**

There is no `controllers.py` or `common.py`. All actions, fixtures, and helpers
live in `__init__.py`, while `utils.py` holds shared helpers.

---

## File Structure

### `__init__.py` - App Initialization, Fixtures, and Actions

Registers the app with py4web and exposes all actions.

**Key Elements:**
- Defines `session`, `T`, and `Logged`
- Declares all routes and API endpoints
- Uses `session_secured` and `authenticated` factories for access control

---

### `settings.py` - Configuration

Defines configuration from environment variables.

**Environment Variables:**
- `PY4WEB_DASHBOARD_MODE`: `"demo"`, `"readonly"`, `"full"`, or `"none"`
- `PY4WEB_APPS_FOLDER`: Path to apps directory (required)
- `PY4WEB_APP_NAMES`: Comma-separated list of exposed app names (optional)
- `PY4WEB_PASSWORD_FILE`: Path to password file for authentication

**Modes:**
- `none`: Dashboard disabled
- `demo`: Read-only with mock authentication
- `readonly`: View apps and settings but cannot modify
- `full`: Complete administrative access

---

### `utils.py` - Shared Utilities

```python
def make_safe(db):
    """Wraps database field defaults/updates to prevent cross-app method access."""
    ...
```

Contains `make_safe()`, `safe_join()`, git helpers, and reference field helpers.

**Purpose:** When dashboard accesses another app's database schema, field defaults like `default=lambda: get_user()` might reference functions that don't exist in dashboard's context. The `make_safe()` wrapper prevents crashes by wrapping these callables in error handlers.

---

### Route Handlers

All dashboard endpoints are defined in `__init__.py` using standard py4web action patterns:

- **Public endpoints:** no authentication required
- **Authenticated endpoints:** use `@session_secured` or `@action.uses(Logged(session))`
- **API endpoints:** use `@catch_errors` to return `{"status": "success/error", ...}`
- **Template endpoints:** use `@action.uses("template.html", session, T)`

### Setting Dashboard Password

```bash
# Using CLI
py4web set_password

# Or manually
python -c "from pydal.validators import CRYPT; print(CRYPT()('mypassword')[0])" > password.txt
export PY4WEB_PASSWORD_FILE=password.txt
```

---

## Theming

The dashboard supports multiple built-in themes (AlienDark, AlienLight) with a fully extensible theming system. Users can switch themes dynamically without page reload, with preferences persisted to the backend.

**For comprehensive theming documentation**, see [THEMES_GUIDE.md](THEMES_GUIDE.md).

### Quick Overview

**Currently Available Themes:**
- **AlienDark** - Modern dark theme with cyan accents (default)
- **AlienLight** - Professional light theme with blue accents

**Key Features:**
- Dynamic theme discovery from `static/themes/` folder
- CSS custom properties (variables) for styling
- Optional theme-specific JavaScript initialization
- Theme metadata in `theme.toml`
- User preference persisted to `user_settings.toml`

### Theme System Architecture

```
static/themes/{ThemeName}/
├── theme.toml              # Metadata (name, description, author, etc.)
├── theme.css               # Styling with CSS variables
├── theme.js                # Optional JS initialization
├── favicon.ico             # Browser tab icon
├── widget.gif              # Loading spinner
└── templates/              # Optional custom templates
    ├── index.html
    └── ...
```

**Frontend System:**
- `js/theme-selector.js` - Manages all client-side theme switching
- Loads theme CSS dynamically by updating `<link id="dashboard-theme">`
- Persists selection to localStorage and backend
- Synchronizes multiple theme selectors on same page

**Backend System:**
- `get_available_themes()` - Scans `static/themes/` folder
- `normalize_selected_theme()` - Validates stored/requested theme values against available themes
- `load_user_settings()` / `save_user_settings()` - Persists theme selection
- `@action("save_theme")` - HTTP endpoint for theme persistence

### Adding a Custom Theme

1. **Create folder:** `static/themes/MyTheme/`
2. **Create `theme.toml`:**
   ```toml
   name = "My Theme"
   description = "Brief description"
   version = "1.0.0"
   author = "Your Name"
   ```
3. **Create `theme.css`:**
   ```css
   :root {
     --bg-primary: white;
     --text-primary: #333;
     --accent: #0074d9;
     --accent-dark: #0052a3;
     --bg-secondary: #f5f5f5;
     --border-color: #d1d1d1;
   }
   body { background: var(--bg-primary); color: var(--text-primary); }
   ```
4. **Optional - Add assets:** `favicon.ico`, `widget.gif`, custom `templates/`
5. **Optional - Add behavior:** `theme.js` for theme-specific JavaScript

**That's it!** The theme automatically appears in the dropdown.

### Theme Selector UI

Dropdowns appear on all dashboard pages:

```html
<select id="dashboard-theme-select" data-theme-selector onchange="setDashboardTheme(this.value)">
  [[for theme in themes:]]
    <option value="[[=theme]]">[[=theme]]</option>
  [[pass]]
</select>
```

**Multiple selectors on the same page stay synchronized** via `data-theme-selector` attribute.

### Best Practices

1. **Use CSS Variables** - Define all colors in `:root`, never hardcode
2. **Foundation Pattern** - Override only the styles you need, let defaults cascade
3. **Metadata Matters** - Complete `theme.toml` helps users understand your theme
4. **Test All Pages** - Verify on main dashboard, dbadmin, and other pages
5. **Accessibility** - Ensure sufficient text contrast (WCAG AA minimum)
6. **Dynamic Features** - Use `theme.js` for ACE editor config, custom UI hooks, etc.

### How Theming Works (Flow Diagram)

```
Page loads
  ↓
Backend loads theme from user_settings.toml
  ↓
Renders HTML with SELECTED_THEME variable
  ↓
theme-selector.js runs
  ↓
getStoredTheme() checks: Backend → localStorage → default
  ↓
loadThemeConfig() fetches theme.toml
  ↓
applyTheme() orchestrates:
  • Update CSS link href
  • Update favicon
  • Load theme.js
  • Save to localStorage + backend
  • Sync all selectors
  ↓
Theme is now active
```

### Persistence

Theme selection is saved in two places:

1. **Backend** - `apps/_dashboard/user_settings.toml`
   ```toml
   selected_theme = "AlienDark"
   ```
   Survives browser cache clear / private browsing

2. **Browser** - localStorage key: `py4web-dashboard-theme`
   Provides immediate fallback if backend unavailable

**Selection Priority:**
1. Backend setting (from `user_settings.toml`)
2. Browser storage (from localStorage)
3. Default theme (AlienDark if available, else first alphabetically)

### Troubleshooting Themes

**Theme not appearing in dropdown:**
- Verify folder exists: `static/themes/MyTheme/`
- Hard refresh browser (Ctrl+Shift+R)
- Restart dashboard to rescan folder

**CSS not loading:**
- Check Network tab for 4xx errors on `themes/MyTheme/theme.css`
- Verify `:root` block has all required CSS variables
- Check Browser Console for JavaScript errors in theme.js

**JavaScript not running:**
- Verify `theme.js` is valid with a linter
- Use retry logic if depending on Vue app (may not be ready yet)
- Check Console for syntax errors

**Settings not persisting:**
- Verify `apps/_dashboard/user_settings.toml` is writable
- Ensure you're logged in (theme save requires `USER_ID`)
- Check Network tab - POST `/save_theme` should return `{"status": "success"}`

---

## Advanced Theming

For advanced features like:
- Theme-specific templates (custom layouts)
- ACE editor theme configuration
- Favicon management
- Complex initialization patterns

See [THEMES_GUIDE.md - Advanced Patterns](THEMES_GUIDE.md#advanced-patterns) section.

---

## API Endpoints

### App Management

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/version` | GET | No | Returns py4web version |
| `/index` | GET | No | Dashboard UI (login if needed) |
| `/login` | POST | No | Authenticate user |
| `/logout` | POST | Session | Clear session |
| `/apps` | GET | Yes | List all applications |
| `/reload` | GET | Yes | Reload all apps |
| `/reload/<name>` | GET | Yes | Reload specific app |
| `/delete_app/<name>` | POST | Yes | Delete app (archives first) |
| `/new_app` | POST | Yes | Create/update app from scaffold, web, or upload |

### File Operations

| Endpoint | Method | Auth | Mode | Description |
|----------|--------|------|------|-------------|
| `/walk/<path:path>` | GET | Yes | Any | Get folder tree structure |
| `/load/<path:path>` | GET | Yes | Any | Load text file content |
| `/load_bytes/<path:path>` | GET | Yes | Any | Load binary file |
| `/save/<path:path>` | POST | Yes | Full | Save file content |
| `/delete/<path:path>` | POST | Yes | Full | Delete file |
| `/new_file/<app>/<path>` | POST | Yes | Any | Create new file |
| `/packed/<app>.zip` | GET | Yes | Any | Download app as ZIP |

### Database Management

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/dbadmin/<app>/<db>/<table>` | GET | Yes | CRUD interface for table |
| `/rest/<app>` | GET/POST/PUT/DELETE | Yes | REST API for app databases |

**DBAdmin Features:**

- **Grid Interface:** Browse, search, sort, and paginate table records
- **Clickable Reference Fields:** Reference fields are automatically rendered as clickable links that navigate to the referenced record's table
- **Supported Field Types:** `id`, `string`, `integer`, `double`, `time`, `date`, `datetime`, `boolean`, `reference`, `big-reference`
- **Smart Display:** Reference fields show the referenced table's `_format` value (e.g., user name instead of ID)
- **Missing References:** Shows "#{id}(missing)" if referenced record doesn't exist

### Error Tracking

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/tickets` | GET | Yes | List error tickets |
| `/tickets/search` | GET | Yes | Search tickets with Grid UI |
| `/ticket/<uuid>` | GET | Yes | View ticket details |
| `/clear` | POST | Yes | Clear all tickets |

### Development Tools

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/info` | GET | Yes | Python modules and versions |
| `/routes` | GET | Yes | All registered routes |
| `/translations/<app>` | GET | Yes | Translation editor UI |
| `/api/translations/<app>` | GET/POST | Yes | Get/update translations |
| `/api/translations/<app>/search` | GET | Yes | Find translatable strings |

### Git Integration

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/gitlog/<project>` | GET | Yes | View commit history |
| `/gitshow/<project>/<commit>` | GET | Yes | View commit diff |
| `/swapbranch/<project>` | POST | Yes | Switch git branch |

---

## Authentication & Authorization

### Login Flow

1. Client sends POST request to `/login` with password in JSON body
2. Server validates against encrypted password in `PY4WEB_PASSWORD_FILE` (skipped in `demo`)
3. On success, sets `session["user"] = {"id": 1}`
4. Subsequent requests include session cookie which `Logged` fixture validates

### Setting Dashboard Password

Use CLI: `py4web set_password` or manually encrypt password and save to file, then set `PY4WEB_PASSWORD_FILE` environment variable.

### Working with External Databases

```python
@action("dbadmin/<app_name>/<db_name>/<table_name>")
@action.uses(Logged(session), "dbadmin.html")
def dbadmin_table(app_name, db_name, table_name):
    # Get the app module
    module = Reloader.MODULES.get(app_name)
    if not module:
        abort(404)
    
    # Get the database instance
    db = getattr(module, db_name, None)
    if not db:
        abort(404)
    
    # CRITICAL: Wrap before using
    make_safe(db)
    
    # Now safe to use
    def make_grid():
        table = db[table_name]

        # Customize reference fields to be clickable
        for field in table:
            if field.type_name in ("reference", "big-reference", "list:reference"):
                field.represent = make_admin_reference_represent(app_name, db_name, field)

        return Grid(table)
    
    grid = action.uses(db)(make_grid)()
    return dict(grid=grid)
```

**Key Points:**

- Always call `make_safe(db)` before accessing external databases
- Reference fields can be customized with `field.represent` functions
- Use `XML()` from `yatl.helpers` to return HTML content
- The Grid helper automatically uses field `represent` functions for rendering

### Using Grid with External DB

The `Grid` helper needs the database as a fixture. Use the pattern:

```python
def make_grid():
    make_safe(db)
    return Grid(db.table_name, ...)

grid = action.uses(db)(make_grid)()
```

This ensures proper DB connection lifecycle.

---

## Security Considerations

### 1. **Environment-Based Authentication**

The dashboard password is stored outside the codebase:

```bash
export PY4WEB_PASSWORD_FILE=/secure/path/password.txt
```

**Never commit password files to version control.**

### 2. **Mode Restrictions**

Always guard dangerous operations:

```python
if MODE != "full":
    abort(403)  # or raise HTTP(403)
```

### 3. **Path Traversal Protection**

Use `safe_join()` from `utils.py`:

```python
from .utils import safe_join

path = safe_join(FOLDER, user_provided_path) or abort(400)
```

This prevents `../../../etc/passwd` attacks.

### 4. **Database Wrapping**

Always call `make_safe(db)` before accessing external databases to prevent forbidden method access.

### 5. **Session Protection**

All POST/PUT/DELETE actions require a valid session cookie and pass through `Logged`.

### 6. **App Name Filtering**

Limit visible apps via `PY4WEB_APP_NAMES` environment variable (comma-separated list).

---

## Development Guide

### Adding a New Endpoint

1. Define action in `__init__.py` using `@action`
2. Use `@session_secured` or `@action.uses(Logged(session))`
3. Use `@catch_errors` for API endpoints
4. Guard dangerous operations with mode checks (`if MODE == "full"`)

### Working with External Databases

1. Get app module from `Reloader.MODULES.get(app_name)`
2. Get database instance from module
3. **Always call `make_safe(db)` before using** to prevent security issues
4. For Grid helper, wrap the grid creation in a function and use `action.uses(db)(make_grid)()`

---


