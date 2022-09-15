a=2
n=int(input("enter a num"))
while a<n//2+1:
    if n%a==0:
        print("prime is not using")
        break
    a=a+1
else:
    print("prime is using")
