#any digit number is entered by user WAP to find sum of digits.

'''
n=4532

sum=0

n=4532         n=453        n=45        n=4

x=4532%10=2   x=453%10=3  x=45%10=5   x=4%10=4
sum=sum+x     sum=sum+x  sum=sum+x    sum=sum+x
    =0+2         =2+3        =5+5         =10+4
    =2           =5          =10          =14
n=n//10       n=n//10    n=n//10       n=n//10
 =4532//10     =453//10   =45//10       =4//10
 =453          =45         =4           =0 =>stop


 In modulus when divident is less than divisor then division occurs in following way.


            0
        -------
     10 |   4
         -  0
         ------
            4
'''

n=int(input('Enter a number')) #initialization
s=0
while n>0: #n is used in condition
    x=n%10
    s=s+x
    n=n//10 #decrement
    print('summation is :',s)
