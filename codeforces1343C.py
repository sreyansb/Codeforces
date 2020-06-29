def findsign(x):
    if x>0:
        return 1
    return 0
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sumi=0
    i=0
    while(i<n):
        maxi=a[i]
        j=i+1
        while(j<n and findsign(a[i])==findsign(a[j])):
            maxi=max(maxi,a[j])
            j+=1
        i=j
        sumi+=maxi
        #print(i)
    print(sumi)
        
    
