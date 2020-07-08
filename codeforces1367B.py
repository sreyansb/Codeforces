for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    odisplaced=0
    edisplaced=0    
    for i in range(n):
        if i%2!=arr[i]%2:
            if i%2:
                odisplaced+=1
            else:
                edisplaced+=1
    #print(displaced)
    if odisplaced!=edisplaced:
        print(-1)
    else:
        print(odisplaced)
