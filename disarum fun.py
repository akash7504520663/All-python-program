def isdisarum(n):
    summ=0
    position=len(str(n))
    num=n
    while n>0:
        rem=n%10
        sum+=rem**position
        position=position-1
        n=n//10
    if num==summ:
        return True
    else:
        return False
def disarum(ll,ul,uapdation=1):
    for i in range(ll,ul,uapdation):
        if isdisarum(i):
            print(i)
disarum(1,13)
