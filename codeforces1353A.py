from math import ceil
for _ in range(int(input())):
    n,m=map(int,input().split())
    if n==1:
        print(0)
    else:
        print(ceil((n-1)/(n//2))*m)
        
    
        
