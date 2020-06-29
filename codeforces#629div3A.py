for _ in range(int(input())):
    a,b=map(int,input().split())
    sol1=a%b
    if sol1!=0:
        sol2=b-sol1
    else:
        sol2=0
    print(sol2)
    
