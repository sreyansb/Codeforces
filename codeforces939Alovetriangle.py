n=int(input())
a=[0]+list(map(int,input().split()))
flag=0
for i in range(1,n+1):
    if a[a[a[i]]]==i :
        flag=1
        print("YES")
        break
if flag==0:
    print("NO")
    
    
    
    
        
