def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
if n<3:
    print(n)
elif n%2:
    print(n*(n-1)*(n-2))
else:
    if n%6!=0:
        print(n*(n-1)*(n-3))
    else:
        print((n-1)*(n-2)*(n-3))
