import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

sys.path.append('site-packages')
sys.path.append('packages/dal')

from gluon.main import main


main()

#import profile
#profile.run('main(); print')
