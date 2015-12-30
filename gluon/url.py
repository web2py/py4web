import re
from gluon.utils import web2py_uuid, simple_hash, compare

regex_crlf = re.compile('\r|\n')

def url_out(request, environ, application, controller, function,
            args, other, scheme, host, port, language=None):
    """Assembles and rewrites outgoing URL"""
    url = '/%s/%s/%s%s' % (application, controller, function, other)
    if host is True or (host is None and (scheme or port is not None)):
        host = request.env.http_host
    if not scheme or scheme is True:
        scheme = request.env.get('wsgi_url_scheme', 'http').lower() \
            if request else 'http'
    if host:
        host_port = host if not port else host.split(':', 1)[0] + ':%s' % port
        url = '%s://%s%s' % (scheme, host_port, url)
    return url

def URL(
    a=None,
    c=None,
    f=None,
    r=None,
    args=None,
    vars=None,
    anchor='',
    extension=None,
    env=None,
    hmac_key=None,
    hash_vars=True,
    salt=None,
    user_signature=None,
    scheme=None,
    host=None,
    port=None,
    encode_embedded_slash=False,
    url_encode=True,
    language=None,
):
    """
    generates a url '/a/c/f' corresponding to application a, controller c
    and function f. If r=request is passed, a, c, f are set, respectively,
    to r.application, r.controller, r.function.

    The more typical usage is:

        URL('index')

    that generates a url for the index function
    within the present application and controller.

    Args:
        a: application (default to current if r is given)
        c: controller (default to current if r is given)
        f: function (default to current if r is given)
        r: request (optional)
        args: any arguments (optional). Additional "path" elements
        vars: any variables (optional). Querystring elements
        anchor: anchorname, without # (optional)
        extension: force an extension
        hmac_key: key to use when generating hmac signature (optional)
        hash_vars: which of the vars to include in our hmac signature
            True (default) - hash all vars, False - hash none of the vars,
            iterable - hash only the included vars ['key1','key2']
        salt: salt hashing with this string
        user_signature: signs automatically the URL in such way that only the
            user can access the URL (use with `URL.verify` or
            `auth.requires_signature()`)
        scheme: URI scheme (True, 'http' or 'https', etc); forces absolute URL (optional)
        host: string to force absolute URL with host (True means http_host)
        port: optional port number (forces absolute URL)
        encode_embedded_slash: encode slash characters included in args
        url_encode: encode characters included in vars

    Raises:
        SyntaxError: when no application, controller or function is available
            or when a CRLF is found in the generated url

    Examples:

    >>> str(URL(a='a', c='c', f='f', args=['x', 'y', 'z'],
    ...     vars={'p':1, 'q':2}, anchor='1'))
    '/a/c/f/x/y/z?p=1&q=2#1'

    >>> str(URL(a='a', c='c', f='f', args=['x', 'y', 'z'],
    ...     vars={'p':(1,3), 'q':2}, anchor='1'))
    '/a/c/f/x/y/z?p=1&p=3&q=2#1'

    >>> str(URL(a='a', c='c', f='f', args=['x', 'y', 'z'],
    ...     vars={'p':(3,1), 'q':2}, anchor='1'))
    '/a/c/f/x/y/z?p=3&p=1&q=2#1'

    >>> str(URL(a='a', c='c', f='f', anchor='1+2'))
    '/a/c/f#1%2B2'

    >>> str(URL(a='a', c='c', f='f', args=['x', 'y', 'z'],
    ...     vars={'p':(1,3), 'q':2}, anchor='1', hmac_key='key'))
    '/a/c/f/x/y/z?p=1&p=3&q=2&_signature=a32530f0d0caa80964bb92aad2bedf8a4486a31f#1'

    >>> str(URL(a='a', c='c', f='f', args=['w/x', 'y/z']))
    '/a/c/f/w/x/y/z'

    >>> str(URL(a='a', c='c', f='f', args=['w/x', 'y/z'], encode_embedded_slash=True))
    '/a/c/f/w%2Fx/y%2Fz'

    >>> str(URL(a='a', c='c', f='f', args=['%(id)d'], url_encode=False))
    '/a/c/f/%(id)d'

    >>> str(URL(a='a', c='c', f='f', args=['%(id)d'], url_encode=True))
    '/a/c/f/%25%28id%29d'

    >>> str(URL(a='a', c='c', f='f', vars={'id' : '%(id)d' }, url_encode=False))
    '/a/c/f?id=%(id)d'

    >>> str(URL(a='a', c='c', f='f', vars={'id' : '%(id)d' }, url_encode=True))
    '/a/c/f?id=%25%28id%29d'

    >>> str(URL(a='a', c='c', f='f', anchor='%(id)d', url_encode=False))
    '/a/c/f#%(id)d'

    >>> str(URL(a='a', c='c', f='f', anchor='%(id)d', url_encode=True))
    '/a/c/f#%25%28id%29d'
    """

    from gluon.main import current

    if args in (None, []):
        args = []
    vars = vars or {}
    application = None
    controller = None
    function = None

    if not isinstance(args, (list, tuple)):
        args = [args]

    if not r:
        if a and not c and not f:
            (f, a, c) = (a, c, f)
        elif a and c and not f:
            (c, f, a) = (a, c, f)
        from globals import current
        if hasattr(current, 'request'):
            r = current.request

    if r:
        application = r.application
        controller = r.controller
        function = r.function
        env = r.env
        if extension is None and r.extension != 'html':
            extension = r.extension
    if a:
        application = a
    if c:
        controller = c
    if f:
        if not isinstance(f, str):
            if hasattr(f, '__name__'):
                function = f.__name__
            else:
                raise SyntaxError('when calling URL, function or function name required')
        elif '/' in f:
            if f.startswith("/"):
                f = f[1:]
            items = f.split('/')
            function = f = items[0]
            args = items[1:] + args
        else:
            function = f

        # if the url gets a static resource, don't force extention
        if controller == 'static':
            extension = None
            # add static version to url
            if hasattr(current, 'response'):
                response = current.response
                if response.static_version and response.static_version_urls:
                    args = [function] + args
                    function = '_'+str(response.static_version)

        if '.' in function:
            function, extension = function.rsplit('.', 1)

    function2 = '%s.%s' % (function, extension or 'html')

    if not (application and controller and function):
        raise SyntaxError('not enough information to build the url (%s %s %s)' % (application, controller, function))

    if args:
        if url_encode:
            if encode_embedded_slash:
                other = '/' + '/'.join([urllib.quote(str(
                    x), '') for x in args])
            else:
                other = args and urllib.quote(
                    '/' + '/'.join([str(x) for x in args]))
        else:
            other = args and ('/' + '/'.join([str(x) for x in args]))
    else:
        other = ''

    if other.endswith('/'):
        other += '/'    # add trailing slash to make last trailing empty arg explicit

    list_vars = []
    for (key, vals) in sorted(vars.items()):
        if key == '_signature':
            continue
        if not isinstance(vals, (list, tuple)):
            vals = [vals]
        for val in vals:
            list_vars.append((key, val))

    if user_signature:
        from globals import current
        if current.session.auth:
            hmac_key = current.session.auth.hmac_key

    if hmac_key:
        # generate an hmac signature of the vars & args so can later
        # verify the user hasn't messed with anything

        h_args = '/%s/%s/%s%s' % (application, controller, function2, other)

        # how many of the vars should we include in our hash?
        if hash_vars is True:       # include them all
            h_vars = list_vars
        elif hash_vars is False:    # include none of them
            h_vars = ''
        else:                       # include just those specified
            if hash_vars and not isinstance(hash_vars, (list, tuple)):
                hash_vars = [hash_vars]
            h_vars = [(k, v) for (k, v) in list_vars if k in hash_vars]

        # re-assembling the same way during hash authentication
        message = h_args + '?' + urllib.urlencode(sorted(h_vars))
        sig = simple_hash(
            message, hmac_key or '', salt or '', digest_alg='sha1')
        # add the signature into vars
        list_vars.append(('_signature', sig))

    if list_vars:
        if url_encode:
            other += '?%s' % urllib.urlencode(list_vars)
        else:
            other += '?%s' % '&'.join(['%s=%s' % var[:2] for var in list_vars])
    if anchor:
        if url_encode:
            other += '#' + urllib.quote(str(anchor))
        else:
            other += '#' + (str(anchor))
    if extension:
        function += '.' + extension

    if regex_crlf.search(join([application, controller, function, other])):
        raise SyntaxError('CRLF Injection Detected')

    url = url_out(r, env, application, controller, function,
                  args, other, scheme, host, port, language=language)
    return url


