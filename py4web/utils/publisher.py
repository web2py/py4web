import uuid
from py4web import action, request, URL
from pydal.restapi import RestAPI, ALLOW_ALL_POLICY, DENY_ALL_POLICY        
from yatl.helpers import DIV, XML, TAG

MTABLE = '<mtable url="{url}" filter="" order="" :editable="true" :deletable="true" :render="{render}"></mtable>'

class Publisher():

    """ this is a work in progress - API subject to change """

    def __init__(self, db, policy=None, path='service/{uuid}/<tablename>'):
        self.db = db
        self.policy = policy
        self.path = path.format(uuid=str(uuid.uuid4()))
        methods = ['GET', 'POST', 'PUT', 'DELETE']
        action(self.path)(action.uses(db)(self.api))

    def api(self, tablename):
        policy = self.policy
        data = RestAPI(self.db, policy)(request.method, tablename, None, request.query, request.json)
        return data
    
    def mtable(self, table):
        path = self.path.replace('<tablename>', table._tablename)
        return XML(MTABLE.format(url=URL(path), render={}))

    def grid(self, table):
        name = 'vue%s' % str(uuid.uuid4())[:8]
        return DIV(
            self.mtable(table),
            TAG.SCRIPT(_src=URL('static/js/axios.min.js')),
            TAG.SCRIPT(_src=URL('static/js/vue.min.js')),
            TAG.SCRIPT(_src=URL('static/js/utils.js')),
            TAG.SCRIPT(_src=URL('static/components/mtable.js')),
            TAG.SCRIPT(XML('var app=utils.app("%s"); app.start()' % name)),
            _id=name)
