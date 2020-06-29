l=input().split()
l=list(map(int,l))
n=l[0]
m=l[1]
a=l[2]
noft=1
i=1
'''if n*m>a*a:
    for i in range(a):
        if (n+i)%a==0:
            noft*=(n+i)//a
            break
    for i in range(a):
        if (m+i)%a==0:
            noft*=(m+i)//a
            break'''
if n*m>a*a:
    if n%a==0:
        noft*=(n//a)
    else:
        noft*=(n+a-(n%a))//a
    if m%a==0:
        noft*=(m//a)
    else:
        noft*=(m+a-(m%a))//a
    
    
print(noft)
    
            
            
    
