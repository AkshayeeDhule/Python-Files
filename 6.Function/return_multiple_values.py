n1=int(input("Enter First Value :")) #n1=9
n2=int(input("Enter Second Value :")) #n2=2

def arithmetic(x,y): #x=9  y=2

    add=x+y #add=9+2=11
    sub=x-y #sub=9-2=7
    mul=x*y #mul=9*2=18
    div=x/y #div=9/2=4.5
    return add,sub,mul,div

a,b,c,d= arithmetic(n1,n2) #addition(9,2)=> add,sub,mul,div

#a,b,c,d= add,sub,mul,div

print("Addition is : ",a)
print("Subtraction is : ",b)
print("Multiplicaton is : ",c)
print("Division is : ",d)
