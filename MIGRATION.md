# web2py → py4web Migration Rules (for Claude)

This is my working playbook for porting a web2py application to py4web. Read it
together with `CLAUDE.md` (py4web conventions) before touching code. When in
doubt, mirror `apps/_scaffold/` and the patterns documented in `docs/chapter-15.rst`.

## 0. Mental model: what actually changes

The two frameworks share **pyDAL** (identical table definitions and queries),
the **same validators**, **similar helpers** (`XML`, `URL`, `HTTP`, `T`), and a
**Form/Grid** pair analogous to `SQLFORM`/`SQLFORM.grid`. What changes is the
*execution model and wiring*, not the database layer.

The single biggest conceptual shift — **when code runs**:

- **web2py**: every file under `models/`, `controllers/`, `views/` is *executed
  in full on every single HTTP request*, in a fixed order, by a custom importer.
  Table definitions, `db = DAL(...)`, `auth.define_tables()`, menu construction —
  all of it re-runs per request. `request`, `response`, `session`, `db`, `auth`,
  `T`, `cache`, `URL`, `SQLFORM`, etc. are **injected globals** — they "just exist".
- **py4web**: an app is a normal Python package. **Module-level code runs only
  once, at import/startup** (the dev server *reloads and re-imports the module
  when a file changes*, but not per request). On each HTTP request **only the
  matched action function body executes.** A function is an action *only* if
  decorated with `@action(...)`. Nothing is global; everything is **explicitly
  imported** and every action **declares its dependencies** via
  `@action.uses(...)` (fixtures).

Two consequences I must internalize:

1. **There are no implicit globals.** Every
   `request`/`response`/`session`/`db`/`auth`/`T`/`URL`/`Form`/`Grid`/`flash`
   reference in web2py code must become an explicit import + a declared fixture.
2. **Because module code runs once, never put per-request logic at module
   level, and never mutate shared pyDAL state outside an action** (this is why
   table definitions are run-once and thread-unsafe to change — see §3). Things
   web2py rebuilt every request (the menu, dynamic `requires`, request-dependent
   defaults) must move *into* the action body.

## 1. Migration procedure (do this in order)

1. **Ensure the web2py app is Python 3.7+.** py4web is Py3.7+ only. Port any
   Python 2 idioms first (`print`, `dict.has_key`, `unicode`, integer division,
   relative imports).
2. **Scaffold the target.** Copy `apps/_scaffold/` to `apps/<appname>/`. This
   gives you `__init__.py`, `settings.py`, `common.py`, `models.py`,
   `controllers.py`, `tasks.py`, `templates/`, `static/`, `translations/`.
   Keep `common.py` largely untouched — it is the wiring file.
3. **Port the database layer** (`models/*.py` → `models.py`). See §3.
4. **Port controllers** (`controllers/*.py` → `controllers.py` or several
   modules imported by `__init__.py`). See §4.
5. **Port views** (`views/*.html` → `templates/*.html`), changing delimiters
   and inheritance. See §6.
6. **Port static assets** (`static/` → `static/`, mostly a copy).
7. **Move config** (hardcoded values + `appconfig.ini`) into `settings.py`. See §2.
8. **Wire auth/authorization** (`auth.requires_*` → fixtures + Tags). See §5.
9. **Port the menu / flash / response metadata** — these have no direct
   equivalent and must become template variables or layout logic. See §7.
10. **Run and fix.** `py4web setup apps` then `py4web run apps`; use the
    dashboard to locate actions and errors.

## 2. Configuration

| web2py | py4web |
|---|---|
| `private/appconfig.ini` + `AppConfig` | `settings.py` (plain Python module) |
| hardcoded DB uri in `models/db.py` | `settings.DB_URI` |
| `response.formstyle = ...` | pass `formstyle=` to `Form`/`Grid`, or set in `common.py` |

- Put **all** configuration in `settings.py`. Never hardcode config in
  controllers/models (CLAUDE.md rule 4).
- Per-environment/secret overrides go in `settings_private.py` (auto-imported by
  `settings.py` via `from .settings_private import *`, gitignored).
- The DB connection, session backend, auth, mailer, scheduler are all built in
  `common.py` from `settings.py`. Reuse the scaffold's `common.py` and only
  flip flags in `settings.py` (e.g. `SESSION_TYPE`, `SMTP_SERVER`,
  `USE_SCHEDULER`, OAuth keys).

## 3. Database / models

