def index():
    return 'hello world'

def vars():
    return 'request.vars='+str(request.vars)

def template():
    return dict(a=1, b=2)
