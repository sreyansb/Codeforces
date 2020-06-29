input()
s=list(map(int,input().split()))
l=s
for i in s:
    if i==0:
        break
    else:
        l.append(1)
max1=0
max2=0
for i in range(0,len(l)-1):
    if l[i+1]==l[i] and l[i]==1:
            max2+=1
    else:
        max2=0
    max1=max(max1,max2)
max1=max1+1
if l.count(1)>0:
    print(max1)
else:
    print(0)
