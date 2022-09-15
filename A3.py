s=["AKASH","ASHU","SABITA","SANU","BIKAST","ANKITA"]
d={}
for i in s:
    if i[0] not in d:
        d[i[0]]=1
    else:
        d[i[0]]=d[i[0]]+1
print(d)
