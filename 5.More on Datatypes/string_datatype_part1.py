#String

'''
x="Itvedant-Eclass"
print(x)

dt=type(x)
print(dt)


Two types of accessing:

1. Positive Access:

   I t v e d a n t - E c  l  a  s  s
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

   
   
2. Negative Access:

     I    t   v  e   d   a   n  t  -  E  c  l  a   s  s
    -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3  -2 -1
    
    '''

#positive index
'''
x="Itvedant-Eclass"
print(x[2])
print(x[12])
print(x[14])

print(x[-14])
'''

#slicing

#string_variable[start:stop:step]
'''
   I t v e d a n t - E c  l  a  s  s
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
'''
 #positive slicing
'''
x="Itvedant-Eclass"
x1=x[2:8:1]
print(x1)

x2=x[2:8:]
print(x2)

x3=x[:8:]
print(x3)

x4=x[::]
print(x4)
'''

#negative slicing
'''
 I    t   v  e   d   a   n  t  -  E  c  l  a   s  s
-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3  -2 -1
'''
'''
x="Itvedant-Eclass"
x1=x[14:8:-1]
print(x1)

x2=x[:2:-1]
print(x2)

x3=x[::-1]
print(x3)

x4=x[::]
print(x4)
'''

#Adding an element
'''
x="Itvedant-Eclass"
x[9]="e"
print(x)

error: string do not support item assignment.
also we cannot add or delete any character from the string.
Thus string are caleed as immutable.
Immutable means once formed they cannot be changed by any of the following means:
1) Add 2) Update 3) Delete

'''

#for loop over a string
x="Itvedant-Eclass"
n=len(x)
for i in range(0,n,1):
    print(x[i])


for x1 in x:
    print(x1)

