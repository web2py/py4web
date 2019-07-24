from py4web import action, redirect, URL

@action('index')
def index():
    redirect(URL('static/index.html'))
