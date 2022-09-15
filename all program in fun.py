def isprime(n):
    if n>1:
         for i in range(2,n//2+1):
                if n%i==0:
                        return False
         else:
            return True
    else:
        return False
def isemirp(n):
    if isprime(n):
        s=str(n)
        rev=int(s[::-1])
        if isprime(rev):
            return True
        else:
            return False
    else:
        return False
def emirpnumber(ll,ul,uapdation=1):
    for i in range(ll,ul,uapdation):
        if isemirp(i):
            print(i)
emirpnumber(1,13)
def isharsad(n):
    sum=0
    num=n
    while n>0:
        rem = n%10
        sum=sum+rem
        n=n//10
    if num % sum==0:
        return True
    else:
        return False
def harsad(ll,ul,uapdation=1):
    for i in range(ll,ul,uapdation):
        if isharsad(i):
            print(i)
harsad(1,13)

def isdisarum(n):
    summ=0
    position=len(str(n))
    num=n
    while n>0:
        rem=n%10
        summ+=rem**position
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
def isamstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if temp == sum:
            return True
        else:
            return False
def amstrong(ll,ul,uapdation=1):
    for i in range(ll,ul,uapdation):
        if isamstrong(i):
            print(i)
amstrong(1,13)
def isperfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=1
    if sum==n:
        return True
    else:
        return False
def perfect(ll,ul,uapdation=1):
    for i in range(ll,ul,uapdation):
        if isperfect(i):
            print(i)
perfect(1,13)

                
