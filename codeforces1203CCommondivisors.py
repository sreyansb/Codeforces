n=int(input())
s=list(map(int,input().split()))
import math
k=s[0]
for i in range(0,n):
    k=math.gcd(s[i],k)
nod={k,1}
for i in range(2,int(k**0.5)+1):
    if k%i==0:
        nod.add(i)
        nod.add(k//i)
print(len(nod))
    
