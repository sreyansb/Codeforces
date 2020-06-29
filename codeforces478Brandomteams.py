n,k=map(int,input().split())
if n!=k:
    x=n//k
    minp0=x
    minpn=x
    if n-k*x>0:
        minp0+=1
    z=(minp0*(n-k*x)*(minp0-1)//2)+(minpn*(k-n+k*x)*(minpn-1)//2)
else:
    z=0
noma=(n-k+1)*(n-k)//2
print(z,noma)

    


    

    
    
