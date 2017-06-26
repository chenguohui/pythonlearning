class wolf(object): 
    def bark(self):
        print "hooooowll"

class dog(object): 
    def bark(self):
        print "woof"


def barkforme(dogtype):
    dogtype.bark()


my_dog = dog()
my_wolf = wolf()
barkforme(my_dog)
barkforme(my_wolf)

