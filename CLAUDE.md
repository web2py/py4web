# py4web Development Guide for Claude

## Project Overview

py4web is a Python web framework for rapid development of database-driven web applications. It is the modern successor to web2py, built on ombott (optimized Bottle fork) and PyDAL.

## App Structure

Every py4web app is a Python package (folder with `__init__.py`) inside the `apps/` directory. Standard layout:

```
apps/myapp/
  __init__.py        # App init: version check, import controllers and db
  settings.py        # All configuration (DB_URI, session type, auth, etc.)
  common.py          # Initialize fixtures: db, session, auth, T, cache, flash, logger
  models.py          # Database table definitions using PyDAL
  controllers.py     # Action handlers (routes)
  tasks.py           # Scheduler/Celery tasks (optional)
  templates/
    layout.html      # Base template (extend this)
    index.html       # Page templates
    auth.html        # Auth forms
  static/
    js/utils.js      # Standard JS utility library (Q selector, AJAX, etc.)
    css/no.css       # Default minimal CSS framework
  databases/         # SQLite files and migration metadata
  translations/      # i18n JSON files
  uploads/           # User-uploaded files
```

## Python Conventions

### Actions (Controllers)

```python
from py4web import action, URL, redirect, request, abort
from .common import db, session, auth, T, flash, cache

# Basic action
@action("index")
@action.uses("index.html", auth, T)
def index():
    user = auth.get_user()
    return dict(message="Hello")

# With URL parameters
@action("item/<id:int>")
@action.uses(db, auth.user)
def item(id):
    record = db.thing[id] or abort(404)
    return dict(record=record)

# API endpoint returning JSON (no template)
@action("api/data", method="GET")
@action.uses(db, auth.user)
def api_data():
    rows = db(db.thing).select()
    return dict(data=rows.as_list())

# POST action
@action("api/create", method="POST")
@action.uses(db, auth.user)
def api_create():
    db.thing.insert(**request.json)
    return dict(ok=True)
```

**Rules:**
- `@action("path")` defines the route. The URL is `/{app_name}/{path}`.
- `@action.uses(...)` declares fixtures. Template must be **first** if present.
- `@action.uses(auth.user)` requires login; `@action.uses(auth)` makes login optional.
- Actions return `dict` (rendered by template or as JSON), `str`, or raise `redirect()`/`abort()`.
- Use `auth.get_user()` to get current user dict, `auth.user_id` for just the ID.
- Use `request.query.get("param")` for query params, `request.json` for JSON body, `request.forms` for form data.
- Multiple routes: stack `@action` decorators on the same function.
- HTTP methods: `@action("path", method=["GET", "POST"])`.

### Convenience Decorators

`common.py` defines `authenticated` and `unauthenticated` ActionFactory decorators:

```python
# Instead of @action.uses(db, session, T, auth.user)
@authenticated()
def protected():
    return dict()

# Instead of @action.uses(db, session, T, auth)
@unauthenticated()
def public():
    return dict()
```

### Database Models

```python
from pydal.validators import *
from .common import db, Field, auth

db.define_table("thing",
    Field("name", requires=IS_NOT_EMPTY()),
    Field("description", "text"),
    Field("quantity", "integer", default=0),
    Field("owner", "reference auth_user"),
    auth.signature,  # Adds created_by, created_on, modified_by, modified_on
)
db.commit()
```

**Rules:**
- Define tables in `models.py` at module level (executed once at startup).
- Always call `db.commit()` after table definitions.
- `auth.signature` adds ownership/timestamp fields automatically.
- Use PyDAL field types: `string`, `text`, `integer`, `float`, `boolean`, `date`, `datetime`, `reference tablename`, `upload`, `json`, `list:string`, `list:integer`.
- Validators: `IS_NOT_EMPTY()`, `IS_IN_SET(["a","b"])`, `IS_INT_IN_RANGE(0, 100)`, `IS_EMAIL()`, `IS_MATCH(regex)`, etc.
- Only field attributes (readable, writable, requires, default) are thread-safe to modify in actions.

### Database Queries

```python
# Select
rows = db(db.thing.owner == auth.user_id).select(orderby=~db.thing.created_on, limitby=(0, 100))

# Insert
id = db.thing.insert(name="foo", description="bar")

# Update
db(db.thing.id == id).update(name="new name")

# Delete
db(db.thing.id == id).delete()

# Joins
rows = db(db.thing.owner == db.auth_user.id).select(db.thing.ALL, db.auth_user.email)

# Count
n = db(db.thing.owner == auth.user_id).count()

# Complex queries with & (AND) and | (OR)
query = (db.thing.name.contains("foo")) & (db.thing.quantity > 0)
rows = db(query).select()
```

### Forms

```python
form = Form(db.thing, csrf_session=session)
if form.accepted:
    redirect(URL("index"))
return dict(form=form)
```

- `Form(db.table)` for create, `Form(db.table, record_id)` for edit.
- Check `form.accepted`, `form.deleted`, `form.errors`.

### Grid

```python
grid = Grid(db.thing, formstyle=FormStyleDefault)
return dict(grid=grid)
```

### Authorization with Tags

```python
from pydal.tools.tags import Tags
groups = Tags(db.auth_user, "groups")
groups.add(user_id, "manager")
if "manager" in groups.get(user_id):
    ...
```

### URL Generation

```python
URL("action_name")                    # /{app}/action_name
URL("action", 1, 2)                   # /{app}/action/1/2
URL("action", vars=dict(x=1))         # /{app}/action?x=1
URL("static", "js/index.js")          # /{app}/static/js/index.js
URL("action", scheme=True)            # https://host/{app}/action
```

