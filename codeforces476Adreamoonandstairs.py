a=input().split()
n=int(a[0])
m=int(a[1])
nos=0
if n<m:
    print(-1)
elif n==m:
    print(n)
else:
    nos=n//2+n%2
    while(nos%m!=0):
        nos+=1
    print(nos)
