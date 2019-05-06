import collections
import copy
import datetime
import functools
import re

# todo check tfieldnames
# expose template to tables

__version__ = '0.1'

class PolicyViolation(ValueError): pass
class InvalidFormat(ValueError): pass
class NotFound(ValueError): pass

def error_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = {}
        try:
            data = func(*args, **kwargs)
            if not data.get('errors'):
                data['status'] = 'success'
                data['code'] = 200
            else:
                data['status'] = 'error'
                data['message'] = 'Validation Errors'
                data['code'] = 422
        except PolicyViolation as e:
            data['status'] = 'error'
            data['message'] = str(e)
            data['code'] = 401
        except NotFound as e:
            data['status'] = 'error'
            data['message'] = str(e)
            data['code'] = 404
        except (InvalidFormat, KeyError, ValueError) as e:
            data['status'] = 'error'
            data['message'] = str(e)
            data['code'] = 400
        finally:
            data['timestamp'] = datetime.datetime.utcnow().isoformat()
            data['api_version'] = __version__
        return data
    return wrapper


class Policy:

    model = {
        'POST': {'authorize':False, 'fields':None},
        'PUT': {'authorize':False, 'fields':None},
        'DELETE': {'authorize':False},
        'GET': {'authorize':False, 'fields':None, 'query':None, 'allowed_patterns':[], 'denied_patterns':[]}
        }

    def __init__(self):
        self.info = {}

    def set(self, tablename, method, **attributes):
        method = method.upper()
        if not method in self.model or any(key not in self.model[method] for key in attributes):
            raise InvalidFormat('Invalid policy format')
        if not tablename in self.info:
            self.info[tablename] = copy.deepcopy(self.model)
        self.info[tablename][method].update(attributes)
    
    def check_if_allowed(self, method, tablename, id=None, get_vars=None, post_vars=None):
        get_vars = get_vars or {}
        post_vars = post_vars or {}
        policy = self.info.get(tablename) or self.info.get('*')
        if not policy:
            raise PolicyViolation('No policy for this object')
        policy = policy.get(method.upper())
        if not policy: 
            raise PolicyViolation('No policy for this method')
        authorize = policy.get('authorize')
        if authorize is False or (callable(authorize) and not authorize(tablename, id, get_vars, post_vars)):
            raise PolicyViolation('Not authorized')
        for key in get_vars:
            if any(fnmatch.fnmatch(key, p) for p in policy['denied_patterns']):
                raise PolicyViolation('Pattern is not allowed')
            allowed_patterns = policy['allowed_patterns']
            if '**' not in allowed_patterns and not any(fnmatch.fnmatch(key, p) for p in allowed_patters):
                raise PolicyViolation('Pattern is not explicitely allowed')
        return


    def allowed_fieldnames(self, table, method='GET'):
        method = method.upper()
        policy = self.info.get(table._tablename) or self.info.get('*')
        policy = policy[method]
        allowed_fieldnames = policy['fields']
        if not allowed_fieldnames:
            allowed_fieldnames = [
                f.name for f in table 
                if (method == 'GET' and f.readable)
                or (method != 'GET' and f.writable)]
        return allowed_fieldnames

    def check_fieldnames(self, table, fieldnames, method='GET'):
        allowed_fieldnames = self.allowed_fieldnames(table, method)
        invalid_fieldnames = set(fieldnames) - set(allowed_fieldnames)
        if invalid_fieldnames:
            raise InvalidFormat('Invalid fields: %s' % list(invalid_fieldnames))


DENY_ALL_POLICY = Policy()
ALLOW_ALL_POLICY = Policy()
ALLOW_ALL_POLICY.set(tablename='*', method='GET', authorize=True, allowed_patterns=['**'])
ALLOW_ALL_POLICY.set(tablename='*', method='POST', authorize=True)
ALLOW_ALL_POLICY.set(tablename='*', method='PUT', authorize=True)
ALLOW_ALL_POLICY.set(tablename='*', method='DELETE', authorize=True)