### Custom Fixtures

```python
from py4web.core import Fixture

class MyFixture(Fixture):
    def on_request(self, context):
        # Called before action
        pass
    def on_success(self, context):
        # Called after successful action
        pass
    def on_error(self, context):
        # Called on error
        pass
```

### URL Signing (CSRF/tamper protection for callbacks)

```python
from py4web.utils.url_signer import URLSigner
url_signer = URLSigner(session)

@action("callback", method="POST")
@action.uses(db, session, url_signer.verify())
def callback():
    ...

# In controller, pass signed URL:
return dict(callback_url=URL("callback", signer=url_signer))
```

## Template Conventions (YATL)

py4web uses `[[...]]` delimiters (NOT `{{...}}` or `{%...%}`) to avoid conflicts with Vue.js/Angular.

```html
[[extend "layout.html"]]

<!-- Output (auto-escaped) -->
[[=variable]]

<!-- Raw output (no escaping) -->
[[=XML(html_string)]]

<!-- Conditionals -->
[[if condition:]]
  <p>yes</p>
[[elif other:]]
  <p>other</p>
[[else:]]
  <p>no</p>
[[pass]]

<!-- Loops -->
[[for item in items:]]
  <p>[[=item.name]]</p>
[[pass]]

<!-- Blocks (for template inheritance) -->
[[block page_head]]
  <link rel="stylesheet" href="[[=URL('static','css/custom.css')]]">
[[end]]

<!-- Include -->
[[include "component.html"]]
```

**Rules:**
- Always `[[extend "layout.html"]]` at top for consistent look.
- Use `[[block name]]...[[end]]` to override sections from layout.
- Actions return `dict(...)` and template variables are accessed directly by name.
- `[[=form]]` renders a Form object. `[[=grid]]` renders a Grid.
- `BEAUTIFY(__vars__)` in `generic.html` for debugging.

## JavaScript Conventions

### Q Utility Library (utils.js)

All apps include `utils.js` which provides a lightweight jQuery alternative:

```javascript
// DOM selection
Q("selector")                        // querySelectorAll wrapper
Q(".myclass")[0].style.display = "none"

// AJAX
Q.get(url)                           // GET, returns Promise
Q.post(url, data)                    // POST with JSON body
Q.put(url, data)                     // PUT
Q.delete(url)                        // DELETE
Q.ajax("GET", url, data, headers)    // Full control

// Cookies
Q.get_cookie("name")

// Forms
Q.trap_form(action, elem_id)         // AJAX form submission

// Components
Q.handle_components()                // Process <ajax-component> tags
Q.flash({message, class})            // Show flash alert

// Translation
T("string")                          // Client-side i18n
```

### Vue.js Pattern (for reactive UIs)

```javascript
// static/js/index.js
var app = {
    data() {
        return { items: [], content: "" };
    },
    methods: {
        submit() {
            axios.post(create_url, { content: this.content })
                .then(() => { this.content = ""; this.reload(); });
        },
        reload() {
            axios.get(data_url).then(r => { this.items = r.data.items; });
        },
    },
    mounted() {
        this.reload();
    },
};

Vue.createApp(app).mount("#app");
```

- Use Vue 3 with `createApp()`.
- Use Axios for HTTP requests.
- Pass URLs from controller via template variables (do NOT hardcode paths in JS).
- Template uses `v-model`, `v-for`, `@click`, `v-if` etc.

### Inline JS in Templates

For simple interactivity without Vue:

```html
<script>
function callback(elem) {
    Q.post(elem.getAttribute("data-url"), {})
     .then(() => location.reload());
}
</script>
<button data-url="[[=URL('my_action')]]" onclick="callback(this)">Click</button>
```

## CSS Conventions

- Default framework: `no.css` (classless, styles semantic HTML automatically).
- Alternative: Bulma (used in birdwatching app).
- Grid classes: `.columns`, `.c25`, `.c33`, `.c50`, `.c66`, `.c75`.
- Color classes: `.success`, `.warning`, `.error`, `.info`, `.black`, `.white`.
- Use `class="padded"` for spacing.

## Important Rules

1. **Fixtures declare dependencies.** Every action must list what it needs via `@action.uses()`. No global middleware.
2. **Template first.** When using a template fixture, it must be the first argument in `@action.uses("template.html", ...)`.
3. **No hardcoded URLs.** Always use `URL()` to generate paths. Pass URLs to JavaScript via template variables.
4. **Settings in settings.py.** Never hardcode configuration values in controllers or models.
5. **Shared state in common.py.** All fixtures (`db`, `session`, `auth`, `T`, `cache`, `flash`) are initialized in `common.py` and imported elsewhere.
6. **`db.commit()` after table definitions.** Required in `models.py` after `db.define_table()` calls.
7. **Thread safety.** Table definitions are NOT thread-safe. Only field attributes (readable, writable, requires, default) can be modified per-request.
8. **DAL transactions are automatic.** Commit on success, rollback on error. No manual commit needed in actions.
9. **YATL delimiters are `[[...]]`**, not `{{...}}`. This avoids conflicts with Vue.js.
10. **Use `auth.signature`** on tables that need ownership tracking.
11. **Static files** go in `static/` and are served at `/{app}/static/...`.
12. **Translations** go in `translations/` as JSON files keyed by language code.

## Testing

Run tests with:
```bash
python -m pytest tests/
```

## Building & Running

```bash
# Install
pip install py4web

# Setup (first time)
py4web setup apps

# Run development server
py4web run apps

# Run on specific port
py4web run --port 8000 apps
```
