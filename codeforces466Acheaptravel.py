n,m,a,b=map(int,input().split())
if b/m<=a:
    if n<m:
        cost=min(b,n*a)
    else:
        cost=(n//m)*b+min(b,(n%m)*a)
else:
    cost=n*a
print(cost)
