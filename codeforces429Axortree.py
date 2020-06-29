def dfs(k,i):
    final1[i]^=1
    for a in k:
        for b in g[a] :
            if b>a:
                dfs(g[b],b)
            
            
        
n=int(input())
g=[[] for i in range(n)]
for i in range(n-1):
    x,y=map(int,input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)
#print(g)

init=list(map(int,input().split()))
final=list(map(int,input().split()))
final1=[init[i]^final[i] for i in range(n)]
cnt=0
for i in range(n):
    if final1[i]==1:
        cnt+=1
        dfs(g[i],i)
print(cnt,final1)
        

