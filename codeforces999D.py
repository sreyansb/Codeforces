n,m=map(int,input().split())
a=list(map(int,input().split()))
summ=sum(a)
k=[[[],0] for i in range(m)]
for i in range(n):
    k[a[i]%m][0].append(i)
    k[a[i]%m][1]+=1
#print(k)
j=0
l=n//m
for i in range(m):
    while(k[i][1]>l):
        while(j<i or k[j%m][1]>=l):
            j+=1
        z=k[i][0].pop()
        k[i][1]-=1
        a[z]+=(j-i)%m
        k[j%m][0].append(z)
        k[j%m][1]+=1
print(sum(a)-summ)
print(*a)

