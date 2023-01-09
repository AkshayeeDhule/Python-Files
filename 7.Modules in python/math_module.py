'''

built in modules
================

                         modules
                            |
                --------------------------
               |            |             |
             Functions    Constants    Classes

In order to use math module in the python file. Then
there is s need to import that module

step1: import module
step2: use that module

'''

#import math
#factorial

'''

r=math.factorial(4)
print("Factorial of number is ", r)

'''

#Alising module => giving different name

import math as m

#ceil() and floor()

'''
  15.7=> 15 to 16 => 16
   15.5=> 15 to 16 => 16
    15.3=> 15 to 16 => 16
  
'''

print(m.ceil(15.8))
print(m.ceil(15.5))
print(m.ceil(15.3))

'''

   15.7=> 15 to 16 => 15
   15.5=> 15 to 16 => 15
    15.3=> 15 to 16 => 15
  
 
'''
print(m.floor(15.8))
print(m.floor(15.5))
print(m.floor(15.3))



# import specific functionality from module

from math import factorial,sqrt

r=factorial(7)
print("Factorial is : ",r)

sroot=sqrt(25)
print("Square root is : ",sroot)

#importing everything from module

from math import*

print(ceil(15.3))
print(floor(15.7))
print(factorial(4))
print(sqrt(16))

import math as m

print("value of PI is:",m.pi)
print("value of tau is:",m.tau)
