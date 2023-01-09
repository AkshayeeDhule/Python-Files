'''
1. required argument
2. Default argument
3. Key value pair argument.
   key=value


   area of rectangle=length x breadth

           3
    ---------------
   |               |
   |               | 2    area=3x2=6
   |               |
    ---------------
'''

def area(l,b):
    print("Length of the rectangle to be manufactured: ",l)
    print("Breath of the rectangle to be manufactured: ",b)

    area=l*b

    print("area of rectangle is: ",area)

area(b=20,l=10)    