Tables and queries are **identical pyDAL** — copy them almost verbatim. The
wiring around them changes.

- web2py `models/db.py` builds `db = DAL(...)` and `auth = Auth(db)`. In py4web
  **that already happens in `common.py`.** Do not recreate `db`/`auth`; instead
  `from .common import db, Field, auth` in `models.py`.
- Define tables at **module level** in `models.py` (runs once at startup), then
  **call `db.commit()`** at the end (CLAUDE.md rule 6).
- Replace web2py auth field helpers: `auth.signature` works the same; use
  `auth.signature` on tables needing ownership/timestamps.
- web2py `DAL(..., migrate_enabled=..., check_reserved=[...])` → migration is
  controlled by `settings.DB_MIGRATE` / `DB_FAKE_MIGRATE` in the scaffold.
- **Thread-safety rule (critical):** code outside actions runs once. Never
  redefine tables or mutate table/field state per-request. Only these field
  attributes may be changed inside an action: `readable`, `writable`,
  `requires`, `update`, `default`. Everything else is effectively global.
- Do **not** use Lazy Tables in py4web — useless and dangerous given the
  run-once model.
- `db.define_table(..., migrate='...')` and conditional GAE branches in web2py
  scaffolds can be dropped; configure via `settings.py`.

## 4. Controllers / actions

Every web2py controller function becomes a decorated py4web action.

### Conversion checklist per function

1. Add `@action("<url-path>")`. The URL is `/<appname>/<path>`. web2py's
   automatic `controller/function` → URL mapping is **gone**; set the path
   explicitly. `index` may be omitted from the URL. Leading `/` = absolute path.
2. Add `@action.uses(...)` declaring **every** fixture the function touches:
   - uses `db`? add `db`. uses `session`? add `session`. uses `T`? add `T`.
   - renders a view? add the **template name first**: `@action.uses("x.html", db, auth)`.
   - needs login? add `auth.user`. login optional but needs auth? add `auth`.
   - uses `flash`? add `flash`.
3. Convert request args. web2py `request.args[i]` → declare typed URL params:
   `@action("f/<a>/<b:int>")` and add them as function parameters.
4. Convert the return value (see mapping below).
5. Replace injected globals with imports from `.common`.

### Request / response mapping

| web2py | py4web |
|---|---|
| `request.vars.x` / `request.get_vars.x` | `request.query.get("x")` |
| `request.post_vars.x` / `request.vars.x` (POST) | `request.forms.get("x")` or `request.json.get("x")` |
| `request.args[0]`, `request.args(0)` | URL param: `@action("f/<a>")` → arg `a` |
| `request.args` (list) | typed params `<a>/<b:int>/<c:int>` |
| `request.env.x` | `request.environ.get("x")` |
| `request.application` / `request.controller` / `request.function` | no equivalent; avoid relying on these |
| `request.folder` | `from .settings import APP_FOLDER` |
| `request.is_local` | check `request.environ` / use `settings.MODE` |
| `request.method` | `request.method`, or split into `@action(..., method="GET")` / `method="POST"` |
| `response.flash = "x"` | `flash.set("x", "green")` (fixture `flash`) |
| `response.render(...)` | just `return dict(...)` with a template fixture |
| `response.headers[...]` | `response.headers[...]` (ombott response) |
| `response.title/keywords/menu` | no equivalent — pass as template vars (see §7) |
| `redirect(URL(...))` | `redirect(URL(...))` (same) |
| `raise HTTP(404)` | `raise HTTP(404)` or `abort(404)` (same) |
| `URL('c','f',args=[1,2],vars={...})` | `URL('c','f',1,2,vars={...})` — **args are positional now** |
| `session.x = v` / `session.x` | `session["x"] = v` / `session.get("x")` — **dict-like, not attribute** |
| `session.forget()` | not needed; sessions are per-action via the fixture |

### Return-value semantics (no more extension routing)

- web2py routes by extension (`.html` → view, `.json` → JSON). **py4web does
  not.** Rule: if the action returns a `dict` **and** has a template fixture,
  the template renders it; otherwise a returned `dict`/`list` is serialized to
  **JSON**. Return a `str` for raw text.
- web2py `return locals()` works in py4web too, but prefer explicit
  `return dict(...)`.
- Multiple HTTP methods: instead of branching on `request.method`, stack
  decorators or use `@action(path, method=["GET","POST"])`.

### Things to delete

- `@cache.action(...)` web2py decorator → use py4web `cache` fixture / `Cache`
  object differently (cache results inside the action), not as routing decorator.
