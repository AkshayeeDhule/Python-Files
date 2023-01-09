'''
type(): Returns you the data type of a variable.

more data types:
1)string
2) list
3) tuple
4) set
5) dictionary


'''

#1)String

'''
Accessing string elements:
String is a collection of characters. each character is called as string elememt.

If there is need to process a string character by character
then we require single character access.

single had index.

 I  T    V   E  D  A  N  T  -  E  C  L  A  S  S
 0  1    2   3  4  5  6  7  8  9  10 11 12 13 14 -> positive index
-15 -14 -13 -12...............................-1->negative index

syntax:
string_variable(index_number)

'''

#x='Itvedant'

#x="Itvedant-Eclass"

'''
x= This ia a string multiline string itvedant eclass learning string

print(x)
print(type(x))

'''

#len(): This is used to calculate number of charaters in the string.

x="Itvedant-Eclass"

print(x)
print(type(x))

n=len(x)
print("Total number of characters: ",n)

#indexing

'''
Need: To process string character by character, there is need to access character in the string.
      Indexing helps you to access character in the string.
      
There are two types of indexing:
1) Positive Indexing
2) Negative Indexing

Positive Index :                  x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Negative Index :                 
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
'''

'''
print(x[7])
print(x[12])
#print(x[16]) #Error: Index out of range
print(x[-14])
print(x[-11])

'''

#Slicing

'''
Need of slicing:
==============
If there is need to extract partial part of the string from
entire string , then use slicing.
1) to reverse string.

syntax:

string_variable[start:stop:step]
                                   x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

Extract vedant word from the give string.

start=>2  stop=>8  step=>1
'''
#x1=x[2:8:1]
#print(x1)

#x1=x[2:12:2]

#x1=x[2:8:] #default step in slicing is 1

#x1=x[:8:]  #default start is 0

#x1=x[::] #default stop= string end
#print(x1)

'''
slicing with negative index

                        Negative Index                  
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
          0   1   2  3   4   5  6   7 8  9 10  11 12 13 14
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

step=> negative

conclusion:
if step is positive then start=left  end=right
if step is negative then start=right end=left
'''

#x1=x[14:8:-1]  #14,13,12,11,10,9
#x1=x[:2:-1]
x1=x[::-1]
print(x1)
