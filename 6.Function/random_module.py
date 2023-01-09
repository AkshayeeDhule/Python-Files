'''
random module
'''

import random as r

#random()

'''
x=r.random() #gives fraction value between 0 and 1
print(x)

t=x*10000
print(t)

otp=round(t)
print("otp to be send:",otp)

'''

otp=round(10000*r.random())
print("OTP to be send:",otp)
