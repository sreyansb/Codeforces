for _ in range(int(input())):
    x,y,z=map(int,input().split())
    a,b,c=-1,-1,-1
    if x==z and y<=x:
        b=x
        a,c=y,y
        print("YES")
        print(a,b,c)
    elif y==z and x<=y:
        c=z
        a,b=x,x
        print("YES")
        print(a,b,c)
    elif x==y and z<=x:
        a=x
        b,c=z,z
        print("YES")
        print(a,b,c)
    else:
        print("NO")
        
        
