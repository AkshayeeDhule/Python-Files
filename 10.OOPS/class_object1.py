class student:
    def getdata(self): #self=s1, self=s2
        self.name=input("Enter student name: ")#s1.name,s2.name
        self.rno=input("Enter roll number: ") #s1.rno, s2.rno


    def display(self): #self=s1,s2
        print("Student name:",self.name)
        print("Student roll number:",self.rno)

s1=student() #object created

s1.getdata() #gerdata(s1)
s1.display() #display(s1)

s2=student()
s2.getdata() #gerdata(s1)
s2.display() #display(s1)

'''

             self=s1

         --------------
         |             |
         name          rno
         itvedant       35
'''