def verifyURL(request, hmac_key=None, hash_vars=True, salt=None, user_signature=None):
    """
    Verifies that a request's args & vars have not been tampered with by the user

    :param request: web2py's request object
    :param hmac_key: the key to authenticate with, must be the same one previously
                    used when calling URL()
    :param hash_vars: which vars to include in our hashing. (Optional)
                    Only uses the 1st value currently
                    True (or undefined) means all, False none,
                    an iterable just the specified keys

    do not call directly. Use instead:

    URL.verify(hmac_key='...')

    the key has to match the one used to generate the URL.

        >>> r = Storage()
        >>> gv = Storage(p=(1,3),q=2,_signature='a32530f0d0caa80964bb92aad2bedf8a4486a31f')
        >>> r.update(dict(application='a', controller='c', function='f', extension='html'))
        >>> r['args'] = ['x', 'y', 'z']
        >>> r['get_vars'] = gv
        >>> verifyURL(r, 'key')
        True
        >>> verifyURL(r, 'kay')
        False
        >>> r.get_vars.p = (3, 1)
        >>> verifyURL(r, 'key')
        True
        >>> r.get_vars.p = (3, 2)
        >>> verifyURL(r, 'key')
        False

    """

    if not '_signature' in request.get_vars:
        return False  # no signature in the request URL

    # check if user_signature requires
    if user_signature:
        from globals import current
        if not current.session or not current.session.auth:
            return False
        hmac_key = current.session.auth.hmac_key
    if not hmac_key:
        return False

    # get our sig from request.get_vars for later comparison
    original_sig = request.get_vars._signature

    # now generate a new hmac for the remaining args & vars
    vars, args = request.get_vars, request.args

    # remove the signature var since it was not part of our signed message
    request.get_vars.pop('_signature')

    # join all the args & vars into one long string

    # always include all of the args
    other = args and urllib.quote('/' + '/'.join([str(x) for x in args])) or ''
    h_args = '/%s/%s/%s.%s%s' % (request.application,
                                 request.controller,
                                 request.function,
                                 request.extension,
                                 other)

    # but only include those vars specified (allows more flexibility for use with
    # forms or ajax)

    list_vars = []
    for (key, vals) in sorted(vars.items()):
        if not isinstance(vals, (list, tuple)):
            vals = [vals]
        for val in vals:
            list_vars.append((key, val))

    # which of the vars are to be included?
    if hash_vars is True:       # include them all
        h_vars = list_vars
    elif hash_vars is False:    # include none of them
        h_vars = ''
    else:                       # include just those specified
        # wrap in a try - if the desired vars have been removed it'll fail
        try:
            if hash_vars and not isinstance(hash_vars, (list, tuple)):
                hash_vars = [hash_vars]
            h_vars = [(k, v) for (k, v) in list_vars if k in hash_vars]
        except:
            # user has removed one of our vars! Immediate fail
            return False
    # build the full message string with both args & vars
    message = h_args + '?' + urllib.urlencode(sorted(h_vars))

    # hash with the hmac_key provided
    sig = simple_hash(message, str(hmac_key), salt or '', digest_alg='sha1')

    # put _signature back in get_vars just in case a second call to URL.verify is performed
    # (otherwise it'll immediately return false)
    request.get_vars['_signature'] = original_sig

    # return whether or not the signature in the request matched the one we just generated
    # (I.E. was the message the same as the one we originally signed)

    return compare(original_sig, sig)

URL.verify = verifyURL
