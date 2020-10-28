for _ in range(int(input())):
    n=int(input())
    c=1
    a=[]
    while(c<n):
        a.append(c)
        c*=3
    if c==n:
        print(n)
    else:
        k=sum(a)
        if k==n:
            print(k)
        elif k>n:
            for i in a[::-1]:
                if k-i>=n:
                    k-=i
            print(k)
        else:
            print(c)
        
        
        
        
        
    
    '''
    ans=3**(ceil(log3(n)))
    if ans==n:
        print(ans)
    else:
    '''
        
    
    
