for i in range(int(input())):
    s,i,e=map(int,input().split())
    m=max(0,(e+i-s+2)//2)
    print(max(0,e-m+1))
        
        
    """if diff==0:
        print(e-e//2)
    elif diff<0:
        if e+diff>0:
            if diff>2*(e//2)-e:
                print(2*(e//2)+diff-1)
            else:
                print(2*(e//2)+diff-diff%2)
        else:
            print(0)
    else:
        e=e+diff
        print(e+1-m)5"""
        
        
    """
    if abs(diff)>=e and diff<=0:
        print (0)
    else:
        if e%2:
            diff+=1
        if diff<=0:
            j=((diff*-1)//2)
            print(e//2+j)
        else:
            print(e-e//2+1)"""
            
