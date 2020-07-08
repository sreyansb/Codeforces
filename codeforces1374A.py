for _ in range(int(input())):
    x,y,n=map(int,input().split())
    j=n//x
    if j*x+y>n:
        j=x*j-(x-y)
    elif j*x+y<=n:
        j=j*x+y
    print(j)
