for _ in range(int(input())):
    number=97
    n,a,b=map(int,input().split())
    listy=['a']*n
    numb=0
    for i in range(n):
        listy[i]=chr(number+numb%b)
        numb+=1
    print(*listy,sep="")
            
        
            
                
            
        
    
    
        
