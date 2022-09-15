def check_prime_no(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")   
lower = int(input("enter 1st Number: "))
upper = int(input("enter 2nd Number: "))
print("Prime numbers between", lower, "To", upper, "are: ")
for i in range(lower, upper + 1):
   check_prime_no(i)

