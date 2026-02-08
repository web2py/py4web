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

The dashboard supports multiple themes using a CSS override pattern. This allows users to switch between themes dynamically without reloading the page, with theme preference persisted in browser localStorage.

### Theme System Architecture

**Folder Structure:**
```
static/
├── css/
│   ├── future.css          # Dark base stylesheet (main dashboard)
│   ├── no.css              # Light base stylesheet (dbadmin pages)
│   └── ...
├── js/
│   ├── theme-selector.js   # Theme switching logic
│   └── ...
├── themes/
│   ├── AlienDark/
│   │   └── theme.css       # Dark theme overrides
│   └── AlienLight/
│       └── theme.css       # Light theme overrides
└── ...
```

### How Theming Works

1. **Base Stylesheets:** Dashboard loads a base stylesheet (`future.css` for main dashboard, `no.css` for dbadmin) that defines the default dark theme
2. **Theme CSS Variables:** Each theme defines CSS custom properties (variables) for colors and styling
3. **Dynamic Theme Loading:** JavaScript (`theme-selector.js`) dynamically loads theme CSS files by updating the `href` of a `<link>` tag with id `dashboard-theme`
4. **Local Storage Persistence:** Selected theme is stored in browser localStorage under key `py4web-dashboard-theme`
5. **Auto-Apply:** On page load, theme-selector.js automatically applies the saved theme preference

### Available Themes

#### AlienDark
- **Description:** Dark theme with cyan accents
- **CSS Variables:**
  - `--bg-primary: black` - Main background
  - `--text-primary: #d1d1d1` - Primary text color
  - `--accent: #33BFFF` - Accent color (cyan)
  - `--accent-dark: #007a99` - Dark accent variant
  - `--bg-secondary: #1a1a1a` - Secondary background
  - `--border-color: #333` - Border color
- **File:** `static/themes/AlienDark/theme.css`

#### AlienLight
- **Description:** Light theme with blue accents
- **CSS Variables:**
  - `--bg-primary: white` - Main background
  - `--text-primary: #333` - Primary text color
  - `--accent: #0074d9` - Accent color (blue)
  - `--accent-dark: #003d74` - Dark accent variant
  - `--bg-secondary: #f5f5f5` - Secondary background
  - `--border-color: #ddd` - Border color
- **File:** `static/themes/AlienLight/theme.css`

### Using CSS Variables in Theme Files

Each theme file uses CSS custom properties for consistent styling across components:

```css
:root {
  --bg-primary: black;
  --text-primary: #d1d1d1;
  --accent: #33BFFF;
  /* ... other variables ... */
}

/* Override specific elements using variables */
body {
  background: var(--bg-primary);
  color: var(--text-primary);
}

button {
  background: var(--accent);
  color: var(--bg-primary);
}
```

### Theme Selector UI

The theme selector is visible on the main dashboard (`index.html`):

```html
<select id="dashboard-theme-select" data-theme-selector 
        onchange="setDashboardTheme(this.value)" 
        style="width: 140px">
  <option value="AlienDark">AlienDark</option>
  <option value="AlienLight">AlienLight</option>
</select>
```

**Features:**
- Dropdown positioned in top-right corner of header
- Uses `data-theme-selector` attribute for synchronization
- Calls `setDashboardTheme()` function from `theme-selector.js`
- Multiple selectors on the same page stay synchronized

### JavaScript Theme Switching (theme-selector.js)

The theme selector module is now fully dynamic, detecting themes from the select element. See [theme-selector.js](static/js/theme-selector.js) for the implementation.

**Key Features:**
- `getAvailableThemes()` - Dynamically reads themes from select element options (no hardcoded list)
- `getDefaultTheme()` - Returns "AlienDark" if available, otherwise the first theme alphabetically
- `applyTheme(theme)` - Loads theme CSS and persists selection in localStorage
- Auto-applies saved theme on page load, or default theme if none saved
- Multiple selectors on the same page stay synchronized
- Automatically detects new themes when they're added to the select element

### Adding a New Theme

To create a new theme (e.g., `MyCustomTheme`):

1. **Create theme folder:**
   ```
   static/themes/MyCustomTheme/
   ```

2. **Create `theme.css` with CSS variables:**
   ```css
   :root {
     --bg-primary: #your-bg-color;
     --text-primary: #your-text-color;
     --accent: #your-accent-color;
     --accent-dark: #your-accent-dark-color;
     --bg-secondary: #your-secondary-bg;
     --border-color: #your-border-color;
   }
   
   /* Override styles using variables */
   body {
     background: var(--bg-primary);
     color: var(--text-primary);
   }
   /* ... more overrides ... */
   ```

3. **Add to theme selector in templates:**
   The theme selector options are now **dynamically generated** from available theme folders in the backend. When you create a new theme folder, it's automatically listed in the select dropdown on both `index.html` and dbadmin pages via Python template iteration.

### Best Practices for Theme Development

1. **Use CSS Variables:** Always reference theme colors via custom properties, never hardcode colors
2. **Minimal Overrides:** Only include CSS rules that differ from the base stylesheet
3. **Test Both Locations:** Verify theme works on main dashboard (`index.html`) and dbadmin pages (`layout.html`)
4. **Check Full Viewport:** Ensure backgrounds extend to full viewport height, no black/white strips at bottom
5. **Text Contrast:** Verify text colors have sufficient contrast with background colors for accessibility
6. **Form Elements:** Ensure all form inputs (text, select, button, checkbox) are styled consistently

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


