#cir21.py
from cir11 import a 
print ( "in module b.py") 
def b():
    print ("hello b") 
def c():
    #from  cir11 import a 
    a()
c() 

