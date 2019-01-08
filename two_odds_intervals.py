n,q=map(int, input().split())
count=0
for i in range(n+1,q):
    if i%2!=0:
        print(i,end=' ')
        count+=1
    if count==2:
        break
