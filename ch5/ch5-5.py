# -*- coding: utf-8 -*-
import os
def sefile(spath,sfile):
    for sdir,sudir,file in os.walk(spath):
        if sfile in file:
            return (sfile,sdir)
    return None
spath=raw_input('please input the path:')
sfile=raw_input('please input the file name:')
f=sefile(spath,sfile)
if f:
    print('file %s is found,in %s' % (f[0],f[1]))
else:
    print('%s is not found'% sfile)

        


