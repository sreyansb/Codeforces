n,k=map(int,input().split())
while(k):
    if n%10:
        n-=1
    else:
        n//=10
    k-=1
print(n)
