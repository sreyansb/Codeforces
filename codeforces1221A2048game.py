for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    if 2048 in s:
            print("YES")
    else:
        s.sort()
        k=sum(s)
        if k<2048:
            print("NO")
        elif k==2048:
            print("YES")
        else:
            k=sum([i for i in s if i<2048])
            if k>2048:
                print("YES")
            else:
                print("NO")
            
            
        
    
