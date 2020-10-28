n=int(input())
a=list(map(int,input().split()))
di={}
for i in a:
    if i not in di:
        di[i]=0
    di[i]+=1
k=sorted(di,key=lambda x:di[x])
print(di[k[-1]])
