#Perfect logic.But did not work because of some sort of slowness in python
def factors(n):
    l={1,n}
    step=2 if n%2==1 else 1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            l|={i,n//i}
    return l
n,x=map(int,input().split())
k=sorted(factors(n))

if x>len(k):
    print(-1)
else:
    print(k[x-1])
    



