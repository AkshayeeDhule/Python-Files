'''
Calculator: Console based Application
=========
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit

Enter your Choice:2

'''


while True:
    print()
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print()
    ch=int(input("Enter Your Choice: ")) #1,2,3,4,5 or other than 1-5

    if ch==1:
        x=int(input("Enter First Number: "))
        y=int(input("Enter Second Number: "))
        z=x+y
        print("Addition is:",z)

    elif ch==2:
        x=int(input("Enter First Number: "))
        y=int(input("Enter Second Number: "))
        z=x-y
        print("Subtraction is:",z)

    elif ch==3:
        x=int(input("Enter First Number: "))
        y=int(input("Enter Second Number: "))
        z=x*y
        print("Multiplication is:",z)


    elif ch==4:
        x=int(input("Enter First Number: "))
        y=int(input("Enter Second Number: "))
        z=x/y
        print("Division is:",z)

    elif ch==5:
        print("Exit from Program,Thank you for using the service.")
        break

    else:
        print("Enter Valid Choice between 1 to 5 !!!")
