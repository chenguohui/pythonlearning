from abc import ABCMeta,abstractmethod
class Shape(object):#(metaclass=ABCMeta):
    __metaclass__=ABCMeta
    def area(self): 
        pass
class  Circle(Shape):
    def __init__(self, radius) : 
        self.radius=radius
    def area(self):
        return   3.14*self.radius*self.radius

class Rectangle(Shape) : 
    def __init__(self,a,b) : 
        self.a=a
        self.b=b 
    def area(self): 
        return  self.a*self.b

def  PrintArea(obj):
    print (obj.area() ) 
mytest1=Circle(2)
mytest2=Rectangle(2,3)
PrintArea(mytest1)
PrintArea(mytest2) 

        
