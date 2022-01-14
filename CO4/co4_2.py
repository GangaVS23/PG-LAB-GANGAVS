#. Create a Bank account with members account number, name, type of account and balance.
#Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class Bank:
    def __init__(self,bal=0):
        #self.accno=accno
        #self.name=name
        #self.acctype=acctype
        self.bal=bal
        name=input("Enter name : ")
        print(".....Account for",name,"is created.....")
        
    def deposit(self):
        amount=int(input("Amount to deposit : "))
        self.bal=self.bal+amount
        print("New balance:",self.bal)
    def withdarw(self):
        amount=int(input("Amount to withdraw : "))
        if(self.bal>amount):
            self.bal=self.bal-amount
            print("New balance:",self.bal)
        else:
            print("....Insufficient Balance....")
            print("Current balance : ",self.bal)
    
    def display(self):
        print("Current Balance:",self.bal)

print("..........Account..........")
b1=Bank()
opt='y'
while(opt=='y'):
    #print("your choice: 1. deposit \n 2. withdarw \n 3. display\n")
    choice=int(input("Choices are: \n1. Deposit\n2. Withdarw \n3. Display\n\nEnter your choice: "))
    if(choice == 1):
        b1.deposit()
    elif(choice==2):
        b1.withdarw()
    elif(choice==3):
        b1.display()
    else:
        print("Invalid Choice")
            
    opt=input("Do you want to continue? (Enter 'y'/'n') : ")





