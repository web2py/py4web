#!/usr/bin/env python3

## BEGIN TEMP LOGIC ##
import sys, os
for filename in os.listdir('site-packages'):
    sys.path.insert(0, os.path.join('site-packages', filename))
## END TEMP LOGIC ##

from web3py.core import main

if __name__ == '__main__':
    main()
