import math
r,x,y,x1,y1=map(int,input().split())
d=((x1-x)**2+(y1-y)**2)**0.5
angle=0
if x1-x==0:
    angle=math.pi/2
else:
    angle=math.atan((y1-y)/(x1-x))
if angle!=0:
    print(int(math.ceil(abs(d/(2*r)))))
else:
    print(abs(math.ceil((x1-x)/(2*r))))
