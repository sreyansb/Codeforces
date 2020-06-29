t=int(input())
sumx=0
sumy=0
sumz=0
for i in range(t):
    l=list(map(int,input().split()))
    sumx+=l[0]
    sumy+=l[1]
    sumz+=l[2]
if sumx==0 and sumy==0 and sumz==0:
    print("YES")
else:
    print("NO")
