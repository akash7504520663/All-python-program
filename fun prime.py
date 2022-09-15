def isprime(n):
    if n>1:
        
        for i in range(2,n//2+1):
            if  n%i==0:
                return False
        else:
            return True
    else:
        return False
def evennumbers(ll,ul,uapdation=1):
    for i in range(ll,ul,uapdation):
        if isprime(i):
            print(i)
evennumbers(1,13)  
  
