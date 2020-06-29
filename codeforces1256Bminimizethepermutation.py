for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    li=list(range(1,n+1))
    k=n-1
    currentno=0
    swapped=[]
    while(k>0 and a!=li):
        if a[currentno:]:
            mini=min(a[currentno:])
            z=a.index(mini)
            if k>=z-currentno:
                noswaps=0
                for i in range(z,currentno,-1):
                    if (i,i-1) not in swapped:
                        a[i]=a[i-1]
                        swapped.append((i,i-1))
                        noswaps+=1
                    else:
                        k-=noswaps
                        a[z-noswaps]=mini
                        break
                #print(noswaps)
                if noswaps==z-currentno:
                    a[currentno]=mini
                    k-=z-currentno
            else:
                #print("this loop")
                noswaps=0
                for i in range(z,z-k,-1):
                    if (i,i-1) not in swapped:
                        a[i]=a[i-1]
                        swapped.append((i,i-1))
                        noswaps+=1
                    else:
                        k-=noswaps
                        a[z-noswaps]=mini
                        break
                if noswaps==k:
                        a[z-k]=mini
                        k=0
                #print(noswaps)
            currentno+=1
        else:
            break
        #print(a,k)
    print(*a)
    #print(swapped)
