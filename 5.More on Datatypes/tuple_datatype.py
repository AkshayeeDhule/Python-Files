'''
tuple
=====
1)It is collection of dissimilar datatype elements.
2)Elements in the tuple are enclosed in round brackets [parenthesis]
3)They are immutable.once tuple is defined it cannot be changed.
'''
'''
t=(10,20,'Itvedant',89.9,'Eclass')
print(t)
print(type(t))
'''
#len()
'''
n=len(t)
print("Total number of elements in Tuple : ",n)
'''
'''
t=(10,20,'Itvedant',89.9,'Eclass',10,20,30,20)
n=t.count(10)
print("Total number of occurance in Tuple : ",n)
'''

t=(10,20,'Itvedant',89.9,'Eclass',10,20,10,30)
ipos=t.index(89.9)
print("Index Position is: ",ipos)


'''
for i in range(0,len(t)):

    if t[i]==20:

        print(i)

'''
#del
del t
print(t)
