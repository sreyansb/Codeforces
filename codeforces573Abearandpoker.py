import math
n=int(input())
a=list(set(map(int,input().split())))
lcm=a[0]
f1=0
while lcm%2==0:
    lcm/=2
while lcm%3==0:
    lcm/=3
for i in a[1:]:
    while i%2==0:
        i/=2
    while i%3==0:
        i/=3
    if i!=lcm:
        f1=1
        break
  
"""
for i in a:
    k=lcm/i
    if k%6==0:
        continue
    z=math.log(k)/math.log(2)
    d=math.log(k)/math.log(3)
    if z==int(z) or d==int(d):
        continue
    else:
        fl=1
        break
"""    
if f1:
    print("NO")
else:
    print("YES")
