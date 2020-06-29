n,l,r=map(int,input().split())
s=[1]*n
k=s.copy()
m=s.copy()
for i in range(1,l):
    k[i-1]=2**i

for i in range(1,r):
    m[i:n]=[2**i]*(n-i)
print(sum(k),sum(m))
