for _ in range(int(input())):
    n,k=map(int,input().split())
    totalcandies=(n//k)*k
    remainingcandies=n%k
    kby2=k//2
    if remainingcandies<=kby2:
        print(totalcandies+remainingcandies)
    else:
        print(totalcandies+kby2)
