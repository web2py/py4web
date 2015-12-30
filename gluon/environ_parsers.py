import Cookie
import urlparse
import tempfile
import copy
import shutil
from gluon.http import HTTP
from gluon.storage import Storage

def parse_cookies(environ):
    cookies = Cookie.SimpleCookie() 
    env_cookie = environ.get('HTTP_COOKIE','')
    if env_cookie:
        for single_cookie in env_cookie.split(';'):
            single_cookie = single_cookie.strip()
            if single_cookie:
                try:
                    cookies.load(single_cookie)
                except Cookie.CookieError:
                    pass  # single invalid cookie ignore
    return cookies

def parse_body(environ):
    try:
        try:  # Android requires this
            dest = tempfile.NamedTemporaryFile()
        except NotImplementedError:  # and GAE this
            dest = tempfile.TemporaryFile()
        shutil.copyfileobj(dest,environ['wsgi.input'])
        return dest
    except IOError:
        raise HTTP(400, "Bad Request - HTTP body is incomplete")

def parse_get_vars(environ):
    """Takes the QUERY_STRING and unpacks it to get_vars"""
    # Ref: https://docs.python.org/2/library/cgi.html#cgi.parse_qs
    query_string = environ.get('QUERY_STRING', '')
    dget = urlparse.parse_qs(query_string, keep_blank_values=1)  
    get_vars = Storage(dget)
    for (key, value) in get_vars.iteritems():
        if isinstance(value, list) and len(value) == 1:
            get_vars[key] = value[0]
    return get_vars

def parse_post_vars(environ, body):
    """
    Takes the body of the request and unpacks it into                                                                                                                                                                                                 
    post_vars. application/json is also automatically parsed                                                                                                                                                                                             
    """
    post_vars = Storage()
    # if content-type is application/json, we must read the body                                                                                                                                                                                         
    is_json = environ.get('content_type', '')[:16] == 'application/json'

    if is_json:
        try:
            json_vars = sj.load(body)
        except:
            # incoherent request bodies can still be parsed "ad-hoc"                                                                                                                                                                                     
            json_vars = {}
            pass
        # update vars and get_vars with what was posted as json                                                                                                                                                                                          
        if isinstance(json_vars, dict):
            post_vars.update(json_vars)
            
        body.seek(0)

    # parse POST variables on POST, PUT, BOTH only in post_vars                                                                                                                                                                                          
    if (body and not is_json
        and environ.request_method in ('POST', 'PUT', 'DELETE', 'BOTH')):
        query_string = environ.pop('QUERY_STRING', None)
        dpost = cgi.FieldStorage(fp=body, environ=environ, keep_blank_values=1)
        try:
            post_vars.update(dpost)
        except:
            pass
        if query_string is not None:
            environ['QUERY_STRING'] = query_string
        # The same detection used by FieldStorage to detect multipart POSTs                                                                                                                                                                              
        body.seek(0)
            
        def listify(a):
            return (not isinstance(a, list) and [a]) or a
        try:
            keys = sorted(dpost)
        except TypeError:
            keys = []
        for key in keys:
            if key is None:
                continue  # not sure why cgi.FieldStorage returns None key                                                                                                                                                                               
            dpk = dpost[key]
            # if an element is not a file replace it with                                                                                                                                                                                                
            # its value else leave it alone
            pvalue = listify([(_dpk if _dpk.filename else _dpk.value)
                              for _dpk in dpk]
                             if isinstance(dpk, list) else
                             (dpk if dpk.filename else dpk.value))
            if len(pvalue):
                post_vars[key] = (len(pvalue) > 1 and pvalue) or pvalue[0]
    return post_vars

def parse_all_vars(get_vars, post_vars):
    vars = copy.copy(get_vars)
    for key, value in post_vars.iteritems():
        if key not in vars:
            vars[key] = value
        else:
            if not isinstance(vars[key], list):
                vars[key] = [vars[key]]
            vars[key] += value if isinstance(value, list) else [value]
    return vars
