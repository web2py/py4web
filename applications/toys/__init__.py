import os, random, datetime
from web3py import action, request, DAL, Field, Session, Cache, user_in

# define database and tables
db = DAL('sqlite://storage.db', folder=os.path.join(os.path.dirname(__file__), 'databases'))

db.define_table(
    'manufacturer',
    Field('name'),
    Field('address','text'))

db.define_table(
    'toy', 
    Field('name'),
    Field('age', 'integer'),
    Field('weight','float'),
    Field('in_stock','boolean'),
    Field('last_sold','datetime'),
    Field('image', 'upload'),
    Field('description','text'),
    Field('manufacturer', 'reference manufacturer'))

db.define_table('tag', Field('name'))

db.define_table('link', Field('toy','reference toy'), Field('tag','reference tag'))

if db(db.manufacturer).count() == 0:
    for name in ['Lego', 'Hasbro', 'Mattel']:
        db.manufacturer.insert(name=name)
    for tag in ['doll','robot','large','plush']:
        db.tag.insert(name=tag)
    for k in range(100):
        id = db.toy.insert(name='toy-%i' % k,
                           age=random.randint(2,10),
                           weight=random.random()*10,
                           in_stock=random.choice((True, False)),
                           last_sold=datetime.datetime.now(),
                           description='bla bla bla',
                           manufacturer=random.randint(1,3))
        for i in range(0,3):
            db.link.insert(toy=id, tag=random.randint(1,4))
    db.commit()
