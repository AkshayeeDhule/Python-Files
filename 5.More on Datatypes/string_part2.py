'''
x="Itvedant-Eclass"

#print(x[9])

x[9]='e'
print(x[9])

'''

'''
x="Itvedant-Eclass"
for i in range(0,len(x),1):

    print(x[i])
'''

#without index
'''
x="Itvedant-Eclass"

print("Without Index")

for i in x:
    print(i)
'''
'''
x="Itvedant-Eclass"

print(x[2])
x[2]='o'
print(x[2])
'''

'''
Find number of vowels and Consonants in the string
entered by user.

a,e,i,o,u,A,E,I,O,U
'''


'''
str=input('enter string: ')
print(str)

v=0
c=0

for x in str:
    
    if x in ('a','e','i','o','u','A','E','I','O','U'):
        
      v+=1
      
    else:
        
      c+=1

print("Total number of Vowels:",v)
print("Total number of Consonants:",c)

Dry_run:

x  x in ()     v=v+1    c=c+1
i  i in ()T    v=0+1=1    --
t  t in ()F    v=1      c=0+1=1
v  v in ()F             c=1+1=2
e  e in ()T    v=1+1=2  c=2
d  d in ()F    v=2      c=2+1=3
a  a in ()T    v=2+1=3  c=3
n  n in ()F    v=3      c=3+1=4
t  t in ()F    v=3      c=4+1=5

        
'''
