for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    p=0
    pos=[]
    for i in range(n):
        if a[i]&1:
            p+=1
            pos.append(i+1)
    if p<k:
        print("NO")
    elif p>=k:
        if (p-k)&1:
            print("NO")
        else:
            pos[k-1]=n
            print("YES")
            print(*pos[:k])
                
            
        
    
        
    
    
    
