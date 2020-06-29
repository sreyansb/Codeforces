n,k=map(int,input().split())
j=100001
modder=1000000007
a=[1]*(j)
for i in range(k,j):
    #Without modder we get memory error
    a[i]=(a[i-1]+a[i-k])%modder
for i in range(1,j):
    #Without modder we get memory error
    a[i]=(a[i]+a[i-1])%modder
for _ in range(n):
    l,r=map(int,input().split())
    print((a[r]-a[l-1])%modder)
