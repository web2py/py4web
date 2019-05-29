import datetime
import functools
from pydal import Field, Field
from pydal.validators import *

class Tags(object):

    def __init__(self, table, name='default'):
        self.table = table
        db = table._db
        self.tag_table = db.define_table(
            table._tablename + '_tag_' + name,
            Field('path'),
            Field('record_id', table))

    def __getitem__(self, record_id):
        tag_table = self.tag_table
        db = tag_table._db
        rows = db(tag_table.record_id==record_id).select(tag_table.path)
        return [row.path.strip('/') for row in rows]

    def __setitem__(self, record_id, tags):
        tag_table = self.tag_table
        db = tag_table._db
        if not isinstance(tags, list):
            tags = [tags]
        for tag in tags:
            tag = tag.strip('/')
            if not db(tag_table.record_id==record_id)(tag_table.path==tag).count():
                tag_table.insert(record_id=record_id, path='/%s/' % tag)

    def __call__(self, tags, mode='and'):
        table = self.table
        tag_table = self.tag_table
        db = tag_table._db
        queries = []        
        if not isinstance(tags, list):
            tags = [tags]
        for tag in tags:
            tag = tag.strip('/')
            subquery = db(tag_table.path.startswith('/%s/' % tag))._select(tag_table.record_id)
            queries.append(table.id.belongs(subquery))
        func = lambda a,b: (a & b) if mode == 'and' else (a | b)
        return functools.reduce(func, queries)
