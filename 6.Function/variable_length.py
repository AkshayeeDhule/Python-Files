'''

variable length argument
========================

variable:changing

length:number of argument


'''

'''
def addition(x,y):

    z=x+y

    print("Addition is: ",z)

addition(20,30)
addition(50)
'''

def addition(*x):

   # print(x)
   # print(type(x))
   sum=0
   for i in x: #(20,30)|(20,30,40)|(50)

       #print(i)
       sum=sum+i

   print("Summation is: ",sum)    

addition(20,30)
addition(20,30,40)
addition(50)


#addition(20,30)
#x=(20,30)

'''
i  i  in x    sum=sum+i      i
20 20 in x[T] sum=0+20=20    30
30 30 in xT   sum=20+30=50      --F

summation is:50

'''
#addition(20,30,40)
#x=(20,30,40)

'''
i   i in x    sum=sum+i    i




'''

