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
Kolkata=Address('Lacktown','Howra','westbengal','india')
Assam=Address('jamunapur','assam','Guwahati','india')
class student:
    def __init__(self,n,a,sub,address):
        self.sname=n
        self.sage=a
        self.ssubject=sub
        self.saddress=address
    def student_information(self):
        print('name',self.sname)
        print('age',self.sage)
        print('sub',self.ssubject)
        self.saddress.display_location()
Akash=student('Akash',24,'Python',Kolkata)
Akash.student_information()
print('*'*10)
