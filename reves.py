s="we are in groot"
l=s.split()
l1=[]
for i in l:
    rev=i[::-1]
    l1.append(rev)
print(''.join(l1))


l=["AKASH","MOTHIT","IPSITA","RAJESH","ROCKY","JAGA","PUJA"]
d={}
for i in l:
    if i[0] not in d:
        d[i[0]]=1
    else:
        d[i[0]]=d[i[0]]+1
print(d)
