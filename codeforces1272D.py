n=int(input())
a=list(map(int,input().split()))
lis=['0']*n
lis[0]='1'
positionsof0=[]
for i in range(1,n) :
    if a[i]>a[i-1]:
        lis[i]='1'
    else:
        lis[i]='0'
        positionsofzero.append(i)
for i in positionsofzero:
    if a[i-1]>a[i]:
        
    
        
        
    


    
    
    
