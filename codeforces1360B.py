for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    mini=10000
    for i in range(n):
        mini=min(mini,abs(a[i-1]-a[i]))
    print(mini)
    
