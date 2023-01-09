x=10
print("Data type of variable x:",type(x))
'''
class student:

    def greet(self):

        print("Good Evening")



s1=student()

print("Data type of object s1: ",type(s1))
'''

'''
Conclusion:
data type of variable is built in datatype i.e int,float

data type of object is classname.

In above program data type of object s1 is Classname => student.
'''

'''        
x is variable of built in data type.
s1 object is variable of user defined datatype.

x=10

In a single line, x variable defined[memory allocate] and it is initialize to value 10.

                     10
                -------------
               |             |
               |             |
                -------------
                      x

If there is a need to initialize object at its creation, then there is need of constructor.

1] Consrtuctor is a special method of function which is used
    to initialize object at the time of its creation.

2] It has fixed name as __init__().

3] Constructor is always called automatically when object of the class is created.
'''

class customer:

    def __init__(self):

        print("Constructor is called !")

   

c1=customer()   #object created => Constructor is called
c2=customer()   #object created => Constructor is called


                      
