'''
Nested if...else
================

Need: If there are more than one conditions to be 
      checked to give decision, then use nested if..else.
	  

Register
========
1) set username. => ru=itvedant123
2) set password. => rp=redhat123@

login
=====

username:__________ =>lu=itvedant123 
password:__________	=>lp=redhat123@

if lu==ru: True|True|False 

   if lp==rp: True |false
   
       Direct user to his dashboard.
   else:
   
       invalid username and password

else:

    invalid username and password
	


Program:greatest of Three numbers

x=80|50|20
y=20|20|80
z=50|80|50

if x>y: T | T | F
 
   if x>z: T | F
   
     display value in x as greater.
   else:
   
      display value in z is greater.
else:
    
	if y>z:T | F
	  value in y is greater.
	  
	else:
	  value in z is greater.
	  
Disadvantage of nested if...else:
================================
1)care need to  be taken to match corresponding pairs of
  if's and else's 
2)Care need to be taken for code indentation that may
  result into indentation error.
3) As condition increases program creeps towards right side.
  

Logical Operators
=================
Need
----
1)If there is need to handel more than one condition in 
  if statement we use logical operators.
2)To remove disadvantage of nested if else, we use logical
  operators.
  
  
  3+4 
  
  operator =>+
  Operation=>Addition
  operands =>3,4
  
  operands of logical operators are conditions 
  Logical operators are going to operates on condition.
  
Types of logical Operators 
==========================
1)Logical AND 
2)Logical OR 
3)Logical NOT 

Logical AND and OR are called as Binary operators,as
they operators on two conditions at a time.

Logical NOT is called as Unary operator as it operates
on single condition at a time.

'and' Truth table
================
cond1   cond2    cond1 and cond2 
T         T        T   and T => T 
T         F        T   and F => F 
F         T        F   and T => F 
F         F        F   and F => F 

'or' Truth table
================
cond1   cond2    cond1 or cond2 
T         T        T   or T => T 
T         F        T   or F => T 
F         T        F   or T => T  
F         F        F   or F => F 

'not'truth Table 
================

cond     not cond 
T        not T => F 
F        not F => T 


x=80
y=50
z=20

if x>y and x>z: 80>50 and 80>20 => T and T => T

   x is greater 
   
if y>x and y>z: 50>80 and 50>20 => F and T => F
   y is greater 
   
if z>x and z>y: 20>80 and 20>50 => F and F => F

   z is greater 
   
   
username and password 

if ru==lu and rp==lp:
   direct user to dashboard 
   
else:

   invalid username and password 

   
  
to save execution time 
======================
if x>y and x>z: 80>50 and 80>20 => T and T => T

   x is greater 
else:  
    if y>x and y>z: 50>80 and 50>20 => F and T => F
       y is greater 
    
	else:
      if z>x and z>y: 20>80 and 20>50 => F and F => F
	     z is greater
		 
Above code save execution time but again may gave rise 
to the disadvantage of nested if..else.

In order to satisfy both 
1) save execution time       ====> elif
2) not to use nested if else 

if x>y and x>z:

   x is greater 
   
elif y>x and y>x:

   y is greater 
   
elif z>x and z>y:
  z is greater 
  
    

   '''

   
   
