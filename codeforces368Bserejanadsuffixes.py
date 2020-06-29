#DYNAMIC PROGRAMMING IMPORTANT PROBLEM
n,m=map(int,input().split())
a=list(map(int,input().split()))
k=[0]*n
p=[0]*(10**5+1)
k[n-1]=1
p[a[n-1]]=1
for  i in range(n-2,-1,-1):
    if p[a[i]]==0:
        k[i]=k[i+1]+1
        p[a[i]]=1
    else:
        k[i]=k[i+1]
    
for i in range(m):
    j=int(input())
    print(k[j-1])
    
    
