
n=int(input(' Enter Number '))

for i in range(2,n,1):
    r = n%i 
    
    if r==0:
            print(n,'Non-Prime Number')
            break
else:
    print('It is prime number')


