#!/usr/bin/evn python

import os.path

for path in [ '/one/two/three','/one/two/three/','/',',']:
    print '"%s" : "%s"' % (path,os.path.dirname(path))
