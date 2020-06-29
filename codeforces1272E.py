n=int(input())
a=list(map(int,input().split()))
positions=[-1]*n
for i in range(n):
    if i-a[i]<0 and i+a[i]>n-1:
        positions[i]=-1
    elif i-a[i]<0:
        if (positions[i+a[i]]+positions[i])%2:
            positions[i]=i+a[i]
    elif i+a[i]>n-1:
        if (positions[i-a[i]]+positions[i])%2:
         positions[i]=i-a[i]
    elif i-a[i]>=0 and i+a[i]<n:
        positions[i]=min(positions[i-a[i]],positions[i+a[i]])
print(*positions)
        
