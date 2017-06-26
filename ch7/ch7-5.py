class  Vehicle(object):
    def __init__(self, speed):
        self.speed=speed 
    
    def start(self) : 
        raise   TypeError('abstract method must be overridden')
    def run(self) :
        raise TypeError("abstract method must be overridden")
    def stop(self) :
        raise TypeError("abstact method must be overridden")
    def testVehicle(self) : 
        self.start() 
        self.run() 
        self.stop() 
class Car(Vehicle) : 
    def __init__(self,speed): 
        super(self.__class__,self).__init__(speed) 
    def start(self ):
        print ( "in car   start") 
    def run (self) : 
        print ( "car speed is %s"%(self.speed) ) 
    def stop(self) : 
        print ("car stop" ) 
class  Truck (Vehicle) :

    def __init__(self,speed): 
        super(self.__class__,self).__init__(speed) 
    def start(self ):
        print ( "in Truck   start") 
    def run (self) : 
        print ( "Truck speed is %s"%(self.speed) ) 
    def stop(self) : 
        print ("Truck stop" ) 



## 调用 
Vehicletest1=Car(100) 
Vehicletest2=Truck(90) 
Vehicletest1.testVehicle()
print ("*****************")
Vehicletest2.testVehicle() 

