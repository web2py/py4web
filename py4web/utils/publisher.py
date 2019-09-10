import uuid
from py4web import action, request, URL
from pydal.restapi import RestAPI, ALLOW_ALL_POLICY, DENY_ALL_POLICY        
from yatl.helpers import DIV, XML, TAG

MTABLE = '<mtable url="{url}" filter="" order="" :editable="true" :deletable="true" :render="{render}"></mtable>'

class Publisher():

    """ this is a work in progress - API subject to change """

    def __init__(self,
                 table,                 
                 policy=None,
                 path='service/{uuid}/{tablename}'):
        self.table = table
        self.policy = policy
        self.path = path.format(uuid=str(uuid.uuid4()), tablename=table._tablename)
        methods = ['GET', 'POST', 'PUT', 'DELETE']
        action(self.path)(action.uses(table._db)(self.api))

    def api(self):
        policy = self.policy
        db, tablename = self.table._db, self.table._tablename
        data = RestAPI(db, policy)(request.method, tablename, None, request.query, request.json)
        return data
    
    @property
    def mtable(self):
        return XML(MTABLE.format(url=URL(self.path), render={}))

    @property
    def grid(self):
        return DIV(
            self.mtable,
            TAG.SCRIPT(_src=URL('static/js/axios.min.js')),
            TAG.SCRIPT(_src=URL('static/js/vue.min.js')),
            TAG.SCRIPT(_src=URL('static/js/utils.js')),
            TAG.SCRIPT(_src=URL('static/components/mtable.js')),
            TAG.SCRIPT('var app=utils.app(); app.start()'),
            _id="vue")
