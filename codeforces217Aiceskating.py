"""n=int(input())
s=set()
for i in range(n):
    s.add(tuple(map(int,input().split())))
k=list(s)
s=set()
for i in range(len(k)):
    for j in range(len(k)):
        if k[i][0]==k[j][0] or k[i][1]==k[j][1]:
            continue
        else:
            if k[i][0]-k[j][0]!=0:
                s.add((abs(k[i][0]-k[j][0]),k[i][1]))
            elif k[i][1]-k[j][1]!=0:
                s.add((abs(k[i][0]-k[j][0]),abs(k[i][1]-k[j][1])))
print(len(s-set(k)))"""
def dfs(i,index,rs):
    i[-1]=rs
    for j in range(n):
        if g[j][-1]==-1 and (i[0]==g[j][0] or i[1]==g[j][1]):
            dfs(g[j],j,rs)
n=int(input())
res=-1
g=[]
for i in range(n):
    x,y=map(int,input().split())
    g.append([x,y,-1])
for i in range(n):
    if g[i][-1]==-1:
        res+=1
        dfs(g[i],i,res)
print(res)
