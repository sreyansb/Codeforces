
#O(n^2) algo
n=int(input())

s=[int(i) for i in list(input())]
l=[[] for i in range(3)]
for i in range(n):
    l[s[i]].append(i)
n=n//3

while(len(l[0])!=len(l[1]) or len(l[1])!=len(l[2]) or len(l[0])!=len(l[2])):
    a=len(l[0])
    b=len(l[1])
    c=len(l[2])
    k=min(a,b,c)
    if k==a:
        if b>c:
            j=min(b-n,n-a)
            l[0].extend(l[1][:j])
            l[1]=l[1][j:]
        else:
            j=min(c-n,n-a)
            l[0].extend(l[2][:j])
            l[2]=l[2][j:]
    elif k==c:
        if a>b:
            j=min(a-n,n-c)
            l[2].extend(l[0][a-j:])
            l[0]=l[0][:a-j]
        else:
            j=min(b-n,n-c)
            l[2].extend(l[1][b-j:])
            l[1]=l[1][:b-j]
    else:
        if a>c:
            j=min(a-n,n-b)
            l[1].extend(l[0][a-j:])
            l[0]=l[0][:a-j]
        else:
            j=min(c-n,n-b)
            l[1].extend(l[2][:j])
            l[2]=l[2][j:]

for i in range(3):
    for j in l[i]:
        s[j]=i

print("".join([str(i) for i in s]))
