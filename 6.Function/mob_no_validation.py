'''
validation:
=========
Input given by  the user is as per rule defined by developer
in the application or validating the input.

Validate mobile number
======================
1.Check whether it is digit or not => isdigit()
2.Check whether it is 10 digit.
'''

mob=input("Enter mobile number: ") #8087670877

if mob.isdigit():

    if len(mob)==10:
        print("Valid mobile number")

    else:
        print("invalid mobile number")


else:

    print("Invalid Mobile Number")
