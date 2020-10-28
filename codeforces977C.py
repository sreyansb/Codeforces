n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

flag=0

if k==0:
    ans=a[0]-1
else:
    ans=a[k-1]
    
for i in range(n):
    if a[i]<=ans:
        flag+=1
        
if flag==k and ans>0 and ans<10**9+1:
    print(ans)
else:
    print(-1)