- `session.forget()`, `response.generic_patterns`, `response.optimize_*`,
  `response.form_label_separator` — drop them.

## 5. Auth & authorization (the trickiest part)

**The two frameworks use fundamentally different authorization models — this is
the part to get right.**

- **web2py** ships a full **Role-Based Access Control (RBAC)** system baked into
  `Auth`. It auto-creates the tables `auth_group`, `auth_membership`, and
  `auth_permission`, and exposes a rich **API**: `auth.add_group`,
  `auth.add_membership`, `auth.has_membership`, `auth.add_permission`,
  `auth.has_permission`, plus the decorator family
  `auth.requires_login()`, `auth.requires_membership(role)`,
  `auth.requires_permission(name, table)`, and `auth.requires(condition)`.
  Roles and per-record permissions are first-class.
- **py4web's `Auth` only establishes identity** (who the user is), **not
  permissions** (what they may do). There is **no** `auth.requires_*` /
  `has_membership` / `has_permission` API and **no** `auth_group` /
  `auth_membership` / `auth_permission` tables. Instead, group membership is
  modeled with **Tags**: the scaffold's `common.py` defines
  `groups = Tags(db.auth_user, "groups")`, and you *tag* a user with the groups
  (roles) they belong to, then check those tags yourself. `Tags` is a general
  mechanism that can label any record, not just users, so the same tool also
  replaces web2py permissions when you need them.

So the migration is: **web2py roles/memberships → py4web user tags via
`groups`**, and **web2py `requires_*` decorators → an explicit fixture
(`auth.user`) plus an in-action tag check**. Map them like this:

| web2py | py4web |
|---|---|
| `auth = Auth(db)` in model | already built in `common.py`; `from .common import auth` |
| `def user(): return dict(form=auth())` + `/user/login` | `auth.enable()` in common.py exposes `/<app>/auth/...` automatically; delete the `user()` action |
| `@auth.requires_login()` | `@action.uses(auth.user)` |
| `auth.user.id`, `auth.user.email` | `auth.user_id`; `auth.get_user().get("email")` (only `user_id` is in session) |
| `if auth.user:` | `if auth.user_id:` (with `@action.uses(auth)`) |
| `@auth.requires_membership("admin")` | `@action.uses(auth.user)` + in-action check (see below) |
| `auth.has_membership("admin")` | `"admin" in groups.get(user_id)` |
| `auth.add_group("admin")` / `auth.add_membership(gid, uid)` | `groups.add(user_id, "admin")` (no separate group table) |
| `auth.del_membership(...)` | `groups.remove(user_id, "admin")` |
| `auth.has_permission("read", "thing", rid)` | model as a tag/`Tags` check you write, or scope by query (e.g. `db.thing.owner == auth.user_id`) |
| `@auth.requires_permission(...)` | in-action check + `abort(403)` |
| `@auth.requires(condition)` | in-action `if not condition: abort(403)` |

Group membership via Tags (the scaffold's `common.py` already defines
`groups = Tags(db.auth_user, "groups")`):

```python
from .common import groups, auth

@action("admin")
@action.uses("admin.html", auth.user)
def admin():
    if "manager" not in groups.get(auth.user_id):
        abort(403)
    ...
```

For finer control or `auth.requires(condition)`, write the check at the top of
the action and `abort(403)` / `redirect(URL("auth/login"))`.

Other auth notes:
- `@action.uses(auth.user)` **requires** a logged-in user (≈ `requires_login`).
  `@action.uses(auth)` makes auth available but login optional.
- Using `auth` (or `auth.user`) automatically pulls in its `session` and
  `flash` — no need to also list them, but listing is harmless.
- Auth forms (register/login/reset/profile) are served by `auth.enable()`. Email
  verification, approval, password rules are all `settings.py` flags consumed in
  `common.py` (`VERIFY_EMAIL`, `REQUIRES_APPROVAL`, `PASSWORD_ENTROPY`, etc.).

## 6. Views / templates

