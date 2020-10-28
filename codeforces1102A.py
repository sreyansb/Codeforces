n=int(input())
sumi=(n*(n+1))>>1
if sumi&1:
    print(1)
else:
    print(0)
