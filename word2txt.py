
#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import glob, re, os
f = glob.glob('*.doc') + glob.glob('*.DOC')

outDir = 'txts'
if not os.path.exists(outDir):
    os.makedirs(outDir)
for i in f:
    os.system("catdoc -w '%s' > '%s'" %
              (i, outDir + '/' + re.sub(r'.*/([^.]+)\.doc', r'\1.txt', i,
                                   flags=re.IGNORECASE)))
                                   