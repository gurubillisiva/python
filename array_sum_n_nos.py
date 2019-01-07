N,K=map(int,input().split())
arr=[]
summ=0
for i in range(0,N):
    a=int(input())
    arr.append(a)
for i in range(0,K):
    summ=summ+arr[i]
print(summ)
