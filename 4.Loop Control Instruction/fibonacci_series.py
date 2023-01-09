#Fibonacci series

'''

 0   1   1     2   3   5   8   13   21......
 i   j   sum
         =0+1
         =1
 
     i   j
     1   1
 
'''

n=int(input('Enter a number'))
i=0
j=1
print(i,end=" ")
print(j,end=" ")
k=1
while k<=n-2:
    sum=i+j
    print(sum,end=" ")
    i=j
    j=sum
    k=k+1

'''
i=0
j=0

sum=i+j=0+1=1   sum=i+j=1+1=2  sum=i+j=1+2=3  sum=i+j=2+3=5
print(sum) 1    print(sum)2    print(sum)3    print(sum)5
i=j             i=j (1)        i=j (2)        
j=sum(1)        j=sum(2)       j=sum(3)

Note:
0 and 1 need to be printed without loop.
Two starting terms of the fibonacci series must be printed without loop.




'''
