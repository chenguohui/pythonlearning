

from abc import ABCMeta,abstractproperty,abstractmethod
class A(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def Printitem(self):
        pass
    
    def get_item(self): 
        pass
    def set_item(self, value): 
        pass
    item = abstractproperty(get_item, set_item, doc="设置或返回item")
 
class B(A):
    def __init__(self):
        self._item=0
    def Printitem(self):
        print self._item
   
    def get_item(self): 
        return self._item
   
    def set_item(self, value): 
        self._item=value
       
    item = property(get_item, set_item,doc="设置或返回item")
 

test1=B()
test1.item=10
print(test1.item)
test1.Printitem() 
