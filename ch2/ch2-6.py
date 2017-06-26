# -*- coding: utf-8 -*-
import numpy
st=numpy.dtype([('code',str,10),('name',unicode,20),('price',float)])
a=numpy.array([('000001',u'平安',15),('000002',u'万科',13.6)],dtype=st)
msg = repr(a).decode('unicode-escape')
print msg
