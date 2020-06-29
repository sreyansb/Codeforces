l=list(map(int,input().split()))
m=l[0]
t=l[1]
n=list(map(int,input().split()))
l=[]
flag=0
i=0
while(i<m-1):
    i=i+n[i]
    l.append(i+1)
if t in l:
    print("YES")
else:
    print("NO")
