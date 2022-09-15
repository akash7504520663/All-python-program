def fun (n):
    nu=1
    for i in range(0,n):
        for j in range(0,i+1):
            if nu % 2==0:
                print('>< ' ,end='')
            else:
                print('<> ',end='')
            nu+=1
        print()
num=10
fun(num)
    
n=int(input("enter a num"))
nu=1
for i in range(0,n):
    for j in range(0,i+1):
            if nu % 2==0:
                print('>< ' ,end='')
            else:
                print('<> ',end='')
            nu+=1
    print()
