"""n,k=map(int,input().split())
b=list(map(int,input().split()))
j=b.copy()
s=sum(b)
for i in range(n-2):
    b[i+1]=max(k-b[i],k-b[i+2])
if s>=sum(b):
    print(0)
    print(*j)
else:
    print(sum(b)-s)
    print(*b)"""

n,k=map(int,input().split())
s=list(map(int,input().split()))
m=s.copy()
j=sum(s)
for i in range(1,n):
    s[i]=max(s[i],k-s[i-1])
if (sum(s)-j)>0:
    print(sum(s)-j)
    print(*s)
else:
    print(0)
    print(*m)
    

    
