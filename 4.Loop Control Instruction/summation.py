'''
Summation of 1 to n
n=5
   1 + 2 + 3 + 4 + 5
   ----
    3    + 3
    --------
        6    + 4
        --------
          10    +   5
          -----------
             15

 
     sum=0

     1  sum=sum+1  => 0+1=1  1st iteration
     3  sum=sum+2  => 1+2=3  2nd iteration
     6  sum=sum+3  => 3+3=6  3rd iteration
     10 sum=sum+4  => 6+4=10 4th iteration
     15 sum=sum+5 => 10+5=15 5th iteration


'''

#n=int(input("Enter last number in series"))
i=1
while i<=5:
    sum=sum+i
    i=i+1
    print("Summation is :",sum)
    
