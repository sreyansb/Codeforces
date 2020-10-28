n,x,y=map(int,input().split())
a=list(map(int,input().split()))
if x>y:
    print(n)
else:
    no=0
    no1=0
    for i in a:
        if i<=x:
            if i+y>=x:
                no1+=1
            else:
                no+=1
    print(no+(no1+no1%2)>>1)
