s=input().split("+")
s=sorted(list(map(int,s)))
for i in s[:-1]:
    print(i,end="+")
print(s[-1])
