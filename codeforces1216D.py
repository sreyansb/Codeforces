#had to go through the editorial
from math import gcd
n=int(input())
a=list(map(int,input().split()))
if n==1:
    print(0,0)
elif n==2:
    if max(a)-min(a):
        print(1,max(a)-min(a))
    else:
        print(0,0)
else:
    b=max(a)
    s=b*n
    f=s-sum(a)
    gm=b-a[0]
    for i in range(1,n):
        gm=gcd(gm,b-a[i])
    print(f//gm,gm)
    """
    a.sort()
    i=0
    while(i<n and (a[i]==0 or f%a[i]!=0)):
        i+=1
    if i<n:
        i=a[i]
    else:
        i=0
    if i==0:
        print(0,0)
    else:
        print(f//i,i)
    """
