'''
Custom Exception
===============
Creating or definig your own exception other that built in
exception.
If you want your error name to be recognised as python exception
it must be derived from the base class Exception

'''

class ItvedantError(Exception):
    pass

x=int(input("Enter Numerator ")) #x=9|x=9
y=int(input("Enter Denominator ")) #y=2|y=0

if y==0: #2==0 F| 0==0 T

    raise ItvedantError('Denominator can not be zero!!')

else:
    d=x/y #9/2=>4.5 | 0/0=> Exception is raise
    print("Division is:",d)
