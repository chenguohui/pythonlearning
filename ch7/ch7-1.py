class A(object):
    def __new__(cls,*args,**kwargs) : 
        print cls 
        print args  
        print kwargs 
    def __init__(self, a,b) : 
        print "in init" 
        print self 
        self.a,self.b=a,b

a=A(1,2) 
 
