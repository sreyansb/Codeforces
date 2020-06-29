import math
n,x1,y1=map(int,input().split())
s=set()
for _ in range(n):
    x2,y2=map(int,input().split())
    if x2-x1==0:
        s.add(math.inf)
    else:
        s.add((y2-y1)/(x2-x1))
print(len(s))
    
    
