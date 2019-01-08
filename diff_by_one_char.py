a,b=input().split()
diff=0
for i in range(len(a)):
	if a[i]==b[i]:
		continue
	else:
		diff+=1
if diff==1:
	print('yes')
else:
	print('no')
