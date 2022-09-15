class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello Central bank")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited Satya: "))
        self.balance += amount
        print("Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("Withdrew:", amount) 
        else:
            print("Insufficient balance  ")
 
    def display(self):
        print(" Available Balance=",self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
