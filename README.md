# web3py

## Try me

```
pip3 install -r requirements.txt
./web3py-start apps
open http://localhost:8000/todo/index
```

## Tell me more

- this is a work in progress and not stable yet but close to be stable
- python3 only
- uses https://github.com/web2py/pydal (same DAL as web2py)
- uses https://github.com/web2py/yatl (same as web2py but defaults to [[...]] instead of {{...}} delimiters)
- uses the same validators as web2py (they are in pyDAL)
- uses the very similar helpers to web2py (A, DIV, SPAN, etc.)
- uses https://github.com/web2py/pluralize for i18n and pluralization
- request, response, abort, redirect are from https://bottlepy.org
- implements sessions in cookies (jwt encrypted), db, memcache, redis and custom
- implements a cache.memoize (Ram cache with O(1) access)
- supports multiple apps under apps folder (same as web2py)
- does not use a custom importer or eval
- admin has been replaced by a _daskboard (90% done)
- appadmin has been replaced by dbadmin (within dashboard) (90% done)
- auth logic is implemented via a "auth" vue.js custom component (90% done)
- SQLFORM has been replaced by web3py/utils/form.py
- SQLFORM.grid was been replaced by a "mtable" vue.js custom component (90% done)
- there are not enough tests
- it is not as stable as web2py yet
- it is 10-20x faster than web2py

## Warning
The code in site-packages is only there for development to make sure web3py uses the correct
development version of pydal sinc pydal on pypi is outdated and we have unable to update it.

## Planned Integrations
- https://pypi.org/project/bottle-auth/
- https://github.com/jbardin/python-saml/blob/master/example_login.py

## Componts

- pydal + dbapi (done)
- yatl (done)
- pluralize (done)
- auth (90%)
- mailer (done)
- session (cookes, db, redis, memcache)
- form (done up to downloads)
- mtable (75%)
- dashboard (90% done)
- scaffold (done)
- bus (0%)
- tornado (done)
- gevent (done)
- gunicorn (done)
- bottle (done)
