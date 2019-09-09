import uuid
from py4web import action, request, URL
from pydal.restapi import RestAPI, ALLOW_ALL_POLICY, DENY_ALL_POLICY        

MTABLE = '<mtable url="{url}" filter="" order="" :editable="false" :deletable="true" :render="{render}"></mtable>'

class Grid():

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
    
    def xml(self):
        return MTABLE.format(url=URL(self.path), render={})