class API:

    re_table_and_fields = re.compile('\w+([\w+(,\w+)+])?')
    re_lookups = re.compile('((\w*\!?\:)?(\w+(\[\w+(,\w+)*\])?)(\.\w+(\[\w+(,\w+)*\])?)*)')
    re_no_brackets = re.compile('\[.*?\]')

    def __init__(self, db, policy):
        self.db = db
        self.policy = policy

    @error_wrapper
    def __call__(self, method, tablename, id=None, get_vars=None, post_vars=None):
        method = method.upper()
        get_vars = get_vars or {}
        post_vars = post_vars or {}
        # validate incoming request
        if not tablename in self.db.tables:
            raise InvalidFormat('Invalid table name: %s' % tablename)
        if self.policy:
            self.policy.check_if_allowed(method, tablename, id, get_vars, post_vars)
            if method in ['POST', 'PUT']:
                self.policy.check_fieldnames(self.db[tablename], post_vars.keys(), method)
        # apply rules
        if method == 'GET':
            if id:
                vars['tablename'] = id
            return self.search(tablename, get_vars)
        elif method == 'POST':
            table =  self.db[tablename]
            return table.validate_and_insert(**post_vars).as_dict()
        elif method == 'PUT':
            id = id or post_vars['id']
            if not id:
                raise InvalidFormat('No item id specified')
            table =  self.db[tablename]
            data = self.db(table.id == id).validate_and_update(**post_vars).as_dict()
            if not data.get('updated'):
                raise NotFound('Item not found')
            return data
        elif method == 'DELETE':
            id = id or post_vars['id']
            if not id:
                raise InvalidFormat('No item id specified')
            table = self.db[tablename]
            deleted = self.db(table.id == id).delete()
            if not deleted:
                raise NotFound('Item not found')
            return {'deleted': deleted}

    def table2template(self,table):
        """ converts a table into its form template """
        data = []
        fields = self.table_policy.get('fields', table.fields)
        for fieldname in fields:
            field = table[fieldname]
            info = {'name': field.name, 'value': '', 'prompt': field.label}
            policies = self.policies[table._tablename]
            # https://github.com/collection-json/extensions/blob/master/template-validation.md
            info['type'] = str(field.type) # FIX THIS                                                                                  
            if hasattr(field,'regexp_validator'):
                info['regexp'] = field.regexp_validator
            info['required'] = field.required
            info['post_writable'] = field.name in policies['POST'].get('fields',fields)
            info['put_writable'] = field.name in policies['PUT'].get('fields',fields)
            info['options'] = {} # FIX THIS                                                                                            
            data.append(info)
        return {'data':data}


    @staticmethod
    def make_query(field, condition, value):
        expression = {
            'eq': lambda: field == value,
            'ne': lambda: field == value,
            'lt': lambda: field < value,
            'gt': lambda: field > value,
            'le': lambda: field <= value,
            'ge': lambda: field >= value,            
            'startswith': lambda: field.startswith(str(value)),
            'in': lambda: field.belongs(value.split(',') if isinstance(value,str) else list(value)),
            }
        return expression[condition]()

    @staticmethod
    def parse_table_and_fields(text):
        if not API.re_table_and_fields.match(text):
            raise ValueError
        parts = text.split('[')
        if len(parts) == 1:
            return parts[0], []
        elif len(parts) == 2:
            return parts[0], parts[1][:-1].split(',')

    def search(self, tname, vars):

        def check_table_permission(tablename):
            if self.policy:
                self.policy.check_if_allowed('GET', tablename)

        def filter_fieldnames(table, fieldnames):            
            if self.policy:
                if fieldnames:
                    self.policy.check_fieldnames(table, fieldnames)
                else:
                    fieldnames = self.policy.allowed_fieldnames(table)
            elif not fielanames:
                fieldnames = table.fields
            return fieldnames

        db = self.db
        tname, tfieldnames = API.parse_table_and_fields(tname)
        check_table_permission(tname)
        tfieldnames = filter_fieldnames(db[tname], tfieldnames)
        query = []
        offset = 0
        limit = 100
        table = db[tname]
        queries = []
        hop1 = collections.defaultdict(list)
        hop2 = collections.defaultdict(list)
        hop3 = collections.defaultdict(list)
        lookup = {}
        
        for key, value in vars.items():

            if key == '$offset':
                offset = int(value)
            elif key == '$limit':
                limit = int(value)
            elif key == '$lookup':
                lookup = {item[0]: {} for item in API.re_lookups.findall(value)}
            else:
                key_parts = key.rsplit('.')
                if not key_parts[-1] in ('eq','ne','gt','lt','ge','le','startswith'):
                    key_parts.append('eq')
                is_negated = key_parts[0] == 'not'
                if is_negated:
                    key_parts = key_parts[1:]
                key, condition = key_parts[:-1], key_parts[-1]
                if len(key) == 1: # example: name.eq=='Chair'
                    query = self.make_query(table[key[0]], condition, value)
                    queries.append(query if not is_negated else ~query)
                elif len(key) == 2: # example: color.name.eq=='red'
                    hop1[is_negated, key[0]].append((key[1], condition, value))
                elif len(key) == 3: # example: a.rel.desc.eq=='above'
                    hop2[is_negated, key[0], key[1]].append((key[2], condition, value))
                elif len(key) == 4: # example: a.rel.b.name.eq == 'Table'
                    hop3[is_negated, key[0], key[1], key[2]].append((key[3], condition, value))

        for item in hop1:
            is_negated, fieldname = item
            ref_tablename = table[fieldname].type.split(' ')[1]
            ref_table = db[ref_tablename]
            subqueries = [self.make_query(ref_table[k], c, v) for k,c,v in hop1[item]]
            subquery = functools.reduce(lambda a,b: a&b, subqueries)
            query = table[fieldname].belongs(db(subquery)._select(ref_table.id))
            queries.append(query if not is_negated else ~query)

        for item in hop2:
            is_negated, linkfield, linktable = item
            ref_table = db[linktable]
            subqueries = [self.make_query(ref_table[k], c, v) for k, c, v in hop2[item]]
            subquery = functools.reduce(lambda a,b: a&b, subqueries)
            query = table.id.belongs(db(subquery)._select(ref_table[linkfield]))
            queries.append(query if not is_negated else ~query)

        for item in hop3:
            is_negated, linkfield, linktable, otherfield = item
            ref_table = db[linktable]
            ref_ref_tablename = ref_table[otherfield].type.split(' ')[1]
            ref_ref_table = db[ref_ref_tablename]
            subqueries = [self.make_query(ref_ref_table[k], c, v) for k,c,v in hop3[item]]
            subquery = functools.reduce(lambda a, b: a&b, subqueries)
            subquery &= ref_ref_table.id == ref_table[otherfield]
            query = table.id.belongs(db(subquery)._select(ref_table[linkfield], groupby=ref_table[linkfield]))
            queries.append(query if not is_negated else ~query)

        if not queries:
            queries.append(table)

        query = functools.reduce(lambda a, b: a&b, queries)        
        tfields = [table[tfieldname] for tfieldname in tfieldnames]
        rows = db(query).select(*tfields, limitby=(offset, limit + offset))

        lookup_map = {}
        for key in list(lookup.keys()):      
            name, key = key.split(':') if ':' in key else ('', key)
            clean_key = API.re_no_brackets.sub('', key)
            lookup_map[clean_key] = {'name': name.rstrip('!') or clean_key,  
                                     'collapsed': name.endswith('!')}
            key = key.split('.')

            if len(key) == 1:
                key, tfieldnames = API.parse_table_and_fields(key[0])
                ref_tablename = table[key].type.split(' ')[1]
                ref_table = db[ref_tablename]
                tfieldnames = filter_fieldnames(ref_table, tfieldnames)
                check_table_permission(ref_tablename)
                ids = [row[key] for row in rows]
                tfields = [ref_table[tfieldname] for tfieldname in tfieldnames]
                if not 'id' in tfieldnames:
                    tfields.append(ref_table['id'])
                drows = db(ref_table.id.belongs(ids)).select(*tfields).as_dict()
                if tfieldnames and not 'id' in tfieldnames:
                    for row in drows.values():
                        del row['id']
                lkey, collapsed = lookup_map[key]['name'], lookup_map[key]['collapsed']
                for row in rows:
                    new_row = drows[row[key]]
                    if collapsed:
                        del row[key]
                        for rkey in new_row:
                            row[lkey + '_' + rkey] = new_row[rkey]
                    else:
                        row[lkey] = new_row

            elif len(key) == 2:
                lfield, key = key
                key, tfieldnames = API.parse_table_and_fields(key)
                check_table_permission(key)
                ref_table = db[key]
                tfieldnames = filter_fieldnames(ref_table, tfieldnames)
                ids = [row['id'] for row in rows]
                tfields = [ref_table[tfieldname] for tfieldname in tfieldnames]
                if not lfield in tfieldnames:
                    tfields.append(ref_table[lfield])
                lrows = db(ref_table[lfield].belongs(ids)).select(*tfields)
                drows = collections.defaultdict(list)
                for row in lrows:
                    row = row.as_dict()
                    drows[row[lfield]].append(row)
                    if not lfield in tfieldnames:
                        del row[lfield]
                lkey = lookup_map[lfield + '.' + key]['name']
                for row in rows:                    
                    row[lkey] = drows.get(row.id, [])

            elif len(key) == 3:
                lfield, key, rfield = key
                key, tfieldnames = API.parse_table_and_fields(key)
                rfield, tfieldnames2 = API.parse_table_and_fields(rfield)
                check_table_permission(key)
                ref_table = db[key]
                ref_ref_tablename = ref_table[rfield].type.split(' ')[1]
                check_table_permission(ref_ref_tablename)
                ref_ref_table = db[ref_ref_tablename]
                tfieldnames = filter_fieldnames(ref_table, tfieldnames)
                tfieldnames2 = filter_fieldnames(ref_ref_table, tfieldnames2)
                ids = [row['id'] for row in rows]
                tfields = [ref_table[tfieldname] for tfieldname in tfieldnames]
                if not lfield in tfieldnames:
                    tfields.append(ref_table[lfield])
                if not rfield in tfieldnames:
                    tfields.append(ref_table[rfield])
                tfields += [ref_ref_table[tfieldname] for tfieldname in tfieldnames2]
                left = ref_ref_table.on(ref_table[rfield]==ref_ref_table['id'])
                lrows = db(ref_table[lfield].belongs(ids)).select(*tfields, left=left)
                drows = collections.defaultdict(list)
                lkey = lfield + '.' + key + '.' + rfield
                lkey, collapsed = lookup_map[lkey]['name'], lookup_map[lkey]['collapsed']
                for row in lrows:
                    row = row.as_dict()
                    new_row = row[key]
                    lfield_value, rfield_value = new_row[lfield], new_row[rfield]
                    if not lfield in tfieldnames:
                        del new_row[lfield]
                    if not rfield in tfieldnames:
                        del new_row[rfield]
                    if collapsed:
                        new_row.update(row[ref_ref_tablename])
                    else:
                        new_row[rfield] = row[ref_ref_tablename]
                    drows[lfield_value].append(new_row)
                for row in rows:                  
                    row[lkey] = drows.get(row.id, [])

        response = {}
        response['items'] = rows.as_list()
        if offset == 0:
            response['count'] = db(query).count()
        return response

