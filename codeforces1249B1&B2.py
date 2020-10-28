#B2
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sol=[1]*n
    for i in range(n):
        if a[i]==i+1:
            continue
        k=a[i]-1
        every=[k]
        nosteps=1
        while(k!=i):
            k=a[k]-1
            nosteps+=1
            every.append(k)
        
        for j in every:
            a[j]=j+1
            sol[j]=nosteps
        
    print(*sol)

#B1
'''
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sol=[1]*n
    for i in range(n):
        k=a[i]-1
        nosteps=1
        while(k!=i):
            k=a[k]-1
            nosteps+=1
        sol[i]=nosteps
    print(*sol)
'''          
        
