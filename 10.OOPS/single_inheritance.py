'''
Single Inheritance:
==================
The inheritance in which there is only one base class and
one derived class is called as Single inheritance.

                         A base class
                         |
                         |
                         |
                         B Derived class
                         
In class A

method     =>geta()
data member=>a

class B
method      => getb()
data member => b
'''

class A:

    def geta(self): #self=b1

        self.a=int(input("Enter value of a: ")) #b1.a=20

class B(A):

    def getb(self): #self=b1
        self.b=int(input("Enter value of b: ")) #b1.b=40

    def addition(self):

        res=self.a+self.b  #res=b1.a+ba.20+40=60
        print("Addition is: ",res)


b1=B() #derived class object
b1.geta() #geta(b1)
b1.getb() #getb(b1)
b1.addition() #addition(b1)
        
        
