'''
import string as s

alpha= s.ascii_letters
digit=s.digits

print(alpha)
print(digit)

alnum=alpha+digit
print(alnum)

'''
'''
import string as s
import string as r

captcha=""

for i in range(0,5):

    index=r.randrange(0,len(alnum))
    print(index)
    print(alnum[index])
    captcha=captcha+alnum[index]
    print(captcha)
    print("-------------")
    
'''


captcha=""

for i in range(0,5):

    index=r.randrange(0,len(alnum))
    captcha=captcha+alnum[index]

print(captcha)
    
