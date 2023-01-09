'''
Default argument
================

   Number of argument or        Number of variable used to 
   values or variable passed =  receive.
'''

def addition(x,y=0):

    z=x+y
    print("Addition is : ",z)

    

#addition(10)error as y value is not passed

addition(10,20) #passing both value
addition(10)
