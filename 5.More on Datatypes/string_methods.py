#capitalized(): first character to upper case

x="itvedant"
print(x)
x1=x.capitalize()
print(x1)

#upper():lower to upper

s2=x.upper()
print(s2)

#lower(): upper to lower

x1="ITVEDANT"
s3=x1.lower()
print(s3)


#isdigit():

z="123456789"
y=z.isdigit()
print(y)

a="1234abc"
b=a.isdigit()
print(b)

#format()

c=10
d=20
e=c+d
print("Addition of",c,"and",d,"is",e)

#split()

f="we are, learning, strings,in python"
g=f.split(',')
print(g)

h="we are: learning: strings:in python"
i=h.split(',')
print(i)

#without index:

j="Itvedant-eclass"
print("without index")
for i in j:
    print(i)

#with index
k="Itvedant-eclass"
print("with class")
print(k[2])
k[2]='o'
print(k[2])
    
