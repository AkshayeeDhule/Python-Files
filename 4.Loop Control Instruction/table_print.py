'''
printing table of a number entered by user.
    i
2=2*1
4=2*2
6=2*3
8=2*4
10=2*5
12=2*6
14=2*7
16=2*8
18=2*9
20=2*10

step1:start
step2:multiply
step3:store  ===:>repeated 10 times==>loop
step4:print to user
step5:stop

fix the following:
initialization, i=1
condition    i<=10 or i<11

increment/decrement: i=i+1

body

'''
n=int(input("Enter a number for table printing"))
i=1
while i<=10:
    r=n*i
    print(r)
    i=i+1

'''
i  i<=10    r=2*i    print(r)        i=i+1
1  1<=10    r=2*1     2              i=1+1=2
2  2<=10    r=2*2     4              i=2+1=3
3  3<=10    r=2*3     6              i=3+1=4
.
.
.
.
.
.
10 10<=10   r=2*10    20              i=10+1=11
11 11<=10 F=> stop




'''
