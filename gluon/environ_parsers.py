import cgi
import Cookie
import urlparse
import tempfile
import copy
import json
import cStringIO
import shutil
import sys
from gluon.http import HTTP
from gluon.storage import Storage
from gluon.fileutils import copystream

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
    if not environ.get('CONTENT_LENGTH', None):
        return cStringIO.StringIO()
    try:
        size = int(environ['CONTENT_LENGTH'])
    except ValueError:
        raise HTTP(400, "Invalid Content-Length header")
    try:
        source = environ['wsgi.input']
        try:  # Android requires this
            dest = tempfile.NamedTemporaryFile()
        except NotImplementedError:  # and GAE this
            dest = tempfile.TemporaryFile()
        copystream(source, dest, size, chunk_size = 10**5)
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
    is_json = environ.get('CONTENT_TYPE', '')[:16] == 'application/json'

    if is_json:
        try:
            json_vars = json.load(body)
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
        and environ.get('REQUEST_METHOD') in ('POST', 'PUT', 'DELETE', 'BOTH')):
        query_string = environ.pop('QUERY_STRING', None)
        dpost = cgi.FieldStorage(fp=body, environ=environ, keep_blank_values=1)
        try: post_vars.update(dpost)
        except: pass
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

def parse_user_agent(environ):
    user_agent = detect_agent(environ.get('HTTP_USER_AGENT'))
    for key, value in user_agent.items():
        if isinstance(value, dict):
            user_agent[key] = Storage(value)
    return Storage(user_agent)


"""
Code below user by parse_user_agent
Extract client information from http user agent
The module does not try to detect all capabilities of browser in current form (it can easily be extended though).
Aim is
    * fast
    * very easy to extend
    * reliable enough for practical purposes
    * and assist python web apps to detect clients.

Taken from http://pypi.python.org/pypi/httpagentparser (MIT license)
Modified my Ross Peoples for web2py to better support iPhone and iPad.
Modified by Angelo Compagnucci <angelo.compagnucci@gmail.com> to better support a wide ringe of mobile devices.
Now it supports: tablet device (is_tablet), BlackBerry, BlackBerry PlayBook, Android Tablets, Windows Mobile,
Symbian.
"""

class DetectorsHub(dict):
    _known_types = ['os', 'dist', 'flavor', 'browser']

    def __init__(self, *args, **kw):
        dict.__init__(self, *args, **kw)
        for typ in self._known_types:
            self.setdefault(typ, [])
        self.registerDetectors()

    def register(self, detector):
        if detector.info_type not in self._known_types:
            self[detector.info_type] = [detector]
            self._known_types.insert(detector.order, detector.info_type)
        else:
            self[detector.info_type].append(detector)

    def reorderByPrefs(self, detectors, prefs):
        if prefs is None:
            return []
        elif prefs == []:
            return detectors
        else:
            prefs.insert(0, '')

            def key_name(d):
                return d.name in prefs and prefs.index(d.name) or sys.maxint
            return sorted(detectors, key=key_name)

    def __iter__(self):
        return iter(self._known_types)

    def registerDetectors(self):
        detectors = [v() for v in globals().values()
                     if DetectorBase in getattr(v, '__mro__', [])]
        for d in detectors:
            if d.can_register:
                self.register(d)


class DetectorBase(object):
    name = ""  # "to perform match in DetectorsHub object"
    info_type = ''  # override me
    result_key = ''  # override me
    order = 10  # 0 is highest
    look_for = []  # list of words to look for
    skip_if_found = []  # strings if present stop processin
    can_register = False
    is_mobile = False
    is_tablet = False
    prefs = dict()  # dict(info_type = [name1, name2], ..)
    version_splitters = ["/", " "]
    _suggested_detectors = None

    def __init__(self):
        if not self.name:
            self.name = self.__class__.__name__
        self.can_register = (self.__class__.__dict__.get('can_register', True))

    def detect(self, agent, result):
        if agent and self.checkWords(agent):
            result[self.info_type] = dict(name=self.name)
            is_mobile = self.is_mobile
            is_tablet = self.is_tablet
            if is_mobile:
                result['is_mobile'] = is_mobile
            if is_tablet:
                result['is_tablet'] = is_tablet

            version = self.getVersion(agent)
            if version:
                result[self.info_type]['version'] = version

            return True
        return False

    def checkWords(self, agent):
        for w in self.skip_if_found:
            if w in agent:
                return False
        for w in self.look_for:
            if not w in agent:
                return False
        return True

    # This works only for the first element of look_for
    # If you want a different behaviour, you have to
    # override this method
    def getVersion(self, agent):
        # -> version string /None
        vs = self.version_splitters
        return agent.partition(self.look_for[0] + vs[0])[2].partition(vs[1])[0].strip()


