z=input()
res=''
a=z.lower().split()
for i in a:
    temp=i
    for j in range(0,len(temp)):
        if j==0:
            res=res+temp[j].upper()
        else:
            res=res+temp[j]
    res=res+' '
print(res.strip())
