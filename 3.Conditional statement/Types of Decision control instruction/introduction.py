
'''
Instruction or statement
=======================
This is command or order given to machine to perform certain
task.

Types of instruction
====================
1)Arithmetic instuction.
2)Decision control instruction.
3)Loop control instruction.


1) Arithemtic Instruction 
   ----------------------
   The instruction which contains arithmetic operator is called
   as Arithemteic Instruction.
   
   z=x+y
   z=x-y
   z=x*y
   z=x/y

2)Decision control instruction 
  ----------------------------
  ATM machine PIN enter Step 
  -------------------------
  step1:user enter four digit pin.
  step2:machine compare the pin enter by user to the
        pin set by user for the first time of card use.
		
		Pin enter by user = pin set by user
		
		condition 1:
		==========
        Pin enter by user = pin set by user ===> machine 
		                                         allow user to move
												 further.
												         
		condition 2:
		===========
		pin enter by user not equal to pin set by user ===> you did not
		                                                   enter correct pin.
	
	
	The instruction which takes decision based on 
	certain condition is called as Decision Control instruction.
	


Types of Decision control instruction 
====================================
1) if statement 
2) if..else statement 
3) nested if else statement 
4) logical operators.
5) elif


condition 
---------
condition is made up  of comparison operators.
comparison operators are:<,>,<=,>=,==,!=  

x >y   x is greater than y
x <y   x is less than y 
x <=y  x is less than or equal to y 
x >=y  x is greater than or equal to y 
x ==y  x is equal to y . LHS = RHS 
x !=y  x is not equal to y. [! not]

condition can be True or false.
x=10  y=20 

x>y  10>20  => false 
x<y  10<20  => True 
x==y 10==20 => false

if statement 
===========
syntax:(python)
-------
if condition:

   body of if or 
   code to be executed when 
   condition is True.
   
working of if 
============
if the condition is True then only the code written inside
if body is executed.
if the condition is false then code written in the if body
is not executed.

if...else 
=========
syntax:

if condition:

   if body code to 
   be executed.
   
else:

   else body code to 
   be executed.
   
working:
======
if the condition is True then code inside if will be executed.
if the condition is false then code insde else will be 
executed. 

e.g
pin1=pin entered by user 
pin2=pin set by user in the bank for first time.

if pin1==pin2:

    display menu for the user.

else:

   display message that he had entered incorrect
   pin.   
   
   
e.g:
===
Greatest of the two numbers given by user.

x=10|30|5
y=20|20|5

if x>y:

   display x is greater. 
   
else:

   display y is greater.
   
   
step1:start
step2:take values of x and y from user=> input=>input box
step3:compare values 
step4:Give decision for the greatest value.
step5:stop.

'''
