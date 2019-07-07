# web3py

## Try me (from pip)

```
python3 -m pip install web3py
web3py-start apps
open http://localhost:8000/todo/index
```

(The apps folder will be created with some apps inside)

## Try me (from source)

```
git clone https://github.com/web2py/web3py.git
cd web2py 
python3 -m pip install -r requirements.txt
./web3py-start apps
open http://localhost:8000/todo/index
```

Notice "web3py-start" uses the pip insalled web3py, "./web3py-start" uses the local one. Do not get confused.

## Tell me more

- this is a work in progress and not stable yet but close to be stable
- python3 only
- uses https://github.com/web2py/pydal (same DAL as web2py)
- uses https://github.com/web2py/yatl (same as web2py but defaults to [[...]] instead of {{...}} delimiters)
- uses the same validators as web2py (they are in pyDAL)
- uses the very similar helpers to web2py (A, DIV, SPAN, etc.)
- uses https://github.com/web2py/pluralize for i18n and pluralization
- request, response, abort are from https://bottlepy.org
- HTTP and redirect are our own objects
- like web2py it supports static asset management /{appname}/static/_0.0.0/{path}
- implements sessions in cookies (jwt encrypted), db, memcache, redis and custom
- implements a cache.memoize (Ram cache with O(1) access)
- supports multiple apps under apps folder (same as web2py)
- unlike web2py does not use a custom importer or eval
- admin has been replaced by a _daskboard (90% done)
- appadmin has been replaced by dbadmin (within dashboard) (90% done)
- auth logic is implemented via a "auth" vue.js custom component (90% done)
- SQLFORM has been replaced by web3py/utils/form.py
- SQLFORM.grid was been replaced by a "mtable" vue.js custom component (90% done)
- there are not enough tests
- it is not as stable as web2py yet
- it is 10-20x faster than web2py

## Components

- pydal + dbapi (done)
- yatl (done)
- pluralize (done)
- auth (WIP, 90%)
- mailer (done)
- session (cookes, db, redis, memcache)
- form (done up to downloads)
- mtable (WIP, 75%)
- dashboard (90% done)
- scaffold (done)
- bus (0%)
- tornado (done)
- gevent (done)
- gunicorn (done)
- bottle (done)

## Storing _dashboard password 

If you do not want to be prompted for a dashboard passwod every time:

1) create the password:

```
$ python3 -c "from pydal.validators import CRYPT; open('password.txt','w').write(str(CRYPT()(input('password:'))[0]))"
password: *****
```

2) (re)use it:

```
./web3py-start -p password.txt apps
```
