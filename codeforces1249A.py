for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    sol=1
    for i in range(n):
        for j in range(i+1,n):
            if abs(a[i]-a[j])==1:
                sol=2
                break
        if sol==2:
            break
    print(sol)
            
                
                    
                
