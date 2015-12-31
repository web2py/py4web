import cgi
import copy_reg

__all__ = ['A', 'BEAUTIFY', 'BODY', 'CODE', 'DIV', 'EM', 'FORM', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'HEAD', 'IMG', 'INPUT', 'LABEL', 'LI', 'METATAG', 'OL', 'OPTION', 'PRE', 'SELECT', 'SPAN', 'STRONG', 'TABLE', 'TAG', 'TAGGER', 'TBODY', 'TD', 'TEXTAREA', 'TH', 'THAED', 'TR', 'UL', 'XML', 'xmlescape']

# ################################################################
# New HTML Helpers
# ################################################################

def xmlescape(text):
    return cgi.escape(text, True).replace("'", "&#x27;")

class TAGGER(object):    

    def __init__(self, name, *children, **attributes):
        self.name = name
        self.children = list(children)
        self.attributes = attributes
        for child in self.children:
            if isinstance(child, TAGGER):
                child.parent = self

    def xml(self):
        name = self.name
        a = ' '.join('%s="%s"' % 
                     (k[1:], k[1:] if v is True else xmlescape(unicode(v)))
                     for k,v in self.attributes.iteritems() 
                     if k.startswith('_') and not v in (False,None))
        if a:
            a = ' '+a
        if name.endswith('/'):
            return '<%s%s/>' % (name, a)
        else:
            b = ''.join(s.xml() if isinstance(s,TAGGER) else xmlescape(unicode(s))
                        for s in self.children)
            return '<%s%s>%s</%s>' %(name, a, b, name)
    
    def __unicode__(self):
        return self.xml()

    def __str__(self):
        return self.xml().encode('utf8')

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.children[key]
        else:
            return self.attributes[key]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.children[key] = value
        else:
            self.attributes[key] =  value

    def append(self, value):
        self.children.append(value)

    def __delitem__(self,key):
        if isinstance(key, int):
            self.children = self.children[:key]+self.children[key+1:]
        else:
            del self.attributes[key]

    def __len__(self):
        return len(self.children)

    def find(self, query):
        raise NotImplementedError

class METATAG(object):

    def __getattr__(self, name):
        return self(name)

    def __getitem__(self, name):
        return lambda *children, **attributes: TAGGER(name, *children, **attributes)

TAG = METATAG()
DIV = TAG['div']
SPAN = TAG['span']
LI = TAG['li']
OL = TAG['ol']
UL = TAG['ul']
A  = TAG['a']
H1 = TAG['h1']
H2 = TAG['h2']
H3 = TAG['h3']
H4 = TAG['h4']
H5 = TAG['h5']
H6 = TAG['h6']
EM = TAG['em']
TR = TAG['tr']
TD = TAG['td']
TH = TAG['th']
IMG = TAG['img/']
PRE = TAG['pre']
CODE = TAG['code']
FORM = TAG['form']
HEAD = TAG['head']
BODY = TAG['body']
TABLE = TAG['thead']
THAED = TAG['tbody']
TBODY = TAG['table']
INPUT = TAG['input/']
LABEL = TAG['label']
STRONG = TAG['strong']
SELECT = TAG['select']
OPTION = TAG['option']
TEXTAREA = TAG['textarea']


# ################################################################
# New XML Helpers
# ################################################################

class XML(TAGGER):
    """
    use it to wrap a string that contains XML/HTML so that it will not be
    escaped by the template

    Examples:

    >>> XML('<h1>Hello</h1>').xml()
    '<h1>Hello</h1>'
    """

    def __init__(
        self,
        text,
        sanitize=False,
        permitted_tags=[
            'a','b','blockquote','br/','i','li','ol','ul','p','cite',
            'code','pre','img/','h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'table', 'tr', 'td', 'div','strong', 'span'],
        allowed_attributes={
            'a': ['href', 'title', 'target'],
            'img': ['src', 'alt'],
            'blockquote': ['type'],
            'td': ['colspan']},
        ):
        """
        Args:
            text: the XML text
            sanitize: sanitize text using the permitted tags and allowed
                attributes (default False)
            permitted_tags: list of permitted tags (default: simple list of
                tags)
            allowed_attributes: dictionary of allowed attributed (default
                for A, IMG and BlockQuote).
                The key is the tag; the value is a list of allowed attributes.
        """

        if sanitize:
            from gluon.sanitizer import sanitize
            text = sanitize(text, permitted_tags, allowed_attributes)
        if isinstance(text, unicode):
            text = text.encode('utf8', 'xmlcharrefreplace')
        elif not isinstance(text, str):
            text = str(text)
        self.text = text

    def xml(self):
        return self.text

    def __str__(self):
        return self.text

    def __add__(self, other):
        return '%s%s' % (self, other)

    def __radd__(self, other):
        return '%s%s' % (other, self)

    def __cmp__(self, other):
        return cmp(str(self), str(other))

    def __hash__(self):
        return hash(str(self))

    def __getitem__(self, i):
        return str(self)[i]

    def __getslice__(self, i, j):
        return str(self)[i:j]

    def __iter__(self):
        for c in str(self):
            yield c

    def __len__(self):
        return len(str(self))

def XML_unpickle(data):
    return XML(marshal.loads(data))

def XML_pickle(data):
    return XML_unpickle, (marshal.dumps(str(data)),)
copy_reg.pickle(XML, XML_pickle, XML_unpickle)

# ################################################################
# BEAUTIFY everything
# ################################################################

def BEAUTIFY(obj): # FIX ME, dealing with very large objects
    if isinstance(obj, TAGGER):
        return obj
    elif isinstance(obj, list):
        return UL(*[LI(BEAUTIFY(item)) for item in  obj])
    elif isinstance(obj, dict):
        return TABLE(TBODY(*[TR(TH(XML(key)),TD(BEAUTIFY(value))) for key, value in obj.iteritems()]))
    else:
        return XML(obj)
