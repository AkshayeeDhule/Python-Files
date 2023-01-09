
'''
variable length argument => key value pair

'''

def addition(**x):

   print(x)
   print(type(x))
        
addition(a=10,b=20) #l=2
addition(a=10,b=20,c=30) #l=3
addition(a=10,b=20,c=30,d=40) #l=4


'''
def addition(**x):
    
    sum=0
    
    for y in x:
        
        sum=sum+(x[y])
        
        print("Summation is: ",sum)

   #print(x)
   #print(type(x))
        
addition(a=10,b=20) #l=2
addition(a=10,b=20,c=30) #l=3
addition(a=10,b=20,c=30,d=40) #l=4
'''