class OS(DetectorBase):
    info_type = "os"
    can_register = False
    version_splitters = [";", " "]


class Dist(DetectorBase):
    info_type = "dist"
    can_register = False


class Flavor(DetectorBase):
    info_type = "flavor"
    can_register = False


class Browser(DetectorBase):
    info_type = "browser"
    can_register = False


class Macintosh(OS):
    look_for = ['Macintosh']
    prefs = dict(dist=None)

    def getVersion(self, agent):
        pass


class Firefox(Browser):
    look_for = ["Firefox"]


class Konqueror(Browser):
    look_for = ["Konqueror"]
    version_splitters = ["/", ";"]


class Opera(Browser):
    look_for = ["Opera"]

    def getVersion(self, agent):
        return agent.partition(self.look_for[0])[2][1:].partition(' ')[0]


class Netscape(Browser):
    look_for = ["Netscape"]


class MSIE(Browser):
    look_for = ["MSIE"]
    skip_if_found = ["Opera"]
    name = "Microsoft Internet Explorer"
    version_splitters = [" ", ";"]


class Galeon(Browser):
    look_for = ["Galeon"]


class Safari(Browser):
    look_for = ["Safari"]
    skip_if_found = ["Chrome", "OmniWeb", "Mobile", "iPad", 'Android']

    def getVersion(self, agent):
        if "Version/" in agent:
            return agent.partition('Version/')[2].partition(' ')[0].strip()


class SafariTablet(Browser):
    name = "Safari"
    look_for = ['Safari', 'Android']
    skip_if_found = ["Chrome", "OmniWeb", "Mobile", "iPad"]
    is_mobile = True
    is_tablet = True

    def getVersion(self, agent):
        if "Version/" in agent:
            return agent.partition('Version/')[2].partition(' ')[0].strip()


class SafariMobile(Browser):
    name = "Safari"
    look_for = ["Safari", "Mobile"]
    is_mobile = True

    def getVersion(self, agent):
        if "Version/" in agent:
            return agent.partition('Version/')[2].partition(' ')[0].strip()


class SafariNokia(Browser):
    name = "Safari"
    look_for = ["Safari", "SymbianOS"]
    is_mobile = True

    def getVersion(self, agent):
        pass


class SafariiPad(Browser):
    name = "Safari"
    look_for = ["Safari", "iPad"]
    skip_if_found = ["Chrome", "OmniWeb"]
    is_mobile = True
    is_tablet = True

    def getVersion(self, agent):
        if "Version/" in agent:
            return agent.partition('Version/')[2].partition(' ')[0].strip()


class Linux(OS):
    look_for = ["Linux"]
    prefs = dict(dist=["Ubuntu", "Android", "Debian"], flavor=None)

    def getVersion(self, agent):
        pass


class BlackBerry(OS):
    look_for = ['BlackBerry']
    prefs = dict(flavor=['PlayBook'])
    is_mobile = True

    # Manual check for tablet
    def checkWords(self, agent):
        if 'BlackBerry' in agent or 'PlayBook' in agent:
            return True
        return False

    def getVersion(self, agent):
        pass


class PlayBook(Flavor):
    look_for = ['PlayBook']
    is_mobile = True
    is_tablet = True

    def getVersion(self, agent):
        return agent.partition('Tablet OS')[2].partition(';')[0].strip()


class Macintosh(OS):
    look_for = ['Macintosh']
    prefs = dict(dist=None, flavor=['MacOS'])

    def getVersion(self, agent):
        pass


class MacOS(Flavor):
    look_for = ['Mac OS']
    prefs = dict(browser=['Safari', 'SafariMobile', 'SafariIpad',
                 'Firefox', 'Opera', "Microsoft Internet Explorer"])

    def getVersion(self, agent):
        version_end_chars = [';', ')']
        part = agent.partition('Mac OS')[2].strip()
        for c in version_end_chars:
            if c in part:
                version = part.partition(c)[0]
                break
        return version.replace('_', '.')


