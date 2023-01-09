#Recursive function: calling function on its own body is called as recursive function.

#foe eg

'''
def greet():
    print("Good Morning!!")
    greet()

greet() #RecursionError: maximum recursion depth exceeded while pickling an object.....recursive function gives looping effect.

'''

#Summation of 1 to n :

''''
num=int(input("enter the last term in the series: "))
def summation(n):   #function body
    if n==1:
        return 1
    sum=n+summation(n-1)   #recursion
    return sum

res=summation(num)           #function call
print("Summation is: ",res)
    
'''

'''
  Disadvantages:
  1] In recursion for every function call there is function body executed, so each function call, function body need to be stored in the memory in the form of stock.
  2] if recursion exceeds that stack limit, then we get recursion error showing maximum limit/ depth is exceeded.



  Advantage:
  recursion allows you to write short code and shorter code function is the execution
  
'''

# factorial of number by recursion:

num=int(input("enter the last term in the series: "))
def facto(n):    #function body
    if n==1:
        return 1
    fact = n*facto(n-1)     #recursion
    return fact

res=facto(num)    #function call
print("Factorial is: ",res)
