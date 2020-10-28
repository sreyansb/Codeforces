from bisect import bisect_left
n,k=map(int,input().split())
a=list(map(int,input().split()))
que=list(map(int,input().split()))
a=[0]+a
for j in range(1,n+1):
    a[j]=a[j]+a[j-1]
for i in que:
    k=bisect_left(a,i)
    print(k,i-a[k-1])
    
        
    
