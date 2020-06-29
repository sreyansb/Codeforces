def findpositions(a,n):
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            #print("s")
            return i
    if n==2:
        if a[0]>a[1]:
            return 0
    return -1
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    valid=list(map(int,input().split()))
    valid=[i-1 for i in valid]
    sol=0
    k=0
    while(1):
        k=findpositions(a,n)
        #print(k)
        if k==-1:
            break
        if k not in valid:
            sol=1
            break
        a[k],a[k+1]=a[k+1],a[k]
    #print(a)
    if sol:
        print("NO")
    else:
        print("YES")
      
    
    
