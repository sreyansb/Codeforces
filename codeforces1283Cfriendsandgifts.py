import random
n=int(input())
a=[0]+list(map(int,input().split()))
pres=[0]*(n+1)
posn0=[]
 
for i in range(1,n+1):
    pres[a[i]]=1
    if a[i]==0:
        posn0.append(i)
 
notpresent=[]
for i in range(1,n+1):
    if pres[i]==0:
        notpresent.append(i)
 
i=0
random.shuffle(notpresent)
random.shuffle(posn0)
 
while(i<len(notpresent)):
    a[posn0[i]]=notpresent[i]
    i+=1
 
shufflepairs=[]
 
for i in range(1,n+1):
    if i==a[i]:
        shufflepairs.append(i)
 
 
for i in range(0,len(shufflepairs),2):
        if i+1<len(shufflepairs):
            a[shufflepairs[i]],a[shufflepairs[i+1]]=(a[shufflepairs[i+1]],a[shufflepairs[i]])
            
        else:
            if notpresent[0]!=shufflepairs[-1]:
                a[posn0[0]],a[shufflepairs[-1]]=(a[shufflepairs[-1]],a[posn0[0]])
            else:
                a[posn0[1]],a[shufflepairs[-1]]=(a[shufflepairs[-1]],a[posn0[1]])
 
print(*a[1:])
        
        
    
