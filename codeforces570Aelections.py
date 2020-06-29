n,m=map(int,input().split())
d=[0]*(n+1)
for i in range(m):
    inp=list(map(int,input().split()))
    s=inp.index(max(inp))
    d[s+1]+=1
print(d.index(max(d)))
