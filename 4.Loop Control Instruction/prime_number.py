'''

prime number
============

A numebr which is completely divisible by 1 and itself is called as prime number

7 is prime number=> 7 is completely divisible by 1 and 7

8 is also completly divisible by 1 and 8, but 8 is non prime number.

n=7

   1     2 3 4 5 6    7
         ---------
  excluding 1 and 7 check whether any number completly divides 7, so none of in between numbers completly divides 7, thus
  it is prime number.

n=9

   1    2 3 4 5 6 7 8   9
        -------------

  Excluding
'''
'''
n=6

i   i in [2,3,4,5]   r=6%i     r==0   print("Non-prime")    i=i+1
2   2 in[]T          r=6%2     0==0T  Non-prime             i=3
3   3 in[]T          r=6%3     0==0T  Non-prime             i=4
4   4 in[]T          r=6%4=2   2==0F   -----                i=5
5   5 in[]T          r=6%5=1   1==0F   -----                i=6
6   6 in[]F


'''

'''
n=int(input("Enter number"))

for i in range(2,n,1):
    r=n%i
    if r==0:
            print("Non-Prime Number")
'''


'''
for prime and non-prime number

n=5

i   i in[2,3,4]  r=5%i   r==0   i=i+1
2   2 in[]T      r=5%2=1 1==0F  i=2+1=3
3   3 in[]T      r=5%3=2 2==0F  i=3+1=4
4   4 in[]T      r=5%4=1 1==0F  i=4+1=5
5   5 in[]F => Completed all iterations

n=7
i   i in[2,3,4,5,6]  r=7%i   r==0   i=i+1
2   2 in[]T          r=7%2=1 1==0F  i=2+1=3
3   3 in[]T          r=7%3=2 2==0F  i=3+1=4
4   4 in[]T          r=7%4=3 3==0F  i=4+1=5
5   5 in[]T          r=7%5=2 2==0F  i=5+1=6
6   6 in[]T          r=7%6=1 1==0F  i=6+1=7
7   7 in[]F     ===> Compl
'''

n=int(input(' Enter Number '))

for i in range(2,n,1):
    r=n%i #r=9%2,r=9%3=0
    
    if r == 0:
            print(n,'Non-Prime Number')
            break
else:
            print('It is prime number')