import unittest            
from pydal import DAL, Field
from pydal.validators import IS_NOT_IN_DB

class TestAPI(unittest.TestCase):

    def setUp(self):
        db = DAL('sqlite:memory')

        db.define_table('color', Field('name', requires=IS_NOT_IN_DB(db, 'color.name')))
        db.color.insert(name='red')
        db.color.insert(name='green')
        db.color.insert(name='blue')

        db.define_table('thing', Field('name'), Field('color', 'reference color'))
        db.thing.insert(name='Chair', color=1)
        db.thing.insert(name='Chair', color=2)
        db.thing.insert(name='Table', color=1)
        db.thing.insert(name='Table', color=3)
        db.thing.insert(name='Lamp', color=2)
    
        db.define_table('rel', Field('a', 'reference thing'), Field('desc'), Field('b','reference thing'))
        db.rel.insert(a=1, b=2, desc='is like')
        db.rel.insert(a=3, b=4, desc='is like')
        db.rel.insert(a=1, b=3, desc='is under')
        db.rel.insert(a=2, b=4, desc='is under')
        db.rel.insert(a=5, b=4, desc='is above')

        api = API(db, ALLOW_ALL_POLICY)

        self.db = db
        self.api = api

    def test_search(self):
        api = self.api
        api.policy = ALLOW_ALL_POLICY
        self.assertEqual(api.search('color', {'name.eq': 'red'}),
           {
            'count': 1, 
            'items': [
                {'id': 1, 'name': 'red'}
                ]
            })
        self.assertEqual(api.search('thing', {'name.eq':'Chair'}), 
                         {
                'count': 2, 
                'items': [
                    {'name': 'Chair', 'color': 1, 'id': 1}, 
                    {'name': 'Chair', 'color': 2, 'id': 2}
                    ]
                })
        self.assertEqual(api.search('rel[a,b]', {'desc.eq':'is like'}),
                         {
                'count': 2, 
                'items': [
                    {'b': 2, 'a': 1}, 
                    {'b': 4, 'a': 3}
                    ]
                })
        self.assertEqual(api.search('thing[name]', {'color.name.eq':'red'}),
                         {
                'count': 2, 
                'items': [
                    {'name': 'Chair'}, 
                    {'name': 'Table'}
                    ]
                })
        self.assertEqual(api.search('thing[name]', {'not.color.name.eq':'red'}),
                         {'count': 3, 
                          'items': [
                    {'name': 'Chair'}, 
                    {'name': 'Table'},
                    {'name': 'Lamp'}
                    ]
                          })
        self.assertEqual(api.search('thing[name]', {'a.rel.desc':'is above'}),
                         {
                'count': 1, 
                'items': [
                    {'name': 'Lamp'}
                    ]
                })
        self.assertEqual(api.search('thing[name]', {'a.rel.b.name':'Table'}),
                         {
                'count': 4, 
                'items': [
                    {'name': 'Chair'}, 
                    {'name': 'Chair'}, 
                    {'name': 'Table'}, 
                    {'name': 'Lamp'}
                    ]
                })
        self.assertEqual(api.search('thing[name]', {'a.rel.b.name':'Table', 'a.rel.desc':'is above'}),
                         {
                'count': 1, 
                'items': [
                    {'name': 'Lamp'}
                    ]
                })
        self.assertEqual(api.search('thing', {'$lookup':'color'}), 
                         {
                'count': 5, 
                'items': [
                    {'name': 'Chair', 'color': {'name': 'red', 'id': 1}, 'id': 1}, 
                    {'name': 'Chair', 'color': {'name': 'green', 'id': 2}, 'id': 2}, 
                    {'name': 'Table', 'color': {'name': 'red', 'id': 1}, 'id': 3}, 
                    {'name': 'Table', 'color': {'name': 'blue', 'id': 3}, 'id': 4}, 
                    {'name': 'Lamp', 'color': {'name': 'green', 'id': 2}, 'id': 5}
                    ]
                })
        self.assertEqual(api.search('thing', {'$lookup':'color[name]'}), 
                         {
                'count': 5, 
                'items': [
                    {'name': 'Chair', 'color': {'name': 'red'}, 'id': 1}, 
                    {'name': 'Chair', 'color': {'name': 'green'}, 'id': 2}, 
                    {'name': 'Table', 'color': {'name': 'red'}, 'id': 3}, 
                    {'name': 'Table', 'color': {'name': 'blue'}, 'id': 4}, 
                    {'name': 'Lamp', 'color': {'name': 'green'}, 'id': 5}
                    ]
                })
        self.assertEqual(api.search('thing', {'$lookup':'color!:color[name]'}), 
                         {
                'count': 5, 
                'items': [
                    {'name': 'Chair', 'color_name': 'red', 'id': 1}, 
                    {'name': 'Chair', 'color_name': 'green', 'id': 2}, 
                    {'name': 'Table', 'color_name': 'red', 'id': 3}, 
                    {'name': 'Table', 'color_name': 'blue', 'id': 4}, 
                    {'name': 'Lamp', 'color_name': 'green', 'id': 5}
                    ]
                })
        self.assertEqual(api.search('thing', {'$lookup':'related:a.rel[desc]'}),
                         {
                'count': 5,
                'items': [
                    {'name': 'Chair', 
                     'related': [{'desc': 'is like'}, {'desc': 'is under'}], 
                     'color': 1, 
                     'id': 1}, 
                    {'name': 'Chair', 
                     'related': [{'desc': 'is under'}], 
                     'color': 2, 
                     'id': 2}, 
                    {'name': 'Table', 
                     'related': [{'desc': 'is like'}],
                     'color': 1,
                     'id': 3}, 
                    {'name': 'Table', 
                     'related': [], 
                     'color': 3,
                     'id': 4}, 
                    {'name': 'Lamp',
                     'related': [{'desc': 'is above'}],
                     'color': 2,
                     'id': 5}]
                }) 
        self.assertEqual(api.search('thing', {'$lookup':'related:a.rel[desc].b[name]'}),
                         {
                'count': 5, 
                'items': [
                    {'name': 'Chair',
                     'related': [{'b': {'name': 'Chair'},'desc': 'is like'}, 
                                 {'b': {'name': 'Table'}, 'desc': 'is under'}],
                     'color': 1,
                     'id': 1}, 
                    {'name': 'Chair',
                     'related': [{'b': {'name': 'Table'}, 'desc': 'is under'}],
                     'color': 2,
                     'id': 2}, 
                    {'name': 'Table',
                     'related': [{'b': {'name': 'Table'}, 'desc': 'is like'}],
                     'color': 1,
                     'id': 3},
                    {'name': 'Table',
                     'related': [],
                     'color': 3,
                     'id': 4}, 
                    {'name': 'Lamp',
                     'related': [{'b': {'name': 'Table'}, 'desc': 'is above'}],
                     'color': 2,
                     'id': 5}
                    ]
                }) 
        self.assertEqual(api.search('thing', {'$lookup':'color[name],related:a.rel[desc].b[name]', '$offset': 1, '$limit':2}),
                         {
                'items': [
                    {'name': 'Chair',
                     'related': [{'b': {'name': 'Table'}, 'desc': 'is under'}],
                     'color': {'name': 'green'},
                     'id': 2},
                    {'name': 'Table',
                     'related': [{'b': {'name': 'Table'}, 'desc': 'is like'}],
                     'color': {'name': 'red'},
                     'id': 3}
                    ]
                })
        self.assertEqual(api.search('thing', {'$lookup':'color[name],related!:a.rel[desc].b[name]', '$offset': 1, '$limit':2}),
                         {
                'items': [
                    {'name': 'Chair',
                     'related': [{'name': 'Table', 'desc': 'is under'}],
                     'color': {'name': 'green'},
                     'id': 2},
                    {'name': 'Table',
                     'related': [{'name': 'Table', 'desc': 'is like'}],
                     'color': {'name': 'red'},
                     'id': 3}
                    ]
                })
    
    def test_REST(self):
        
        api = self.api
        api.policy = ALLOW_ALL_POLICY

        response = api('GET', 'color', None, {'name.eq': 'red'})
        del response['timestamp']
        self.assertEqual(response,
                         {'count': 1, 
                          'status': 
                          'success', 
                          'code': 200, 
                          'items': [{'id': 1, 'name': 'red'}], 
                          'api_version': __version__
                          })
        response = api('POST','color', post_vars={'name':'magenta'})
        del response['timestamp']
        self.assertEqual(response,
                         {'status': 'success',
                          'errors': {},
                          'code': 200,
                          'id': 4,
                          'api_version': __version__
                          })    
        response = api('POST','color', post_vars={'name':'magenta'})
        del response['timestamp']
        self.assertEqual(response, 
                         {'status': 'error',
                          'errors': {'name': 'Value already in database or empty'},
                          'code': 422,
                          'message': 'Validation Errors',
                          'id': None,
                          'api_version': __version__
                          });
        response = api('PUT','color', 4, post_vars={'name':'Magenta'})
        del response['timestamp']
        self.assertEqual(response, 
                         {'status': 'success',
                          'updated': 1,
                          'errors': {},
                          'code': 200,
                          'api_version': '0.1'
                          })
        response = api('DELETE', 'color', 4)
        del response['timestamp']
        self.assertEqual(response, 
                         {'deleted': 1,
                          'status': 'success',
                          'code': 200,
                          'api_version': '0.1'
                          })

    def test_policies(self):
        
        api = self.api
        api.policy = DENY_ALL_POLICY    
        
        response = api('GET', 'color', None, {'name.eq': 'red'})
        del response['timestamp']
        self.assertEqual(response, 
                         {'status': 'error',
                          'message': 'No policy for this object',
                          'code': 401,
                          'api_version': __version__
                          })

if __name__ == '__main__':
    unittest.main()


