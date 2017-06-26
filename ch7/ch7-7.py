
#-*- coding:utf-8  -*-
class Person(object):
    def __init__(self, id):
        self.id = id
       
        #'''只是访问未定义的属性,即__dict__中不包含的。 '''
    def __getattr__(self,myattr ):
        print  (u"__dict__中无%s属性,不过__getattr__可以假装它有"%myattr)
        if myattr == 'name':
            self.name="default"
            print (u"添加了个name属性")
            return  self.name
        else :
            print  (u"但确实无%s属性"%myattr)
            return None
         
   
    def  __setattr__(self,attr,value) : 
        print (u" 通过__setattr__给%s属性赋值：%s"%(attr,value)) 
        self.__dict__[attr]=value

    def __delattr__(self,attr) :
        object.__delattr__(self,attr)   
      

mytest=Person(10) 
print (mytest.id) 
print (mytest.__dict__)
print (mytest.age )
print (mytest.name)
print (mytest.__dict__)#添加了name属性，但没有添加age属性
mytest.age=30
mytest.name="test"
print (mytest.__dict__)


  
class  Proxy(object) : 
    def __init__(self,subject) : 
        self._subject=subject
    
    def __getattr__(self,attr) :
        return   getattr(self._subject,  attr) 
myproxy=Proxy(mytest) 
print (myproxy.age )

