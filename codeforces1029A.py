n,k=map(int,input().split())
s=input()
i=1
j=s[0]
while(i<n and s[i]==j):
    i+=1
print(s+s[i-1:]*(k-1))
    

    
        
        
    
        
    
