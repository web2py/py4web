import unittest
from pydal import DAL, Field
from web3py.utils.tags import Tags


class TestTags(unittest.TestCase):

    def test_tags(self):
        db = DAL('sqlite:memory')
        db.define_table('thing', Field('name'))
        properties = Tags(db.thing)
        id1 = db.thing.insert(name='chair')
        id2 = db.thing.insert(name='table')
        properties[id1] = ['color/red','style/modern']
        properties[id2] = ['color/gree','material/wood']

        self.assertTrue(properties[id1], ['color/red','style/modern'])
        self.assertTrue(properties[id2], ['color/gree','material/wood'])

        rows = db(properties(['style/modern'])).select()
        self.assertTrue(rows.first().id, id1)

        rows = db(properties(['material/wood'])).select()
        self.assertTrue(rows.first().id, id1)

        rows = db(properties(['color'])).select()
        self.assertTrue(len(rows), 2)
