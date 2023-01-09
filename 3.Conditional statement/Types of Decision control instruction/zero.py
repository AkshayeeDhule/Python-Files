'''
Nested if else
=============
When there is need to give decision based on more than
one condition.

syntax:

if Condition1: T | T | F
 
   if Condition2: T | F
   
     execute if block.
   else:
   
      excute else block.
else:
    
	if Condition3:T | F
	  excute if block.
	  
	else:
	  excute else block.

checking
========
step1:first check for zero and non-zero
step2:if zero then display neither positive nor negative.
step3:if non-zero, then further check for positive and negative.
  
'''

print("enter a number")
n=int(input())

if n==0:
      print("Number is neither positive nor negative")
else:
      if n>0:
       print("Positive Number")
      else:
       print("Negative number")

    


'''

n=int(input("enter a number:"))
if n==0:
      print("no is either pos or neg")
else:
      if n>0:
            print("Positive")
      else:
            print("Negative")
            
 '''     
          
