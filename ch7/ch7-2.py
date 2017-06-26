import datetime 
class A(object) : 
    def __new__(cls,*args,**kwargs):
        print("in new")
        instance  =object.__new__(cls,*args,**kwargs)
        instance.__dict__['create']=datetime.datetime.now()
        print ("end new") 
        return instance 
    def __init__(self,a,b): 
        print ("in init" )
        self.a,self.b=a,b

a=A(1,2) 
print ("output  a.__dict__") 
print a.__dict__

