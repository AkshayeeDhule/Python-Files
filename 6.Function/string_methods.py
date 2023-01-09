s="Itvedant-Eclass"
print(s)
print(type(s))

'''
sup=s.upper()
print(sup)

slow=s.lower()
print(slow)

'''

#isalpha()
'''
This method check whether entire string contains alphabets.
If all string elements are alphabets then it return True
or it returns False.
'''

#s="Itvedant-Eclass"

#s="Itvedant Eclass"
'''
s="ItvedantEclass"

r=s.isalpha()
    
print(r)
'''

#isdigit():
'''
This method is used to check whether string elements are
digits i.e 0,1,2,3,...9
It returns True if string contains all digits.
It returns False if string contains other than digit.
'''

#s="1234567"
'''
s="1234567a"
r=s.isdigit()
print(r)
'''

#split()

'''
When there is need to convert a string into list, split() method is used.

syntax:
    str_variable.split('separator')
'''

'''
s='we are learning, String Methods, in todays class'
print(s)
#l=s.split(',')
l=s.split('-')
print(l)
print(type(l))
'''

s='we are learning, String Methods in todays class'
print(s)
l=s.split()
print(l)
#Default separator is space.
