"""DOESN'T WORK-MY APPROACH
input()
s=list(map(int,input().split()))
for i in s:
    nos=2
    if int(i**0.5)==i**0.5 and i!=1:
        i=i**0.5
        nos=3
        if i%6==1 or i%6==5 or i==2 or i==3:
            s=set(range(3,int(i**0.5)+1,2))
            k=0
            while(s):
                m=min(s)
                q=2
                for j in range(m,int(i**0.5),m*q):
                    s.discard(j)
                    print(s)
                if i%m==0:
                    nos+=1
                    break
        else:
            nos=4
        if nos==3:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")"""
n=10**6+1
k=[1]*n
l=set()
for i in range(2,n):
    if k[i]==1:
        l.add(i**2)
        for j in range(i,n,i):
            k[j]=0
print(l)
for i in list(map(int,input().split())):
    if i in l:
        print("YES")
    else:
        print("NO")
