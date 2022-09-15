class Address:
    def __init__(self,n,c,s,co):
        self.Jname=n
        self.Jcity=c
        self.Jstate=s
        self.Jcountry=co
    def display_location(self):
        print('city',self.Jcity)
        print('state',self.Jstate)
        print('country',self.Jcountry)
Bangalor=Address('marathahalli','bangalor','karnatak','india')
class Trainer:
    def __init__(self,n,a,sub,address):
        self.Tname=n
        self.Tage=a
        self.Tsubject=sub
        self.Taddress=address
    def Trainer_information(self):
        print('name',self.Tname)
        print('age',self.Tage)
        print('sub',self.Tsubject)
        self.Taddress.display_location()
Harshad=Trainer('Harshad',27,'Python',Bangalor)
Harshad.Trainer_information()
