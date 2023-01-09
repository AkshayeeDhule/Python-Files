

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

ch=int(input("Enter the choice like 1 as Addition, 2 as Subtraction, 3 as Multiplication, 4 as division"))

a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

if ch==1:
    z=a+b
    print("Addition is: ",z)

elif ch==2:
    z=a-b
    print("Subtraction is: ",z)

elif ch==3:
    z=a*b
    print("Multiplication is: ",z)

elif ch==4:
    z=a/b
    print("Division is: ",z)

else:
    print("Enter Valid choice!!")
    
