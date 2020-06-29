s=input().split()
n=int(s[0])
t=int(s[1])
s=int("1"+("0"*(n-1)))
if t>=int("1"+("0"*(n))):
    print(-1)
else:
    k=s+t-(s%t)
    print(k)