class Windows(OS):
    look_for = ['Windows', 'NT']
    prefs = dict(browser=["Microsoft Internet Explorer", 'Firefox'],
                 dist=['WindowsMobile'], flavor=None)

    def getVersion(self, agent):
        v = agent.partition('NT')
        return v[1] + ' ' + v[2].replace(')', ';').partition(';')[0].strip()


class WindowsMobile(Dist):
    name = 'Phone'
    look_for = ['Windows', 'Phone']
    is_mobile = True

    def getVersion(self, agent):
        return agent.partition('Windows Phone')[2].replace(')', '').partition(';')[0].strip()


class Ubuntu(Dist):
    look_for = ['Ubuntu']
    version_splitters = ["/", " "]
    prefs = dict(browser=['Firefox'])


class Debian(Dist):
    look_for = ['Debian']
    version_splitters = ["/", " "]
    prefs = dict(browser=['Firefox'])


class Chrome(Browser):
    look_for = ['Chrome']
    version_splitters = ["/", " "]


class ChromeOS(OS):
    look_for = ['CrOS']
    version_splitters = [" ", ")"]
    prefs = dict(browser=['Chrome'])

    def getVersion(self, agent):
        vs = self.version_splitters
        return agent.partition(self.look_for[0] + vs[0])[2].partition(vs[1])[0].partition(" ")[2].strip()


class Android(Dist):
    look_for = ['Android']
    prefs = dict(browser=['SafariTablet', 'SafariMobile'])
    is_mobile = True

    def getVersion(self, agent):
        return agent.partition('Android')[2].partition(';')[0].strip()


class SymbianOS(OS):
    look_for = ['SymbianOS']
    prefs = dict(dist=['Series'], browser=['Safari', 'Opera'])
    is_mobile = True
    version_splitters = ['/', '; ']


class Series(Flavor):
    look_for = ['SymbianOS', 'Series']
    version_splitters = ['/', ';']

    def getVersion(self, agent):
        return agent.partition('Series')[2].partition(' ')[0].replace('/', ' ')


class BrowserNG(Browser):
    look_for = ['BrowserNG']
    version_splitters = ['/', ';']


class iPhone(Dist):
    look_for = ['iPhone']
    is_mobile = True
    prefs = dict(browser=['SafariMobile'])

    def getVersion(self, agent):
        version_end_chars = ['like', ';', ')']
        if (not 'CPU iPhone OS' in agent) and (not 'CPU OS' in agent):
            return 'X'
        part = agent.partition('OS')[2].strip()
        for c in version_end_chars:
            if c in part:
                version = 'iOS ' + part.partition(c)[0].strip()
                break
        return version.replace('_', '.')


class iPad(Dist):
    look_for = ['iPad']
    is_mobile = True
    is_tablet = True

    def getVersion(self, agent):
        version_end_chars = ['like', ';', ')']
        if not 'OS' in agent:
            return ''
        part = agent.partition('OS')[2].strip()
        for c in version_end_chars:
            if c in part:
                version = 'iOS ' + part.partition(c)[0].strip()
                break
        return version.replace('_', '.')

detectorshub = DetectorsHub()


def detect_agent(agent):
    result = dict()
    prefs = dict()
    result['is_mobile'] = False
    result['is_tablet'] = False
    for info_type in detectorshub:
        detectors = detectorshub[info_type]
        _d_prefs = prefs.get(info_type, [])
        detectors = detectorshub.reorderByPrefs(detectors, _d_prefs)
        try:
            for detector in detectors:
                if detector.detect(agent, result):
                    prefs = detector.prefs
                    break
        except Exception, ex:
            result['exception'] = ex
    # hack to address https://code.google.com/p/web2py/issues/detail?id=1755
    if not 'browser' in result:
        result['browser'] = {'name':'IE11'}
    return result


class Result(dict):
    def __missing__(self, k):
        return ""


def simple_detect(agent):
    """
    -> (os, browser, is_mobile) # tuple of strings
    """
    result = detect(agent)
    os_list = []
    if 'flavor' in result:
        os_list.append(result['flavor']['name'])
    if 'dist' in result:
        os_list.append(result['dist']['name'])
    if 'os' in result:
        os_list.append(result['os']['name'])

    os = os_list and " ".join(os_list) or "Unknown OS"
    os_version = os_list and ('flavor' in result and result['flavor'] and result['flavor'].get(
        'version')) or ('dist' in result and result['dist'] and result['dist'].get('version')) \
        or ('os' in result and result['os'] and result['os'].get('version')) or ""
    browser = 'browser' in result and result['browser'][
        'name'] or 'Unknown Browser'
    browser_version = 'browser' in result \
        and result['browser'].get('version') or ""
    if browser_version:
        browser = " ".join((browser, browser_version))
    if os_version:
        os = " ".join((os, os_version))
    #is_mobile = ('dist' in result and result.dist.is_mobile) or ('os' in result and result.os.is_mobile) or False
    return os, browser, result['is_mobile']


