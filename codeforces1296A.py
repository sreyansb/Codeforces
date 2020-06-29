for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    posi=[0,0]
    for i in a:
        if i&1==0:
            posi[0]+=1
        else:
            posi[1]+=1
    if posi[0]!=0 and posi[1]!=0:
        print("YES")
    else:
        if posi[1]!=0:
            if n%2==1:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
        
