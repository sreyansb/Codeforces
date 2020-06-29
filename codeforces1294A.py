for _ in range(int(input())):
    li=list(map(int,input().split()))
    if sum(li)%3==0:
        k=sum(li)//3
        #important conditions
        if k>=li[0] and k>=li[1] and k>=li[2]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
