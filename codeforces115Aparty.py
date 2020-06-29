"""n=int(input())
d1=int(input())
d_ones={1:{-1}}
for i in range(2,n+1):
    k=int(input())
    if k==-1:
        d_ones[i]={-1}
    else:
        p=i-1
        while(p>=0):
            if p in d_ones and p<=k:
                d_ones[p]=d_ones[p]|{k}
                break
            p-=1
maxh=-4
for i in d_ones:
    if maxh<=len(d_ones[i]):
        maxh=len(d_ones[i])
print(maxh)"""
n=int(input())
k=[int(input()) for i in range(n)]
r=0
i=0
for i in range(n):
    c=0
    while(i>=0):
        i=k[i]-1
        c+=1
    r=max(r,c)
print(r)
    
    
