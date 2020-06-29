n,m=map(int,input().split())
cats=list(map(int,input().split()))
q=[[] for i in range(n)]
for i in range(n-1):
    x,y=map(int,input().split())
    q[x-1].append(y-1)
    q[y-1].append(x-1)
#0 is start_index,0 is the number of cats initially.
query=[(0,0)]
l=0
ans=0
visited=[0 for i in range(n)]
while(l<len(query)):
    current_index,nofcatstillnow=query[l]
    visited[current_index]=1
    if nofcatstillnow+cats[current_index]<=m:
        isLeaf=True
        for i in q[current_index]:
            if visited[i]==0:
                isLeaf=False
                query.append((i,cats[current_index]*(cats[current_index]+nofcatsforthegivenvertex)))
        if isLeaf:
            ans+=1
    l+=1
print(ans)
            
        
