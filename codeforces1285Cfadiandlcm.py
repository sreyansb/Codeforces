import math
n=int(input())
s=(1,n)
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        k=n//i
        if (k*i)//math.gcd(i,k)==n:
            if k<s[1]:
                s=(i,k)
print(*s,end=" ")
            
        
