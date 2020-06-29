n,m,k=map(int,input().split())
a=[0]*(m+1)
for i in range(m+1):
    a[i]=int(input())
b=a[m]
nof=0
for i in a[:m]:
    
    z=bin(i^b)
    #print(z)
    if z.count('1')<=k:
        #print(i,bin(i),bin(b),z)
        nof+=1
print(nof)
