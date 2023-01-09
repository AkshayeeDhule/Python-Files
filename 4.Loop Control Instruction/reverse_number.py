
'''
write a program to reverse any digit number

n=675
o/p=> 576


step1:get the digit separated
step2: print the digit

repeat step1 and step2 till n become 0

'''
n=int(input('Enter a number'))

while n>0:
    
    x=n%10
    print(x,end=" ")
    n=n//10

    
'''
n=456

n    n>0     x=n%10        print(x)       n=n//10
456 456>0 T  x=456%10=6     6             n=456//10=45
45  45>0  T  x=45%10=5      5             n=45//10=4
4   4>0   T  x=4%10=4       4             n=4//10=0
0   0>0 F

'''
