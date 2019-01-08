n,q=map(int, input().split())
count=0
if q%2==1:
    last_even=q-1
else:
    last_odd=q-2
for i in range(n+1,q):
    if i%2==0:
    	if i!=last_even:
    		print(i,end=' ')
    	else:
        	print(i)
