# -*- coding: utf-8 -*-
#Python list
import time 
t0 = time.clock()
a=range(100)
b=[]
c=[]
for i in range(100):
    b.append(a[i]**2)
    c.append(a[i]+b[i])
print c
print  time.clock()-t0 
