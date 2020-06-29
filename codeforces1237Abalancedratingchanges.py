import math
li=[]
lodd=[]
n=int(input())
for i in range(n):
    li.append(int(input()))
for i in range(n):
    if li[i]%2==0:
        li[i]=li[i]//2
    else:
        lodd.append((li[i],i))
lodd=sorted(lodd,key=lambda x:x[0])
k=len(lodd)
for i in range(k//2):
    li[lodd[i][1]]=math.floor(lodd[i][0]/2)
    li[lodd[k-1-i][1]]=math.ceil(lodd[k-1-i][0]/2)
for i in li:
    print(i)

        
    
        

    
