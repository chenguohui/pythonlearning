#cir2.py
from  cir1 import a 
def b():
    print ('a() has run in cir2')
def c():
    print ("c() in cir2") 
    #from  cir1 import a 
    a()
c()
