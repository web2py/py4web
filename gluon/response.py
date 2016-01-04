import Cookie
import cgi
from gluon.helpers import XML
from gluon.streamer import stream_file_or_304_or_206
from gluon.template import render
from gluon.memoize_property import memoize_property

have_minify = False # FIX THIS
css_template = '<link href="%s" rel="stylesheet" type="text/css" />'
js_template = '<script src="%s" type="text/javascript"></script>'
coffee_template = '<script src="%s" type="text/coffee"></script>'
typescript_template = '<script src="%s" type="text/typescript"></script>'
less_template = '<link href="%s" rel="stylesheet/less" type="text/css" />'
css_inline = '<style type="text/css">\n%s\n</style>'
js_inline = '<script type="text/javascript">\n%s\n</script>'

template_mapping = {
    'css': css_template,
    'js': js_template,
    'coffee': coffee_template,
    'ts': typescript_template,
    'less': less_template,
    'css:inline': css_inline,
    'js:inline': js_inline
}

class Response(object):
    def __init__(self):
        self.status = 200
        self.headers = {}
        self.view = {}
        self.flash = None
        self.files = []
        self.render = render
        self.auto_commit = True
        self.static_version = None

    @memoize_property
    def cookies(self):
        return Cookie.SimpleCookie()

    def stream(self, filename):
        stream_file_or_304_or_206(filename, environ=current.request.environ)

    def include_meta(self):
        s = "\n"
        for meta in getattr(self,'meta',{}).iteritems():
            k, v = meta
            if isinstance(v, dict):
                s += '<meta' + ''.join(' %s="%s"' % (xmlescape(key), xmlescape(v[key])) for key in v) +' />\n'
            else:
                s += '<meta name="%s" content="%s" />\n' % (k, cgi.escape(v))
        return XML(s)
        
    def include_files(self, extensions=None):

        """                                                                                                                                                                                                                                                                                                                                                                                                                          
        Includes files (usually in the head).                                                                                                                                                                                                                                                                                                                                                                                        
        Can minify and cache local files                                                                                                                                                                                                                                                                                                                                                                                             
        By default, caches in ram for 5 minutes. To change,                                                                                                                                                                                                                                                                                                                                                                          
        response.cache_includes = (cache_method, time_expire).                                                                                                                                                                                                                                                                                                                                                                       
        Example: (cache.disk, 60) # caches to disk for 1 minute.                                                                                                                                                                                                                                                                                                                                                                     
        """
        files = []
        ext_files = []
        has_js = has_css = False
        for item in self.files:
            if isinstance(item, (list, tuple)):
                ext_files.append(item)
                continue
            if extensions and not item.rpartition('.')[2] in extensions:
                continue
            if item in files:
                continue
            if item.endswith('.js'):
                has_js = True
            if item.endswith('.css'):
                has_css = True
            files.append(item)

        if have_minify and ((self.optimize_css and has_css) or (self.optimize_js and has_js)):
            # cache for 5 minutes by default                                                                                                                                                                                                                                                                                                                                                                                         
            key = hashlib.md5(repr(files)).hexdigest()

            cache = self.cache_includes or (current.cache.ram, 60 * 5)

            def call_minify(files=files):
                return minify.minify(files,
                                     URL('static', 'temp'),
                                     current.request.folder,
                                     self.optimize_css,
                                     self.optimize_js)
            if cache:
                cache_model, time_expire = cache
                files = cache_model('response.files.minified/' + key,
                                    call_minify,
                                    time_expire)
            else:
                files = call_minify()

        files.extend(ext_files)
        s = []
        for item in files:
            if isinstance(item, str):
                f = item.lower().split('?')[0]
                ext = f.rpartition('.')[2]
                # if static_version we need also to check for                                                                                                                                                                                                                                                                                                                                                                        
                # static_version_urls. In that case, the _.x.x.x                                                                                                                                                                                                                                                                                                                                                                     
                # bit would have already been added by the URL()                                                                                                                                                                                                                                                                                                                                                                     
                # function                                                                                                                                                                                                                                                                                                                                                                                                           
                if self.static_version and not self.static_version_urls:
                    item = item.replace(
                        '/static/', '/static/_%s/' % self.static_version, 1)
                tmpl = template_mapping.get(ext)
                if tmpl:
                    s.append(tmpl % item)
            elif isinstance(item, (list, tuple)):
                f = item[0]
                tmpl = template_mapping.get(f)
                if tmpl:
                    s.append(tmpl % item[1])
        return XML(''.join(s))
