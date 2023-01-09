'''
Variable defined in the function or in a scope has life or accessibilty to its
value within that scope only, it cannot be accessed outside that scope.
This type of variable is called as local variable.
'''

def scope_variable():
    x=50
    print("Value of variable inside functio: ",x)
scope_variable()
print("Value of variable outside function: ",x)
    
