n=int(input())
a=list(map(int,input().split()))
a.sort()
maxd=a[-1]-a[0]
if maxd==0:
    countj=n*(n-1)//2
else:
    countj=0
s=sorted(set(a))
l=len(s)
for i in range(l//2):
    if s[l-1-i]-s[i]==maxd :
        countj+=a.count(s[l-1-i])*a.count(s[i])
print(maxd,countj)
    
    
