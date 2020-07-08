for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    last1=n-1
    numbers=1
    for i in range(n-1,-1,-1):
        if s[i]=='0':
            if last1-i>k:
                numbers+=1
                last1=i
        else:
            if last1-i<=k:
                numbers-=1
            last1=i
    print(numbers)

        
        
    
