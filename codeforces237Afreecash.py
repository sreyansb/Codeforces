s=[]
fnoc=1
noc=1
n=int(input())
prev=input()
for i in range(n-1):
    k=input()
    
    #k=str(int(k[:k.index(" ")])*60+int(k[k.index(" ")+1:]))
    if k==prev:
        noc+=1
    else:
        fnoc=max(noc,fnoc)
        noc=1
        prev=k
print(max(fnoc,noc))
        
        
        
    
