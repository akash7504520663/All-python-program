class Bank:
    bank_name='Bob'
    bank_address='Bangalore'
    bank_roi=7
    def __init__(self,n,a,bal,roi):
        self.name=n
        self.age=a
        self.bal=bal
        self.roi=roi

    def customer_details(self):
        print(self.name)
        print(self.age)
        print(self.bal)
        print(self.roi)
seetha=Bank('S devi',23,98765,3)
ankita=Bank('a devi',23,98765,3)

geetha=Bank('geetha',24,45679,9)


geetha.customer_details()
seetha.customer_details()
ankita.customer_details()

