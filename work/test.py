import collections
import functools
import re

## todo: return status and errors
## add validation
## check policies


class API:

    re_table_and_fields = re.compile('\w+([\w+(,\w+)+])?')
    re_lookups = re.compile('((\w+\!?\:)?(\w+(\[\w+(,\w+)*\])?)(\.\w+(\[\w+(,\w+)*\])?)*)')
    re_no_brackets = re.compile('\[.*?\]')

    def __init__(self, db):
        self.db = db

    def __call__(self, method, tname, id, get_vars, post_vars):
        assert tname in self.db.tables
        if method == 'GET':
            if id:
                vars['tname'] = id
            return self.search(tname, get_vars) # FIX ME
        elif method == 'POST':
            return self.db[tname].validate_and_insert(**post_vars) # FIX ME
        elif method == 'PUT':
            id = id or post_vars['id']
            return self.db[tname].validate_and_update(id, **post_vars) # FIX ME
        elif method == 'DELETE':
            id = id or post_vars['id']
            table = self.db[tname]
            return self.db(table.id == id).delete() # FIX ME

    @staticmethod
    def make_query(field, condition, value):
        expression = {
            'eq': lambda: field == value,
            'ne': lambda: field == value,
            'lt': lambda: field < value,
            'gt': lambda: field > value,
            'le': lambda: field <= value,
            'ge': lambda: field >= value,
            'startswith': lambda: field.startswith(value)
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

        db = self.db
        tname, tfieldnames = API.parse_table_and_fields(tname)
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
                key, condition = key_parts[:-1], key_parts[-1]
                if len(key) == 1: # example: name.eq=='Chair'
                    queries.append(self.make_query(table[key[0]], condition, value))
                elif len(key) == 2: # example: color.name.eq=='red'
                    hop1[key[0]].append((key[1], condition, value))
                elif len(key) == 3: # example: a.rel.desc.eq=='above'
                    hop2[key[0], key[1]].append((key[2], condition, value))
                elif len(key) == 4: # example: a.rel.b.name.eq == 'Table'
                    hop3[key[0], key[1], key[2]].append((key[3], condition, value))

        for fieldname in hop1:
            ref_table = db[table[fieldname].type.split(' ')[1]]
            subqueries = [self.make_query(ref_table[k], c, v) for k,c,v in hop1[fieldname]]
            subquery = functools.reduce(lambda a,b: a&b, subqueries)
            queries.append(table[fieldname].belongs(db(subquery)._select(ref_table.id)))

        for linkfield, linktable in hop2:
            ref_table = db[linktable]
            subqueries = [self.make_query(ref_table[k], c, v) for k, c, v in hop2[linkfield, linktable]]
            subquery = functools.reduce(lambda a,b: a&b, subqueries)
            queries.append(table.id.belongs(db(subquery)._select(ref_table[linkfield])))

        for linkfield, linktable, otherfield in hop3:
            ref_table = db[linktable]
            ref_ref_table = db[ref_table[otherfield].type.split(' ')[1]]
            subqueries = [self.make_query(ref_ref_table[k], c, v) for k,c,v in hop3[linkfield, linktable, otherfield]]
            subquery = functools.reduce(lambda a, b: a&b, subqueries)
            subquery &= ref_ref_table.id == ref_table[otherfield]
            queries.append(table.id.belongs(db(subquery)._select(ref_table[linkfield], groupby=ref_table[linkfield])))

        if not queries:
            queries.append(table)

        query = functools.reduce(lambda a, b: a&b, queries)
        tfields = [table[tfieldname] for tfieldname in tfieldnames or table.fields] 
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
                ref_table = db[table[key].type.split(' ')[1]]
                ids = [row[key] for row in rows]
                tfields = [ref_table[tfieldname] for tfieldname in tfieldnames or ref_table.fields]
                if not 'id' in tfieldnames:
                    tfields.append(ref_table['id'])
                drows = db(ref_table.id.belongs(ids)).select(*tfields).as_dict()
                if not 'id'in tfieldnames:
                    for row in drows.values():
                        del row['id']
                lkey, collapsed = lookup_map[key]['name'], lookup_map[key]['collapsed']
                for row in rows:      
                    if collapsed:
                        row[lkey].update(drows[row[key]])
                    else:
                        row[lkey] = drows[row[key]]

            elif len(key) == 2:
                lfield, key = key
                key, tfieldnames = API.parse_table_and_fields(key)
                print(lookup_map, key, tfieldnames)
                ref_table = db[key]
                ids = [row['id'] for row in rows]
                tfields = [ref_table[tfieldname] for tfieldname in tfieldnames or ref_table.fields]
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
                ref_table = db[key]
                ref_ref_tablename = ref_table[rfield].type.split(' ')[1]
                ref_ref_table = db[ref_ref_tablename]
                ids = [row['id'] for row in rows]
                tfields = [ref_table[tfieldname] for tfieldname in tfieldnames or ref_table.fields]
                if not lfield in tfieldnames:
                    tfields.append(ref_table[lfield])
                if not rfield in tfieldnames:
                    tfields.append(ref_table[rfield])
                tfields += [ref_ref_table[tfieldname] for tfieldname in tfieldnames2 or ref_ref_table.fields]
                left = ref_ref_table.on(ref_table[rfield]==ref_ref_table['id'])
                lrows = db(ref_table[lfield].belongs(ids)).select(*tfields, left=left)
                drows = collections.defaultdict(list)
                lkey = lfield + '.' + key + '.' + rfield
                lkey, collapsed = lookup_map[key]['name'], lookup_map[key]['collapsed']
                for row in lrows:
                    row = row.as_dict()
                    new_row = row[key]
                    lfield_value = new_row[lfield]
                    if not lfield in tfieldnames:
                        del new_row[lfield]
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
            
def test():
    from pydal import DAL, Field
    
    db = DAL('sqlite:memory')
    db.define_table('color', Field('name'))
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

    api = API(db)

    assert (api.search('color', {'name.eq': 'red'}) ==
           {
            'count': 1, 
            'items': [
                {'id': 1, 'name': 'red'}
                ]
            })
    assert (api.search('thing', {'name.eq':'Chair'}) == 
           {
            'count': 2, 
            'items': [
                {'name': 'Chair', 'color': 1, 'id': 1}, 
                {'name': 'Chair', 'color': 2, 'id': 2}
                ]
            })
    assert (api.search('rel[a,b]', {'desc.eq':'is like'}) ==
            {
            'count': 2, 
            'items': [
                {'b': 2, 'a': 1}, 
                {'b': 4, 'a': 3}
                ]
            })
    assert (api.search('thing[name]', {'color.name.eq':'red'}) ==
            {
            'count': 2, 
            'items': [
                {'name': 'Chair'}, 
                {'name': 'Table'}
                ]
            })
    assert (api.search('thing[name]', {'a.rel.desc':'is above'}) ==
            {
            'count': 1, 
            'items': [
                {'name': 'Lamp'}
                ]
            })
    assert (api.search('thing[name]', {'a.rel.b.name':'Table'}) ==
            {
            'count': 4, 
            'items': [
                {'name': 'Chair'}, 
                {'name': 'Chair'}, 
                {'name': 'Table'}, 
                {'name': 'Lamp'}
                ]
            })
    assert (api.search('thing[name]', {'a.rel.b.name':'Table', 'a.rel.desc':'is above'}) ==
            {
            'count': 1, 
            'items': [
                {'name': 'Lamp'}
                ]
            })
    assert (api.search('thing', {'$lookup':'color'}) == 
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
    assert (api.search('thing', {'$lookup':'color[name]'}) ==
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
    assert (api.search('thing', {'$lookup':'related:a.rel[desc]'}) ==
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
    assert (api.search('thing', {'$lookup':'related:a.rel[desc].b[name]'}) ==
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
    assert (api.search('thing', {'$lookup':'color[name],related:a.rel[desc].b[name]', '$offset': 1, '$limit':2}) ==
            {
            # 'count': 5, 
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
test()
