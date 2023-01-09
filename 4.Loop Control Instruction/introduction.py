'''

Need of Loop control instruction or
Iterative Statement 
===================================
step1 :start
step2 :display Hello world.    ======>  Hello World
step3 :display Hello world.    ======>  Hello World
step4 :display Hello world.    ======>  Hello World
step5 :display Hello world.    ======>  Hello World
step6 :display Hello world.    ======>  Hello World
step7 :display Hello world.    ======>  Hello World
step8 :display Hello world.    ======>  Hello World
step9 :display Hello world.    ======>  Hello World
step10:display Hello world.    ======>  Hello World
step11:display Hello world.    ======>  Hello World

Repeatition must be avoided.
Disadvantage of Repeatition
1)Length of program increases due to which debugging or
  error finding become difficult.

Repeatition must be avoided and Reusability of code must
be achieved.

Reusability: Writing code once and use many times.
DRY:  Donot  Repeat Yourself.

To overcome disadvantage of code repeatition by writing
code once and repeating it finite or infinite number 
of times there is need of loop control instruction.

What are loops or iterative statements?
======================================
The statements which allows programmer to write code
once and repeat it finite or infinte number of times
to achieve reusability is called as Iterative statement or
loop control statement.


Types of Loop control instruction 
=================================
1)while loop
2)for loop 


While loop 
=========
syntax:

initialization;

while condition:

    code to be executed
	
	increment/decrement
	
working:
step1:initialization [Done only once]
step2:check condition 
step3:If condition is True then executed code or loop body.
step4:increment or decrement 
step5:repeat step2 to step4 till condition is True.
step6:Once condition is False ,go to step7.
step7:stop


                          initialization
                                |
							    |       False
                 ----------->condition-------->Out of loop
                |               |
                |               | True
                |          code in loop[Body]
                |               |
                |               |
                |               |
				incre/decre<----


Iterative statement to print 1 to 10 numbers.

i=1


while i<=10:

    display i
	
	i=i+1
                							   
	
i    i<=10      display i     i=i+1
1    1<=10 T    1             i=1+1=2
2    2<=10 T    2             i=2+1=3 
3    3<=10 T    3             i=3+1=4 
4    4<=10 T    4             i=4+1=5
5    5<=10 T    5             i=5+1=6
6    6<=10 T    6
7
8
9
10   10<=10 T   10            i=10+1=11
11   11<=10 F   

Each step executed in the loop is called as Iteration 
e.g 2    2<=10 T    2             i=2+1=3  is a iteration.
                
finite  => One has a end. 
infinite=> Never Ending. 

Finite Loop
===========
The loop in which at certain iteration condition become
false and loop stops is called as Finite Loop.

Infinite Loop 
============
The loop in which condition is always true is called as
infinite loop.



i=1 

while i>0:

    diaply i 
	
	i=i+1
	

In above example i>0 this condition is always True.
hence Loop repeats infinite number of times.


Factorial of Given number 
=========================

;;;
