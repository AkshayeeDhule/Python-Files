
'''
conversions: list,tuple, set
'''

t=(10,20,30,40)
print(t)
print(type(t))

#convert tuple into list
#list(): This method is used to convert datatype into list.

l=list(t)
print(l)
print(type(l))

#changing element value

l[2]=300
print(l)

#tuple():This method is used to convert datatype into tuple.

tnew=tuple(l)
print(tnew)
