for _ in range(int(input())):
    k,n,a,b=map(int,input().split())
    if k>n*a:
        print( n)
    elif k<=n*b:
        print(-1)
    else:
        atmost=(k-b*n)/(a-b)
        if atmost==int(atmost):
            print(int(atmost)-1)
        else:
            print(int(atmost))
