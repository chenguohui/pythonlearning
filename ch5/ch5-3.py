# -*- coding: utf-8 -*-
import sys
import StringIO as sio
f=sio.StringIO()
stdout=sys.stdout
sys.stdout=f
print 'matlab'
print 'C++'
print 'Computer'
print 'Java'
strf=f.getvalue().replace('Computer','Python')
sys.stdout=stdout
print u'原始输出'
print f.getvalue()
print u'更替后输出'
print strf
f.close()