| web2py | py4web (YATL) |
|---|---|
| `{{ ... }}` delimiters | `[[ ... ]]` delimiters |
| `{{= var }}` | `[[= var ]]` |
| `{{ extend 'layout.html' }}` | `[[ extend 'layout.html' ]]` |
| `{{ for x in xs: }} ... {{ pass }}` | `[[ for x in xs: ]] ... [[ pass ]]` |
| `{{ if c: }}...{{ pass }}` | `[[ if c: ]]...[[ pass ]]` (also `elif`/`else`/`pass`) |
| `{{ block name }}{{ end }}` | `[[ block name ]][[ end ]]` |
| `{{ include 'x.html' }}` | `[[ include 'x.html' ]]` |
| `{{=XML(s)}}` raw | `[[=XML(s)]]` raw (auto-escape otherwise) |
| `views/<controller>/<function>.html` auto-selected | no auto-selection; name the template in `@action.uses("name.html", ...)` |
| `{{=form}}` / `{{=grid}}` | `[[=form]]` / `[[=grid]]` |
| `response.flash` rendered in layout | pass `flash` and render `<flash-alerts data-alert="[[=globals().get('flash','')]]">` (needs `utils.js`) |

- Templates live in `templates/` (web2py used `views/`). Always
  `[[extend "layout.html"]]`.
- The mechanical bulk of view migration is **delimiter replacement**
  `{{` → `[[`, `}}` → `]]`. Do it carefully so Vue/Angular `{{ }}` in client code
  is **not** touched (py4web chose `[[ ]]` precisely to coexist with Vue).
- `web2py_ajax.html`, `generic.*` views: drop them. Use the scaffold's
  `generic.html` for debug rendering if wanted.
- Helpers (`DIV`, `A`, `INPUT`, `SPAN`, ...) exist in py4web's `yatl.helpers` but
  are a lighter reimplementation; verify signatures for non-trivial usage.

## 7. Things with no direct equivalent — convert deliberately

- **`response.menu`** (web2py global menu built in `models/menu.py`): py4web has
  no global menu. Build the menu list in `common.py` or a helper, pass it to
  templates as a variable, and render it in `layout.html`. Or hardcode the nav
  in `layout.html`.
- **`response.title` / `response.keywords` / `response.description`**: pass as
  dict values from the action and render in the layout's `<head>` block.
- **`response.flash`**: use the `flash` fixture + `flash.set(msg, "class")`; render
  via the `flash-alerts` custom tag (utils.js) or a plain div.
- **`crud`, `auth.requires`, `SQLFORM.factory` with `.process()`**: replace
  `SQLFORM(...).process()` with `Form(...)` (postback is automatic; check
  `form.accepted` / `form.errors` / `form.deleted`). Replace `SQLFORM.grid(...)`
  with `Grid(...)` — see §9.
- **Scheduler**: web2py `Scheduler(db)` in a model → py4web enables the pyDAL
  scheduler via `settings.USE_SCHEDULER` (built in `common.py`); define tasks in
  `tasks.py`.
- **Modules in `modules/`**: become normal package imports inside the app
  package or installed packages.
- **`appadmin`**: replaced by the py4web `_dashboard` (dbadmin). Expose `db` by
  importing it in `__init__.py` (the scaffold already does
  `from .models import db`).

## 8. Forms quick map (SQLFORM → Form)

```python
# web2py
form = SQLFORM(db.thing)
if form.process().accepted:
    response.flash = "Done"

# py4web
@action("create")
@action.uses("create.html", db, flash)
def create():
    form = Form(db.thing)            # postback automatic
    if form.accepted:
        flash.set("Done", "green")
        redirect(URL("index"))
    return dict(form=form)
```

- `Form(db.table)` = create; `Form(db.table, record_id)` = edit.
- No `.process()` call — instantiating the Form processes the postback.
- Import `Form` from `py4web.utils.form` (not `SQLFORM`); `Grid` from
  `py4web.utils.grid`.
- For upload fields, set `field.upload_path` and `field.download_url` (see the
  commented download action in `common.py`).

## 9. Grid (SQLFORM.grid → Grid)

`Grid` is the py4web counterpart of web2py's `SQLFORM.grid` and is the
cornerstone of most data-driven py4web apps: full CRUD, sorting, pagination,
search, and custom row buttons. Migration is mostly a change of constructor
signature plus correct fixtures.

```python
# web2py
def manage():
    grid = SQLFORM.grid(db.thing, editable=True, deletable=True, searchable=True)
    return dict(grid=grid)

# py4web
from py4web.utils.grid import Grid, Column
from py4web.utils.form import FormStyleDefault
from py4web.utils.grid import GridClassStyle

@action("manage", method=["GET", "POST"])          # MUST allow POST
@action.uses("manage.html", session, db)           # MUST include session
def manage():
    grid = Grid(
        db.thing.id > 0,                            # a QUERY, not just the table
        editable=True,
        deletable=True,
        create=True,
        details=True,
        orderby=[db.thing.name],
        search_queries=[["Search by name", lambda v: db.thing.name.contains(v)]],
        formstyle=FormStyleDefault,
        grid_class_style=GridClassStyle,
    )
    return dict(grid=grid)
```

