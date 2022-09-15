s='a3b2c1d4r1'
a=''
for i in s:
    if i.isalpha():
        x=i
    else:
        d=int(i)
        a=a+x*d
print(a)
