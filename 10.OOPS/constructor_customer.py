

class customer:

    def __init__(self):

        self.bname="SBI"
        self.ifsc="SBIN123456789"
        self.loc="Eclass"

    def getdata(self):

        self.name=input("Enter Customer Name: ")
        self.mob=input("Enter Mobile Number: ")
        self.bal=input("Enter Account Opening Balance: ")

    def display(self):

        print("Bank Details: ")
        print("----------------------------")
        print("Bank Name: ",self.bname)
        print("Bank IFSC: ",self.ifsc)
        print("Bank location: ",self.loc)
        print()
        print("Customer Details: ")
        print("----------------------------")
        print("Customer Name: ",self.name)
        print("customer Mobile: ",self.mob)
        print("Customer Balance: ",self.bal)


c1=customer() #object created => constructor is called
c1.getdata()  #getdata(c1)
c1.display()#display(c1)
print()
c2=customer() #object created => constructor is called
c2.getdata()  #getdata(c2)
c2.display()#display(c2)


'''
                            c1
                            |
          ----------------------------------------------------------------
          |          |               |           |         |             |
          bname     ifsc            loc       name       mob          bal
          SBI     SBIN123456789    Eclass    itvedant  9898989898     5000
'''
        
