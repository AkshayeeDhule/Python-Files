#greatest of three numbers entered by user.

x=int(input("enter first number."))
y=int(input("enter second number."))
z=int(input("enter third number."))

if x>y:
    if x>z:
        print("Greatest is: ",x)
    else:
        print("Greatest is: ",z)

if y>x:
    if y>z:
        print("Greatest is: ",y)

    else:
        print("Greatest is: ",z)

 '''
    Disadvantages:
    1) care need to be taken for indentation of if...else.
    2) care need to be take to match corresponding pairs of if's and else's.
    3) program creeps to the right side.
    
 '''
