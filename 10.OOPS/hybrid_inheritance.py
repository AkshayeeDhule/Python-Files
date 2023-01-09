'''
Hybrid inheritance
==================
The inheritance which is the combination of Hirarchical and
multiple inheritance is called as Hybrid Inheritance.

                        A geta() => self.a
                        |
                 -----------------
                |                 |
getb()=>self.b  B                 C  self.c <= getc()
                |                 |
                 ----------------
                        |
                        D addition()
class A:


class B(A):


class C(A):



class D(B,C):
