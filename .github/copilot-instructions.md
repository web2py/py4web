# PY4WEB Codebase Guide for AI Coding Agents

## Project Overview
PY4WEB is a web framework for rapid development of database-driven web applications, evolved from web2py but faster and more modern. Built on PyDAL (database abstraction layer), Ombott (WSGI framework), YATL (templating), and Renoir (template engine).

## Architecture

### Core Components
- **py4web/core.py** (2200+ lines): Central framework logic including Fixtures, action decorator, session/cache/flash, DAL integration, and CLI commands
- **py4web/__init__.py**: Exports main API (`action`, `DAL`, `Field`, `Session`, `Cache`, etc.)
- **py4web/utils/**: Modular utilities (auth, forms, grids, mailer, security, URL signing, etc.)
- **apps/**: Individual web applications following the app-per-folder convention

### Application Structure (see `apps/_scaffold/`)
Each app is a Python package with standard files:
- **__init__.py**: Imports controllers, models, settings; exposes `db` and `scheduler`; must call `py4web.check_compatible()`
- **controllers.py**: Define actions using `@action` decorator with `.uses()` for fixtures
- **models.py**: Database table definitions via PyDAL
- **common.py**: Shared fixtures (db, auth, session, cache, T, flash) instantiated here - import these, don't recreate
- **settings.py**: App configuration (DB_URI, SESSION_TYPE, VERIFY_EMAIL, etc.)
- **tasks.py**: Background scheduler tasks (PyDAL Scheduler or Celery)
- **templates/**: YATL/HTML templates
- **static/**: CSS/JS/images
- **databases/**: SQLite files and migration metadata

### Dashboard App (`apps/_dashboard/`)
Special administrative app with elevated privileges for managing py4web itself. Uses custom authentication (password file, not Auth framework) and can access/modify all app files.

**Key differences from regular apps**:
- Uses `Logged` fixture instead of `Auth` for authentication
- Can access files and databases across all applications
- Password-based login via `password.txt` file

For detailed Dashboard documentation, see `apps/_dashboard/DASHBOARD_GUIDE.md`.

## Critical Patterns

### The Fixture System
**Fixtures are the backbone** - they manage request lifecycle (db connections, sessions, templates, auth).

```python
# Correct: Declare ALL fixtures with @action.uses()
@action("index")
@action.uses(db, session, auth, T, "index.html")
def index():
    return dict(message="Hello")
```

**WARNING**: Fixtures MUST be declared with `@action.uses()` or app behavior is undefined. Never mix `@action.uses()` with ActionFactory decorators (`authenticated`, `unauthenticated`).

**Fixture Lifecycle**:
1. `on_request()` - Initialize (get DB connection, load session)
2. `on_success()` or `on_error()` - Cleanup (commit/rollback DB, save session)
3. Fixtures use thread-local storage via `Fixture.local`

### Action Decorator Pattern
```python
from py4web import action, request, redirect, URL
from .common import db, session, auth, T

@action("path/to/endpoint")  # Routes to /{app_name}/path/to/endpoint
@action.uses(db, session, auth.user, T, "template.html")
def my_action():
    # auth.user requires logged-in user (raises HTTP 401 if not)
    user = auth.get_user()
    # Return dict for templates, or direct response
    return dict(data=db(db.table).select())
```

### Database (PyDAL) Integration
```python
# In models.py - define tables
from .common import db, Field
from pydal.validators import IS_NOT_EMPTY, IS_EMAIL

db.define_table('person',
    Field('name', requires=IS_NOT_EMPTY()),
    Field('email', requires=IS_EMAIL()))
db.commit()  # Always commit models

# In controllers.py - query data
@action("list")
@action.uses(db, "list.html")
def list_people():
    rows = db(db.person).select()
    return dict(rows=rows)
```

**Thread-Safety**: PyDAL Field attributes (`readable`, `writable`, `default`, `requires`, etc.) are ThreadSafeVariable - safe to modify per-request.

### Authentication Flow
Auth is configured in `common.py`. Standard pattern:
```python
from py4web.utils.auth import Auth

auth = Auth(session, db, define_tables=False)
auth.use_username = True
auth.param.registration_requires_confirmation = settings.VERIFY_EMAIL
# Auth defines tables on first use
auth.enable()  # Call in common.py to create auth_user, auth_group tables
```

Use fixtures: `auth` (any user), `auth.user` (logged-in only).

## Developer Workflows

### Setup & Run
```bash
# Standard installation
pip install --upgrade py4web
py4web setup apps        # Creates app scaffolds, sets dashboard password
py4web run apps          # Runs on localhost:8000

# With uv (recommended)
uv run --with py4web python 3.12 py4web setup apps
uv run --with py4web python 3.12 py4web run apps

# Development with auto-reload
py4web run -p password.txt apps --watch=lazy -L20  # -L20 = INFO logging
```

### Testing
```bash
uv run --python 3.13 --extra test pytest --cov=py4web --cov-report html:cov.html -v tests/
```

Tests are in `tests/` using pytest. See `tests/test_action.py` for action/fixture testing patterns.

### Creating New Apps
```bash
py4web new_app -s apps/myapp  # -s uses _scaffold template
```

Or copy `apps/_scaffold/` manually. Must import controllers in `__init__.py` to expose actions.

### CLI Commands
```bash
py4web setup apps              # Interactive app creation wizard
py4web set_password            # Set dashboard password
py4web run apps                # Start server
py4web shell apps              # Python shell with apps loaded
py4web routes apps             # Show all registered routes
py4web version                 # Show version
```

See `py4web/core.py` lines 1941-2241 for CLI implementation.

## Project Conventions

### Import Patterns
```python
# In controllers.py
from py4web import action, request, response, redirect, abort, URL
from .common import db, session, auth, T, cache, flash  # Shared fixtures
from yatl.helpers import A, DIV, SPAN  # HTML helpers
```

Never instantiate fixtures in controllers - import from `common.py`.

### URL Generation
```python
# In controllers
URL('other_action', vars=dict(id=123))
# In templates
[[=URL('action', vars=dict(x=1))]]  # [[ ]] delimiters for YATL
```

### Template Syntax (YATL)
- Delimiters: `[[ python code ]]`
- Helpers auto-imported: `A`, `DIV`, `TABLE`, etc.
- Context: `request`, `URL`, `__vars__` (returned dict) available

### Session Types
Configured via `settings.SESSION_TYPE`:
- `"cookies"` - Client-side (default, good for most)
- `"database"` - Server-side in DB (requires `DBStore`)
- `"redis"` - Server-side in Redis
- `"memcache"` - Server-side in Memcache

### Background Tasks
PyDAL Scheduler (default) or Celery. In `tasks.py`:
```python
from .common import scheduler

def my_task(inputs):
    # Task logic
    pass

scheduler.register_task("my_task", my_task)
scheduler.enqueue_run("my_task", inputs={}, period=60)
```

## Key Files Reference
- **py4web.py**: Entry point, calls `py4web.core.cli()`
- **pyproject.toml**: Dependencies (pydal, ombott, renoir, yatl, etc.), version in `py4web.__init__.__version__`
- **Makefile**: Build/test commands (`make test`, `make assets`, `make docs`)
- **apps/_scaffold/**: Template for new apps - study this for patterns
- **apps/_dashboard/**: Web-based admin interface (edit code, manage DB)

## Common Pitfalls
1. **Forgetting `@action.uses()`** - Always declare fixtures or db connections won't work
2. **Creating fixtures in controllers** - Import from `common.py`, don't instantiate
3. **Not committing models** - Always `db.commit()` at end of `models.py`
4. **Mixing action styles** - Don't mix `@action`/`@action.uses()` with ActionFactory decorators
5. **Wrong app loading** - Apps must import controllers in `__init__.py` to register actions

## External Resources
- Main website: https://py4web.com
- Documentation: https://py4web.com/_documentation
- GitHub: https://github.com/web2py/py4web
- Mailing List: https://groups.google.com/g/py4web
- Discord: https://discord.gg/xCzQ9KTk3W
- PyDAL docs: https://py4web.com/_documentation/static/en/chapter-07.html
