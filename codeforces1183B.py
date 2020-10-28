for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    #max value that can be obtained a[0]+k
    #min value i.e. a[-1]-k has to be greater than this
    if a[0]+k>=a[-1]-k:
        print(a[0]+k)
    else:
        print(-1)
    
