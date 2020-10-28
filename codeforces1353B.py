for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    i=0
    j=0
    noswaps=0
    while(i<n and j<n and noswaps<k):
        if b[j]>a[i]:
            a[i]=b[j]
            i+=1
            j+=1
            noswaps+=1
        else:
            break
    print(sum(a))
    
    
