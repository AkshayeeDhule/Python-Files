'''
what is loop or iterative statement?

The statement which helps us to repeat the code n numbers of times by writting
it only one time is called as Iterative statment.

Types of iterative:
1) while loop
2)for loop

while loop
syntax:

initialization

while condition:
body of while loop

increment/decrement


working of while loop:

                      initialization
                            |
                            |
                            |       False
                  ------>condition----->out of loop
                  |         | T
                  |         |
               inc/dec  --->body
  
'''
print("Hello world!!")
print("Hello world!!")
print("Hello world!!")
print("Hello world!!")
print("Hello world!!")

'''
Disadvantages in code repeatation:
1) length of the program increases due to which error
   finding or debugging may be difficult.
2) compiler or interpreter is engaged in checking same piece of code again and again.   
'''


i=1 #initialization
while i<=10: #condition
    
    print("Hello World")
    
    i=i+1 #inc
