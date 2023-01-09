#elif (else.......if)

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))

if x>y and x>z:
    print("Greatest is: ",x)

elif y>x and y>z:
    print("Greatest is: ",y)

elif z>x and z>y:
    print("Greatest is: ",z)
    
else:
    print("In else block..")
    
