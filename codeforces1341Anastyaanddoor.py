def findpeak(a,left,right):
    nofpeaks=0
    for i in range(left+1,right):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            nofpeaks+=1
    return nofpeaks

for _ in range(int(input())):
    maxi=-1
    posn=-1
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    values=[1]*n
    for i in range(n-k+1):
        maxii=findpeak(arr,i,i+k-1)
        if maxii>maxi:
            #print(maxii)
            maxi=maxii
            posn=i
    print(maxi+1,posn+1)
        
