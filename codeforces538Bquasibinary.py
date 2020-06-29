n=int(input())
sol=[]
while(n>0):
    N=n
    m=0
    p=1
    while(N):
        if N%10:
            m+=p
        N//=10
        p*=10
    sol.append(m)
    n-=m
print(len(sol))
print(*sol)
        
    

