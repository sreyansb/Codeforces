n=int(input())
coins=[100,20,10,5,1]
i=0
noc=0
while(n):
    if n>=coins[i]:
        noc+=n//coins[i]
        n=n%coins[i]
    i+=1
print(noc)
        
        

    
