a,b,c,d=sorted(map(int,input().split()))
s1=a+b
s2=b+c
if s1>c or s2>d:
    print("TRIANGLE")
elif s1==c or s2==d:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
