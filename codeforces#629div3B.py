for _ in range(int(input())):
    n,k=map(int,input().split())
    init=["a"]*(n)
    i=1
    string=list(init)
    j=n-2
    while(j>=0):
        if k<=n-j-1:
            init[j]='b'
            init[n-k]='b'
            print("".join(init))
            break
        k-=n-j-1
        j-=1
            
        
    
    
