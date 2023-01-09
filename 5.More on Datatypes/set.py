'''

set
1)Set is collections of dissimilar datatype elements.
2)sets are enclosed within curly braces {}
3)sets are mutable.
4)sets are unordered.
   In other data types index position of the element is fixed.
   but in set position of the element changes.
5)sets allows only unique values[no duplication].
'''

'''

s={10,20,'Itvedant',89.9,'Eclass'}
print(s)
print(type(s))
'''
#len()
'''
n=len(s)
print("Total number of elements in the sets: ",n)

print(s[1])
'''

#Error

#indexing or accessing elements is not possible in set
#slicing which require index is not possible in set

#for loop over set
# for loop with index
'''
s ={10,20,'Itvedant',89.9,'Eclass'}

for x in s :
    print(x)

'''    
#add element in the set
    
'''
add(): This function is used to add element in the set.

  set_varianle.add(value)
'''

'''
s ={10,20,'Itvedant',89.9,'Eclass'}
s.add('Itvedant-Eclass')
print(s)

s.add(20) #no duplicate values are allowed in the set.
'''

#updating an existing value is not possible in set ==> no index

#delete or remove element from set
'''
set_variable.remove(value)
'''
s ={10,20,'Itvedant',89.9,'Eclass'}
s.remove(89.9)
print(s)


del s
print(s)
