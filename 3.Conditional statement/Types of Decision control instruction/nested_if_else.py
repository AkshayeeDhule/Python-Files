'''
3) nested if...else

syntax:
if condition1:
    if condition2:
        body of if
    else:
        body of else
else:
    if condition3:
        body of if
    else:
        body of else

'''

x=int(input("enter first number: "))
y=int(input("enter second number: "))

if x==y:
    print("Both are equal.")

else:
    if x>y:
        print("greatest is :", x)

    else:
        print("greatest is :",y)
    
