# -*- coding: utf-8 -*-
#NumPy array
import time 
import numpy as np #导入NumPy模块
t0=time.clock() 
a=np.arange(100)
b=np.arange(100)**2
c=a+b
print c
print  time.clock()-t0
