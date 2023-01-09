'''
When there is need to preserve old data or new data must be
added at the end of the old data use append mode.

'''

fp=open('data,txt','a')
mn=input("Enter Mobile number:")
data=mn+"\n"
fp.write(data)
fp.close()

'''
If a file is open in write mode and it has previous data,
then new data get overwritten on the previous data.


OTP generated
1)Send to user mobile number
2)store in database or file in web application.

when user enter OTP

For verification
OTP entered by User is matched with the OTP stored in File.
If above condition is true then user mobile is verified.
'''


