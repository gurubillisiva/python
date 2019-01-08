n,q=map(int, input().split())
count=0
if q%2==0:
    q_odd=q-1
else:
    q_odd=q-2
for i in range(n+1,q):
    if i%2!=0:
    	if i!=q_odd:
    		print(i,end=' ')
    	else:
        	print(i)
