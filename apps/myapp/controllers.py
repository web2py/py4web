from py4web import action, request, redirect, abort
from . models import db

@action('helloworld') # exposes http://127.0.0.1:8000/myapp/helloworld
@action.uses(db, 'helloworld.html')
def helloworld(): return dict(name=request.forms.get('name', 'visitor'))
