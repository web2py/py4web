import uuid

from pydal.restapi import ALLOW_ALL_POLICY, DENY_ALL_POLICY, RestAPI
from yatl.helpers import DIV, TAG, XML

from py4web import URL, action, request, response

MTABLE = '<mtable url="{url}" filter="" order="" :editable="true" :deletable="true" :create="true" :render="{render}"></mtable>'


class Publisher:

    """ this is a work in progress - API subject to change """

    def __init__(self, db, policy=None, auth=None, path="service/{uuid}/<tablename>"):
        self.db = db
        self.policy = policy
        self.restapi = RestAPI(self.db, policy)
        self.path = path.format(uuid=str(uuid.uuid4()))
        args = [db, auth] if auth else [db]
        f = action.uses(*args)(self.api)
        f = action(self.path, method=["GET", "POST"])(f)
        f = action(self.path + "/<id:int>", method=["PUT", "DELETE"])(f)

    def api(self, tablename, id=None):
        policy = self.policy
        data = self.restapi(request.method, tablename, id, request.query, request.json)
        response.status = data["code"]
        return data

    def mtable(self, table):
        path = self.path.replace("<tablename>", table._tablename)
        return XML(MTABLE.format(url=URL(path), render={}))

    def grid(self, table):
        name = "vue%s" % str(uuid.uuid4())[:8]
        return DIV(
            self.mtable(table),
            TAG.SCRIPT(_src=URL("static/js/axios.min.js")),
            TAG.SCRIPT(_src=URL("static/js/vue.min.js")),
            TAG.SCRIPT(_src=URL("static/js/utils.js")),
            TAG.SCRIPT(_src=URL("static/components/mtable.js")),
            TAG.SCRIPT(XML('var app={}; app.vue = new Vue({el:"#%s"});' % name)),
            _id=name,
        )
