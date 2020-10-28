n,k=map(int,input().split())
a=list(map(int,input().split()))
di={}
for i in range(n):
    if a[i] not in di:
        di[a[i]]=[]
    di[a[i]].append(i)
group=0
flag=0
for i in di:
    if len(di[i])>k:
        flag=1
        break
    for j in di[i]:
        a[j]=group%k+1
        group=group%k+1
if flag:
    print("NO")
else:
    print("YES")
    print(*a)
