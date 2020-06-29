def findclosestprime(n):
    if n==4:
        return 3
    elif n==6:
        return 5
    else:
        return 7
t=int(input())
k=input()
k=k.strip("0")
s=1
finalres=[]
for i in k:
    j=int(i)
    if j==0 or j==1:
        continue
    if j==2 or j==3 or j==5 or j==7:
        finalres.append(j)
    else:
        l=findclosestprime(j)
        finalres.append(l)
        if j==9:
            j=72
        while(j%6==0):
            finalres.append(3)
            j=j//6
        while(j>1):
            finalres.append(2)
            j=j//2
print(*(sorted(finalres,reverse=True)),sep="")
        
    



    
    
    
    
    
    
