n=int(input())
tem=n
res=0
while n:
	res=res+(n%10)**3
	n=n//10
if res==tem:
	print('yes')
else:
	print('no')
	
