for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    """k=sum(a)
    z=(k+2)/n
    y=(k+1)/n
    if z==int(z) or y==int(y):
        print("YES")
    else:
        print("NO")"""
    l=[0,0]
    for i in range(n):
        l[a[i]%2]+=1
    if l[0]==n or l[1]==n:
        print("YES")
    else:
        print("NO")
        
        
        