Template: render with **`[[=grid.render()]]`** (not `[[=grid]]`).

Migration rules — these are the gotchas, not the obvious parts:

- **Fixtures:** the action **must** declare `session` (the grid signs its
  action URLs against the session) and `db`. Add `auth.user` if access should be
  restricted. Pass the translator with `Grid(..., T=T)` and add `T` as a fixture
  for i18n.
- **Method:** the grid posts back (search, delete confirmation), so the action
  **must** accept POST: `@action(..., method=["GET", "POST"])`.
- **First argument is a query, not a table.** web2py accepted `SQLFORM.grid(db.t)`;
  in py4web pass a pyDAL query such as `db.thing.id > 0` (or
  `(db.thing.owner == auth.user_id)` to scope by owner). A bare table also works
  but a query is the idiom.
- **CRUD flags are constructor keyword args**, not `.grid(...)` kwargs with the
  same names everywhere and **not** `grid.param.*`: `create`, `details`,
  `editable`, `deletable` (each accepts `True`/`False`, a URL string to redirect
  to your own page, or a **callable receiving the row** — e.g.
  `deletable=lambda row: row.job != "CEO"`).
- **Search:** web2py's `searchable=True`/`searchfields` becomes either
  `search_queries=[[label, lambda v: <query>], ...]` (auto-built search box; a
  dropdown appears if more than one entry) or a custom `search_form=` Form whose
  values you apply to the query yourself.
- **Styling:** choose `formstyle` + `grid_class_style` + `icon_style`
  (`FormStyleDefault`/`Bulma`/`Bootstrap4`/`Bootstrap5`/`Tailwind`, matching
  `GridClassStyle*`, `IconStyleFontawesome`/`IconStyleBootstrapIcons`). With the
  default `no.css` you can omit these. Load the matching CSS in `layout.html`.
- **Custom columns:** `columns=[db.thing.name, Column("Link", lambda row: A(...))]`.
  **Define the `columns` list INSIDE the action**, never at module level — the
  grid mutates it (appends the action-buttons column) on each render, so a
  module-level list would accumulate duplicate columns. This is a direct
  consequence of the run-once execution model (§0).
- **Joins:** use `left=` for the join and `field_id=` to tell the grid which
  table backs edit/details/delete.
- `auto_process=True` (default) processes the request at construction; set
  `False` and call `grid.process()` if you need to do work in between.

## 10. URL signing / callbacks (replacing web2py inline LOAD/ajax)

web2py often used `LOAD()` components and `ajax()` with implicit URLs. In py4web:
- Generate URLs server-side with `URL(...)` and pass them to JS via template
  variables — **never hardcode paths in JS** (CLAUDE.md rule 3).
- For state-changing callbacks, sign them: `URLSigner(session)` and
  `@action.uses(..., url_signer.verify())`.
- Client AJAX uses the bundled `utils.js` `Q` helpers or Vue + axios.

## 11. Final sanity checklist before declaring done

- [ ] Every controller function that should be a URL has `@action(...)`.
- [ ] Every action lists all fixtures in `@action.uses(...)`, template first.
- [ ] No references to undeclared globals (`request`/`response`/`session`/`db`/
      `auth`/`T`/`URL`/`cache` all imported from `.common` or `py4web`).
- [ ] No per-request logic at module level (menu/dynamic defaults moved into
      actions); module code is safe to run exactly once.
- [ ] `db.commit()` after table definitions in `models.py`.
- [ ] No per-request mutation of table/field state (except readable/writable/
      requires/update/default).
- [ ] Template delimiters converted `{{ }}` → `[[ ]]`, Vue `{{ }}` left intact.
- [ ] `auth.requires_*` decorators replaced by `auth.user` fixture / Tags checks.
- [ ] `SQLFORM.grid` → `Grid`: action allows POST, declares `session`, gets a
      query, columns defined inside the action, rendered with `grid.render()`.
- [ ] `session` accessed dict-style; `URL` args positional.
- [ ] Config in `settings.py`, secrets in `settings_private.py`.
- [ ] `__init__.py` imports controllers and `db`; app runs under `py4web run apps`.
```
