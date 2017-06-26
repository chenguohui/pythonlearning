class C(object):
    pass 
c=C() 
print (c.__dict__)
c.age =10 
print (c.__dict__ ,c.age)
 
def print_attribute(obj):
    for attr in obj.__dict__:
        print (attr,  getattr(obj,attr)) 


print_attribute(c) 

