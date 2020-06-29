for _ in range(int(input())):
    n=int(input())
    cost=0
    while(n>9):
        cost+=n-n%10
        k=n%10
        n=n//10+k
    cost+=n
    print(cost)
        
    
        
    
        
