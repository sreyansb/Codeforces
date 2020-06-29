n=int(input())
k=list(map(int,input().split()))
a=[0]+k
for i in range(1,n+1):
    a[i]+=a[i-1]
k.sort()
k=[0]+k
for i in range(1,n+1):
    k[i]+=k[i-1]

for _ in range(int(input())):
    typa,l,r=map(int,input().split())
    if typa==1:
        print(a[r]-a[l-1])
    else:
        print(k[r]-k[l-1])
        
        
        
        
