fp=open("data.txt",'r')

d=fp.readlines()

print("data in the file is:")

print(d)

print(d[0])
#print(d[1])
#print(d[2])

print("Using for loop:")

for x in d:

    print(x)
