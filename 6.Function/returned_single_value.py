
'''
syntax:

def function_name(arguments):

    function body

    return value

Need: If there is need for a function to return a value or
      result there use return statement.
Problem:
=======
values given to function=>marks of 3 subjects
definition of function  =>Calculate total

%  = marks obtained           marks obtained
     -------------- x 100  => ---------------  
        300                          3

returned value is returned at the place of the function call.
Thus we require a variable to which function call is assigned
so that returned value is stored in that variable.
'''
m1=int(input("Enter marks of First student ")) #m1=70
m2=int(input("Enter marks of Second student ")) #m2=80
m3=int(input("Enter marks of Third student ")) #m3=90

def marksadd(a,b,c): #function definition

    t=a+b+c    #t=70+80+90=240

    return t

tot=marksadd(m1,m2,m3)    #function call => m1=70, m2=80, m3= 90

print("Total marks: ",tot)
