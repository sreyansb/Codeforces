for _ in range(int(input())):
    nod=int(input())
    pos=33000
    n=input()
    k=n
    n=list(map(int,n))
    count1=0
    for i in range(nod):
        if n[i]%2:
            n[i]=1
            count1+=1
            pos=min(pos,i)
        else:
            n[i]=0
    if count1%2==0 and n[-1]==1:
        print(k)
    elif count1%2==1 and n[-1]==1:
        if pos!=nod-1:
            print((k[:pos]+k[pos+1:]).strip('0'))
        else:
            print(-1)
    elif count1%2==0 and n[-1]==0:
        while(len(n)>0 and n[-1]%2==0):
            n=n[:-1]
            k=k[:-1]
        if len(n)>0:
            print(k.strip('0'))
        else:
            print(-1)
    elif count1%2==1 and n[-1]==0:
        while(n[-1]==0):
            n=n[:-1]
            k=k[:-1]
        if len(n)==0:
            print(-1)
        else:
            flag=0
            for i in range(len(n)-1):
                if n[i]==1:
                    flag=1
                    print((k[:i]+k[i+1:]).strip('0'))
                    break
            if flag==0:
                print(-1)
            
                    
            
            
    
    
            
        
        
    
    
    
