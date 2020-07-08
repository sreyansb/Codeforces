for _ in range(int(input())):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    if 2*a<b:
        print(b*b)
    else:
        print(4*a*a)
