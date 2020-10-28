for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    back=n-1
    while(back>0 and a[back-1]>=a[back]):
        back-=1
    while(back>0 and a[back-1]<=a[back]):
        back-=1
    print(back)
            
        
