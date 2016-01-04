def index():
    from gluon.form import Form
    session.enable()
    session.counter = (session.counter or 0)+1
    form = Form([Field('name'),Field('image','upload')], csrf=False)
    return dict(form=form)

def simple():
    return 'hello world'

def vars():
    return 'request.vars=%s' % BEAUTIFY(request.vars)

def error():
    1/0

def user(): 
    return auth()
