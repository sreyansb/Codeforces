import math
x1,y1,x2,y2=map(int,input().split())
x3,x4,y3,y4=0,0,0,0
angle=0
sol=-1
sidex=int(abs(x2-x1))
sidey=int(abs(y2-y1))
if sidey==0 and sidex!=0:
    sol=0
    x3=x1
    x4=x2
    y3=y1+sidex
    y4=y2+sidex
    
elif sidex==0 and sidey!=0:
    sol=0
    x3=x1+sidey
    x4=x2+sidey
    y3=y1
    y4=y2
elif sidex!=0 and abs(sidey/sidex)==1:
    sol=0
    x3=x1
    x4=x2
    y3=y2
    y4=y1
if not((x3>-1001 and x3<1001) or (x4>-1001 and x4<1001) or (y3>-1001 and y3<1001) or (y4>-1001 and y4<1001)):
        sol=-1
if sol!=-1:
    print(x3,y3,x4,y4)
else:
    print(sol)
    
    
