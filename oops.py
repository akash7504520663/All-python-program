class Bank:
    bank_name='Bob'
    bank_address='Bangalore'
    bank_roi=7
    #created
    def __init__(self,n,a,bal,roi):
        self.name=n
        self.age=a
        self.bal=bal
        self.roi=roi
    
    #display
    def customer_details(self):
        print(self.name)
        print(self.age)
        print(self.bal)
        print(self.roi)
    #modify
    def deposite(self,amount):
        self.bal+=amount
        print('deposite is successfull')
        print(self.bal)
        
    
        


Akash=Bank('Akash',23,98765,3)

#Akash.customer_details()


