s="MY NAME IS AKASH"
x=s.split()
y="AKASH"
for i in x:
    if i==y:
        b=i[::-1]
x.pop(3)
x.append(b)
b=" ".join(x)
print(s)
print(b)



s="we are in groot"
l=s.split()
l1=[]
for i in l:
    rev=i[::-1]
    l1.append(rev)
print(''.join(l1))




