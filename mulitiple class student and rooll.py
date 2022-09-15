class student:
    def __init__(self,rollno,name,age,address,course,mobile):
        self.rollno=rollno
        self.name=name
        self.age=age
        self.address=address
        self.course=course
        self.mobile=mobile
    def display(self):
        print(self.rollno,end='\t\t')
        print(self.name,end='\t\t')
        print(self.age,end='\t\t')
        print(self.address,end='\t\t')
        print(self.course,end='\t\t')
        print(self.mobile,end='\t\t')
st=list()
n=int(input("enter no of students:"))
print("students details entry..")
for i in range(n):
    print('student: ',i+1)
    rollno=input('\tRollno : ')
    name=input('\tName : ')
    age=int(input('\tAge : '))
    course=input('\tcourse : ')
    address=input('\taddress : ')
    mobile=input('\tMobile : ')
    st.append(student(rollno,name,age,course,address,mobile))

print('student information')
print('Rollno\t\tName\tAge\tcourse\taddress\tMobile')
for i in range(n):
    for j in range(i+1,n):
        if (st[i].name>st[j].name):
            tmp=st[i]
            st[i]=st[j]
            st[j]=tmp
print('student information')
print('Rollno\t\tName\tAge\tcourse\taddress\tMobile')
for i in range(n):
    st[i].display()


    
        
