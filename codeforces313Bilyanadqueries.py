s=input()
a=[0]*(len(s)+1)
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        a[i+1]=a[i]+1
    else:
        a[i+1]=a[i]
m=int(input())
for i in range(m):
    l,b=map(int,input().split())
    print(a[b]-a[l])
