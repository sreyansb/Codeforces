for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif a<b:
        if (b-a)&1==0:
            print(2)
        else:
            print(1)
    else:
        if (a-b)&1==0:
            print(1)
        else:
            print(2)
        
