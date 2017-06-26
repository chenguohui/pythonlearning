class A(object) :
    def OnlyA(self,a):
        self.a=a
        print ("Only A :%s"%self.a)
    def CommonAB_Cover(self,ab1):
        self.ab1=ab1
        print ("CommonAB  In A : %s"%self.ab1)
    
    def CommonAB_NoCover(self,ab2):
        self.ab2=ab2
        print("CommonAB No Cover in A :%s"%self.ab2)
        
class B(A):
    def CommonAB_Cover(self,ab1):
        self.ab1=ab1+10
        print("CommonAB Cover in B:%s" %self.ab1)
    def CommonAB_NoCover(self,ab2):
        #super( ).CommonAB_NoCover(ab2)      
        super(self.__class__,self).CommonAB_NoCover(ab2) 
        print("CommonAB No Cover in B :%s"%self.ab2)
    def OnlyB(self,b):
        self.b=b
         
        print("only B :%s"%self.b)
    def FakeOnlyA(self):
        self.a=10*self.a
        print ("OnlyA  Fake inB:%s" %self.a)
        


testb=B()
 
testb.OnlyA(1)
testb.CommonAB_Cover(2)
testb.CommonAB_NoCover(3)
testb.OnlyB(4)
testb.FakeOnlyA( )
print ("********Now is A********")
testa=A()
testa.OnlyA(10)
testa.CommonAB_Cover(20)
testa.CommonAB_NoCover(30)
testa.OnlyB(40)
testa.FakeOnlyA( )



 
