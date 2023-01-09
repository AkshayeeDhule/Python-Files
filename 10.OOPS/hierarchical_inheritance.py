'''
Hirarchical Inheritance
======================
The inheritance in which there is one base class and many derived
classes is called as Hirarchical Inheritance.

                                B
                                |
                    -------------------------------
                   |      |     |      |           |
                   D1    D2     D3     D4 .........Dn


e.g                        A
                           |
                     --------------
|              |
                    B              C
'''

class A:
    def geta(self): #self=b1 |self=c1
        self.a=int(input("Enter value of a: ")) #b1.a=30 |c1.a=60

class B(A):
    
    def getb(self): #self=b1
        self.b=int(input("Enter value of b: ")) #b1.b=50
    def addition(self): #self=b1
        r1=self.a+self.b  #r1=b1.a+b1.b= 30+50= 80
        print("Addition of A and B is: ",r1)
        
class C(A):
    
    def getc(self): #self=c1
        self.c=int(input("Enter value of b: ")) #c1.c=70
    def addition(self): #self=c1
        r2=self.a+self.c  #r2=c1.a+c1.c= 60+70=130
        print("Addition of A and C is: ",r2)

b1=B() #derived class object B
b1.geta() #geta(b1)
b1.getb()#getb(b1)
b1.addition() #addition()
print()
c1=C()  #derived class object C
c1.geta() #geta(c1)
c1.getc() #getc(c1)
c1.addition()  #addition()
        
        
