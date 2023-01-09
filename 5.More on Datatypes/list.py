'''
List:
1) list is a collection of dissimilar datatype elements.
2) Elements in list are enclosed in square brackets[].

There are two methods or function to add
element in the list.
1)append():
   This function or method is used to add element at the
   end of the list.
   syntax:
          list_variable.append(element)
'''

l=[10,89.7,45.6,'Akshu']
l.append(24.5)
print(l)

'''
2) insert(): This function or method is used to add elements at specific index position.

     list_variable.insert(index_pos,value)

'''

l.insert(2,50)
print(l)


#update list elements

'''
syntax:

  list_variable[index_pos]=value
'''

l[4]='Akshayee'
print(l)


#delete or remove list elements

'''
pop(): This is used to delete last elements.

pop(index):This remove specific element whose index is
mentioned in the pop() method.

'''
'''
[10, 89.7, 50, 45.6, 'Akshayee', 24.5, 'Dhwani']
 0    1     2   3       4                5      6
 '''
l.pop()
print(l)

'''
[10, 89.7, 50, 45.6, 'Akshayee', 24.5]
 0    1     2   3       4                5      
'''
l.pop(2)
print(l)
