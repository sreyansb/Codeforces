for _ in range(int(input())):
    n=int(input())
    l=d=-(10**5)
    r=u=(10**5)
    for i in range(n):
        a=list(map(int,input().split()))
        if a[2]==0:
            l=max(l,a[0])
        if a[3]==0:
            u=min(u,a[1])
        if a[4]==0:
            r=min(r,a[0])
        if a[5]==0:
            d=max(d,a[1])
    if l<=r and d<=u:
        print(1,r,u)
    else:
        print(0)