if __name__ == '__main__':
    import time
    import unittest

    data = (


        (
            'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.83; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
            ('Series SymbianOS 60 3.1', 'Safari', True),
            {'is_mobile': True, 'is_tablet': False, 'flavor': {'name': 'Series', 'version': '60 3.1'}, 'os': {'name': 'SymbianOS', 'version': '9.2'}, 'browser': {'name': 'Safari'}},),
        (
            'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
            ('Series SymbianOS 60 5.0', 'BrowserNG 7.1.18124', True),
            {'is_mobile': True, 'is_tablet': False, 'flavor': {'name': 'Series', 'version': '60 5.0'}, 'os': {'name': 'SymbianOS', 'version': '9.4'}, 'browser': {'name': 'BrowserNG', 'version': '7.1.18124'}},),
        (
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Windows Phone 6.5.3.5)',
            ('Phone Windows 6.5.3.5', 'Microsoft Internet Explorer 6.0', True),
            {'is_mobile': True, 'is_tablet': False, 'dist': {'name': 'Phone', 'version': '6.5.3.5'}, 'os': {'name': 'Windows', 'version': 'NT 5.1'}, 'browser': {'name': 'Microsoft Internet Explorer', 'version': '6.0'}},),
        (
            'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 1.0.0; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/0.0.1 Safari/534.8+',
            ('PlayBook BlackBerry 1.0.0', 'Safari 0.0.1', True),
            {'is_mobile': True, 'is_tablet': True, 'flavor': {'name': 'PlayBook', 'version': '1.0.0'}, 'os': {'name': 'BlackBerry'}, 'browser': {'name': 'Safari', 'version': '0.0.1'}},),
        (
            'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+',
            ('BlackBerry', 'Safari 6.0.0.246', True),
            {'is_mobile': True, 'is_tablet': False, 'os': {'name': 'BlackBerry'}, 'browser': {'name': 'Safari', 'version': '6.0.0.246'}},),
        (
            'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.600 Mobile Safari/534.8+',
            ('BlackBerry', 'Safari 6.0.0.600', True),
            {'is_mobile': True, 'is_tablet': False, 'os': {'name': 'BlackBerry'}, 'browser': {'name': 'Safari', 'version': '6.0.0.600'}},),
        (
            'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
            ('MacOS iPad X', 'Safari 5.0.2', True),
            {'is_mobile': True, 'is_tablet': True, 'flavor': {'version': 'X', 'name': 'MacOS'}, 'dist': {'version': 'iOS 4.2.1', 'name': 'iPad'}, 'browser': {'name': 'Safari', 'version': '5.0.2'}},),
        (
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20060127 Netscape/8.1',
            ('Windows NT 5.1', 'Netscape 8.1', False),
            {'is_mobile': False, 'is_tablet': False, 'os': {'name': 'Windows', 'version': 'NT 5.1'}, 'browser': {'name': 'Netscape', 'version': '8.1'}},),
        (
            'Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
            ('Android Linux 3.0.1', 'Safari 4.0', True),
            {'is_mobile': True, 'is_tablet': True, 'dist': {'version': '3.0.1', 'name': 'Android'}, 'os': {'name': 'Linux'}, 'browser': {'version': '4.0', 'name': 'Safari'}},),
        (
            'Mozilla/5.0 (Linux; U; Android 2.3.7; it-it; Dream/Sapphire Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            ('Android Linux 2.3.7', 'Safari 4.0', True),
            {'is_mobile': True, 'is_tablet': False, 'dist': {'version': '2.3.7', 'name': 'Android'}, 'os': {'name': 'Linux'}, 'browser': {'version': '4.0', 'name': 'Safari'}},),
        (
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-GB; rv:1.9.0.10) Gecko/2009042315 Firefox/3.0.10',
            ('MacOS Macintosh X 10.5', 'Firefox 3.0.10', False),
            {'is_mobile': False, 'is_tablet': False, 'flavor': {'version': 'X 10.5', 'name': 'MacOS'}, 'os': {'name': 'Macintosh'}, 'browser': {'version': '3.0.10', 'name': 'Firefox'}},),
        (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24,gzip(gfe)',
            ('MacOS Macintosh X 10.6.6', 'Chrome 11.0.696.3', False),
            {'is_mobile': False, 'is_tablet': False, 'flavor': {'version': 'X 10.6.6', 'name': 'MacOS'}, 'os': {'name': 'Macintosh'}, 'browser': {'version': '11.0.696.3', 'name': 'Chrome'}},),
        (
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100308 Ubuntu/10.04 (lucid) Firefox/3.6 GTB7.1',
            ('Ubuntu Linux 10.04', 'Firefox 3.6', False),
            {'is_mobile': False, 'is_tablet': False, 'dist': {'version': '10.04', 'name': 'Ubuntu'}, 'os': {'name': 'Linux'}, 'browser': {'version': '3.6', 'name': 'Firefox'}},),
        (
            'Mozilla/5.0 (Linux; U; Android 2.2.1; fr-ch; A43 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            ('Android Linux 2.2.1', 'Safari 4.0', True),
            {'is_mobile': True, 'is_tablet': False, 'dist': {'version': '2.2.1', 'name': 'Android'}, 'os': {'name': 'Linux'}, 'browser': {'version': '4.0', 'name': 'Safari'}},),
        (
            'Mozilla/5.0 (Linux; U; Android 2.3.4; it-it; LG-P990 Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MMS/LG-Android-MMS-V1.0/1.2',
            ('Android Linux 2.3.4', 'Safari 4.0', True),
            {'is_mobile': True, 'is_tablet': False, 'dist': {'version': '2.3.4', 'name': 'Android'}, 'os': {'name': 'Linux'}, 'browser': {'version': '4.0', 'name': 'Safari'}},),
        (
            'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3',
            ('MacOS iPhone X', 'Safari 3.0', True),
            {'is_mobile': True, 'is_tablet': False, 'flavor': {'version': 'X', 'name': 'MacOS'}, 'dist': {'version': 'X', 'name': 'iPhone'}, 'browser': {'version': '3.0', 'name': 'Safari'}},),
        (
            'Mozilla/5.0 (X11; CrOS i686 0.0.0) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.27 Safari/534.24,gzip(gfe)',
            ('ChromeOS 0.0.0', 'Chrome 11.0.696.27', False),
            {'is_mobile': False, 'is_tablet': False, 'os': {'name': 'ChromeOS', 'version': '0.0.0'}, 'browser': {'name': 'Chrome', 'version': '11.0.696.27'}},),
        (
            'Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.02 [en]',
            ('Windows NT 5.1', 'Opera 7.02', False),
            {'is_mobile': False, 'is_tablet': False, 'os': {'name': 'Windows', 'version': 'NT 5.1'}, 'browser': {'name': 'Opera', 'version': '7.02'}},),
        ('Opera/9.80 (X11; Linux i686; U; en) Presto/2.9.168 Version/11.50',
         ('Linux', 'Opera 9.80', False),
            {'is_mobile': False, 'is_tablet': False, 'os': {'name': 'Linux'}, 'browser': {'name': 'Opera', 'version': '9.80'}},),
    )

    class TestHAP(unittest.TestCase):
        def setUp(self):
            self.harass_repeat = 100
            self.data = data

        def test_simple_detect(self):
            for agent, simple_res, res in data:
                self.assertEqual(simple_detect(agent), simple_res)

        def test_detect(self):
            for agent, simple_res, res in data:
                self.assertEqual(detect(agent), res)

        def test_harass(self):
            then = time.time()
            for agent, simple_res, res in data * self.harass_repeat:
                detect(agent)
            time_taken = time.time() - then
            no_of_tests = len(self.data) * self.harass_repeat
            print "\nTime taken for %s detecttions: %s" \
                % (no_of_tests, time_taken)
            print "Time taken for single detecttion: ", \
                time_taken / (len(self.data) * self.harass_repeat)

    unittest.main()


class mobilize(object):

    def __init__(self, func):
        self.func = func

    def __call__(self):
        from gluon import current
        user_agent = current.request.user_agent()
        if user_agent.is_mobile:
            items = current.response.view.split('.')
            items.insert(-1, 'mobile')
            current.response.view = '.'.join(items)
        return self.func()

