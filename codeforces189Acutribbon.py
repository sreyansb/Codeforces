s=list(map(int,input().split()))
n=s[0]
s=sorted(s[1:])
sums=[]
m=[]
no=0
for i in range(3):
    for j in range(i+1,3):
        sums.append(s[i]+s[j])
sums=sorted(sums)
k=n
#print(sums)
while(n>=min(sums)):
    if n>=sums[2]:
        n-=sums[2]
        no+=2
    elif n>=sums[1]:
        n-=sums[1]
        no+=2
    elif n>=sums[0]:
        n-=sums[0]
        no+=2
    #print(no)
m.append(no)
no=0
for i in sorted(s,reverse=True):
    j=k
    no=0
    if j>=i and i!=2:
        no+=j//i
        j%=i
    if j in s or j==1:
        m.append(no)
    print(no,i)
print(max(m))
