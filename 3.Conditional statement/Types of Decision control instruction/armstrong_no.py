#A three digit number is entered by user.WAP to check whether that number
# is a armstong number or not.

'''
Armstrong number:

153= 1*1*1 =>  1
     5*5*5 =>125
     3*3*3 => 27

           => 153
'''

n=int(input("Enter a number: ")) #n=153
a=n%10 #a=153%10= 3
b=n//10 #b= 153//10= 15
c=b%10 # c= 15%10 => 5
d=b//10 #d= 15//10 =>1
sum=a*a*a+c*c*c+d*d*d
if sum==n:
    print("It is a armstrong number.")

else:
    print("It is not a armstrong number.")


