t=input().split()
n=int(t[0])
k=int(t[1])
d=input().split()
d=list(map(int,d))
l=[]
j=0
while(d):
    j=len(d)

    t=d[0]
    for m in d[1:]:
        if (t+m)%k==0 and (t,m) not in l:
            l.append((t,m))
            d.remove(m)
            break
    if j==len(d):
        break
    
    d.remove(t)
    
print(len(l)*2)        
            
            

    
            
