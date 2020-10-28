n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(1,n):
    a[i]+=a[i-1]
a=[0]+a
maxi=0
for i in range(1,n-k+2):#has to be n-k+2 and not n-k+1
    for j in range(i+k-1,n+1):
        maxi=max(maxi,(a[j]-a[i-1])/(j-i+1))
print(maxi)
        
        
