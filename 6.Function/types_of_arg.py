# Types of arguments
#1) default argument
'''
def addition(a,b):
    c=a+b
    print("addition is",c)

addition(100) #TypeError: addition() missing 1 required positional argument: 'b'
'''
'''
def addition(a,b=0):
    c=a+b
    print("Addition is ",c)

addition(100)
'''
def addition(a=0,b=0):
     c=a+b
     print("Addition is ",c)

addition()
    

#2) keyword argument: key and value

def addition(a,b=0):
    c=a+b
    print("Addition is ",c)

addition(a=20,b=30)    

