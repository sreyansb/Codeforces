"""z,o=map(int,input().split())
s=['1']*(z+o)
res=0
for i in range(2,len(s),3):
    if z>0:
        z-=1
        s[i]='0'
    elif z==0 and i-o<=2:
        break
    else:
        res=-1
if ('111' in "".join(s)) or (res==0 and z>1) :
    res=-1
elif res==0 and z==1:
    s[-1]='0'
if '00' in "".join(s):
    res=-1
if res==0:
    print("".join(s))
else:
    print(-1)"""
z,o=map(int,input().split())
if o<z-1 or o>(2*z+2):
    print(-1)
else:
    if z-1==o:
        print("0"+"10"*o)
    if z==o-1:
        print("01"*z+'1')
    else:
        while(o>0 and z>0):
            if o<2*z:
                print("10",end="")
                z-=1
                o-=1
            else:
                print("110",end="")
                z-=1
                o-=2
        print('1'*o)
            
        

    
    

    
