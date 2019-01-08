n,q=map(int,input().split())
x=''

for i in range(n,q):
    tem=i
    res=0
    while tem:
        res=res+(tem%10)**3
        tem=tem//10
 
    if res==i:
        x=x+str(i)+' '

print(x.strip())
