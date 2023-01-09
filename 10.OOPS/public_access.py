'''
Four pillars of Object Oriented Programming system
==================================================
1)Abstraction
2)Encapsulation
3)Inheritance
4)Polymorphism
Need of Encapsulation
=====================
Security

medicine capsule:
================
Capsule cover protect the medicine ingredients that are
inside capsule.


Data members and Methods are enclosed withing class wrapper.
Class indirectly provide security to the data member and
Methods[Functions] inside class.
The process of Wrapping data in a single unit class is called as
encapsulation.

class is wrapping data members and Methods in a single unit.


Access specfier
===============
1)public
2)private

By Default all data members and methods has public access.
The data members with public access specifier can be access
inside class as well as outside class.
'''

class student:
    def getdata(self):
        self.name=input("Enter Name ")
        self.rno=input("Enter Roll No. ")
        self.display() #display(self)=>display(s2)

    def display(self): #self=s1|self=s2
        print("Student name:",self.name)
        print("Roll Number:",self.rno)

#s1=student() #object is created

#Accessing name and rno outside class
#s1.name="Itvedant"
#s1.rno=56

#s1.display() #display(s1)

s2=student()
s2.getdata() #getdata(s2)
