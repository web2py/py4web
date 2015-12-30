import os, sys
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)
sys.path = [path] + [p for p in sys.path if not p == path]
sys.path.append('site-packages')
sys.path.append('packages/dal')

from gluon.main import main_wsgi_app, main
from gluon.anyserver import start

#main()
start(main_wsgi_app)
