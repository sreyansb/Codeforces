n,k=map(int,input().split())
a=list(map(int,input().split()))
cur=sum(a[0:k])
m=1
z=cur
for i in range(k,n):
    cur+=a[i]-a[i-k]
    if z>cur:
        z=cur
        m=i-k+2
        #print(z)
print(m)
    


"""
n,k=map(int,input().split())
a=list(map(int,input().split()))
x=0
res=sum(a[0:k])
j=0
m=1
for i in range(1,n-k+1):
    cursum=sum(a[i:i+k])
    #print(cursum,a[i:i+k])
    j+=1
    if min(res,cursum)!=res:
        m=i+1
        res=cursum
print(m)"""
