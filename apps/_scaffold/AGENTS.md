# py4web — Notes for AI Agents and New Contributors

This file lists the framework gotchas that bite people (and AI assistants) most
often. If you're an AI agent working in a py4web app, load this file into your
context before you start editing. If you're a human, skim it once — every line
here represents at least one wasted afternoon.

See also: `CLAUDE.md` in the repo root (if present) for higher-level conventions.

---

## Quick rules

1. Templates use `[[ ... ]]`, **not** `{{ ... }}`. (Avoids Vue/Angular conflict.)
2. Every action declares its fixtures: `@action.uses(template_first, db, session, auth.user, ...)`.
   The template fixture (a string) must be the **first** argument when present.
3. Never hardcode URLs. Use `URL("action", arg, vars=dict(x=1))`.
4. After defining tables in `models.py`, call `db.commit()`.
5. Field attributes that are thread-safe to mutate per-request: `readable`, `writable`,
   `requires`, `default`, `label`, `widget`, `represent`, `filter_in`, `filter_out`,
   `update`. **Nothing else.** Never `db.define_table()` inside an action.

---

## Gotchas (silent or surprising)

### 1. `Field("blob", "json", default=dict)` can leak the `dict` *class*

Symptom: `TypeError: <class 'dict'> is not JSON serializable` on insert.

Fix: use a lambda.

```python
Field("payload", "json", default=lambda: {})
Field("tags",    "json", default=lambda: [])
```

(py4web ≥ 1.20260520 warns and auto-rewrites `default=dict` / `default=list` /
`default=set` at table-definition time, but the lambda form is still the
documented best practice.)

### 2. Pluralize translation values must be dicts, not strings

In `translations/it.json`, this is silently ignored:

```json
{ "Hello": "Ciao" }
```

You'll see "Hello" in the browser and waste an hour. The correct shape is:

```json
{ "Hello": {"0": "Ciao"} }
{ "thing": {"0": "cosa", "1": "cose"} }
```

(py4web ≥ 1.20260520 auto-normalizes string values to `{"0": value}` and logs a
warning at load time, so plain-string entries now work. Prefer the dict form
when writing new files.)

### 3. `request.query` is **single-value** in ombott

For a URL like `?tag=a&tag=b`, `request.query.get("tag")` returns only `"b"`.
To get repeated params:

```python
from urllib.parse import parse_qs
parse_qs(request.query_string)["tag"]   # ["a", "b"]
```

### 4. Built-in `/auth/*` routes do **not** go through your `@action.uses` chain

The auth fixtures register their own routes. If you want i18n on the auth pages
(register, login, etc.), import `T` at the top of `layout.html`:

```html
[[from py4web import URL]]
[[from .common import T]]
```

…and use `[[=T('Register')]]` in the auth templates.

### 5. `validate_and_insert` / `validate_and_update` **return** errors, they don't raise

```python
res = db.thing.validate_and_insert(**request.json)
if res.get("errors"):
    abort(400)
record_id = res["id"]
```

Same for update: check `res.get("errors")` before continuing.

### 6. `auth.sender` is a `Mailer` — call it with keyword args

The `Mailer.send` signature is `send(to, subject=..., body=..., html=...)`,
**not** `send(name, user, **kwargs)`. If you write a custom dev sender to dump
mail to stdout, mirror that signature:

```python
class StdoutMailer:
    def send(self, to, subject="", body="", html=None, **_):
        print(f"--- mail to {to}: {subject} ---\n{body}\n---")

if MODE == "development":
    auth.sender = StdoutMailer()
```

### 7. Stale `.table` files vs. missing `storage.db` → "no such table"

If you delete `databases/storage.db` but leave the `*.table` migration markers
behind, pydal thinks the schema is already applied and refuses to recreate it.

Fix: `rm databases/*.table` and let py4web re-migrate, **or** start once with
`DAL(..., fake_migrate_all=True)` then revert.

(py4web ≥ 1.20260520 raises a clearer error at startup when this state is
detected for SQLite.)

### 8. Duplicate `@action` paths silently win-last

```python
@action("/")
@action.uses(...)
def home(): ...

@action("index")        # also resolves to "/"
@action.uses(...)
def home2(): ...
```

The framework auto-aliases `/index` → `/`, so the second decorator overwrites
the first and you get whichever loaded last. (py4web ≥ 1.20260520 logs a
warning naming both registrations.)

### 9. Action return types

Return value handling:

- `dict` → rendered by the template fixture if one is declared; otherwise JSON.
- `str` → returned as-is.
- `None` → empty body.
- A `yatl` tag (e.g. `DIV(...)`) → coerced to string.
- A `redirect()` or `abort()` is raised, not returned.

Anything else raises `RuntimeError: Cannot return type <name>`.

### 10. Settings come from `settings.py`, fixtures from `common.py`

Don't hardcode config in controllers. Don't initialize fixtures (db, auth,
session) anywhere except `common.py`. Other modules import them.

### 11. `--dev` flag flips a bunch of knobs for you

`py4web run apps --dev` is equivalent to `--mode development` and additionally
sets verbose logging. The scaffold's `settings.py` reads `PY4WEB_MODE`, so
`--dev` also relaxes `PASSWORD_ENTROPY` and `VERIFY_EMAIL`. Use it in dev,
don't use it in prod.

---

## When in doubt

- Read `apps/showcase/` for end-to-end examples (auth, forms, grids, uploads,
  scheduler, i18n, OAuth, HTMX).
- Read `apps/_dashboard/` for an example of a complex multi-controller app
  with restricted access.
- `py4web shell apps` gives you an interactive REPL with `db`, `auth`, etc.
  pre-loaded for the app you select.
- Tickets (server errors) are at `/_dashboard/tickets`.

---

## File you're reading

This file is part of the `_scaffold` app. When you create a new app with
`py4web new_app apps myapp`, this file is copied along. Keep it — every AI
assistant that touches the new app will start from these notes.
