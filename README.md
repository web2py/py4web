# web3py

## Try me

```
pip3 install -r requirements.txt
start.py applications/
open http://localhost:8000/todo/index
```

## Tell me more

- this is a work in progress and not stable
- uses pyDAL (same DAL as web2py)
- uses yatl (same template language as web2py but defaults to [[...]] instead of {{...}} delimiters)
- uses the same validators as web2py (they are in pyDAL)
- uses the very similar helpers to web2py (A, DIV, SPAN, etc.)
- supports multiple apps under applications/ folder (same as web2py)
- request, response objects are from bottle (https://bottlepy.org/docs/dev/)
- sessions are encrypted jwt in cookies, and they must be small
- only supports cache.memoize (in Ram but O(1) access)
- unlike web2py, web3py is py3 only
- unlike web2py, web3py does not use custom import or eval
- dynamic module reloading is only partially supported
- there is no i18n yet (WIP)
- there is no admin yet (WIP)
- there is no appadmin yet (WIP)
- there is no Auth logic yet (WIP)
- there are no SQLFORM/grid/smartgrid (should there be? should they be in JS only?)
- there are not enough tests
- it is not as good as web2py yet, but it is 10-20x faster

## Warning
The code in site-packages is only there for development to make sure web3py uses the correct
development version of pydal sinc pydal on pypi is outdated and we have unable to update it.

## Integrations
- https://pypi.org/project/bottle-auth/
- https://github.com/jbardin/python-saml/blob/master/example_login.py
