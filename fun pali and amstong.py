def ispalindrome(n):
    rev=0
    num=n
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if num==rev:
        return True
    else:
        return False
def isprime(a):
    if a>1:
        for i in range(2,a//2+1):
            if  a%i==0:
                return False
        else:
            return True
    else:
        return False
def palindrome_prime(ll,ul,uapdation=1):
    for j in range(ll,ul):
        if isprime(j) and ispalindrome(j):
            print(j)
palindrome_prime(1,200)
