for i in range(int(input())):
    sol=0
    s=list(map(int,input().split()))
    if sum(s)>=3:
        sol=min(min(s[0],s[1])*3,sum(s))//3
    print(sol)
        
