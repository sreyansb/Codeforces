import math
n,m=map(int,input().split())
count=0
while(m!=n):
    if m>n:
        if n%2==0:
            n*=2
            count+=1
        else:
            n-=1
            count+=1
    else:
        n-=1
        count+=1
print(count)
    
