for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    odds=[]
    oddlen=0
    evens=[]
    evenlen=0
    for i in a:
        if i%2:
            oddlen+=1
            odds.append(i)
        else:
            evenlen+=1
            evens.append(i)
    if oddlen%2==0:
        print("YES")
    else:
        flag=1
        for i in odds:
            for j in evens:
                if abs(i-j)==1:
                    flag=0
                    break
        if flag:
            print("NO")
        else:
            print("YES")
