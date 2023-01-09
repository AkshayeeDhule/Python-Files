'''
scope of variable:
================
The section in the program where value of the variable can be accessed is called as
scope of variable.

or
life of a variable.

There are two types of scope:
1)Local scope
2) Global scope


'''
'''
The variable that is defined outside the function and whose value can be accessed
outside as well as inside the function is called as Global Variable.

'''

x=10

print("Value of variable x outside function: ",x)

def scope_variable():
    print("Value of variable inside function: ",x)
