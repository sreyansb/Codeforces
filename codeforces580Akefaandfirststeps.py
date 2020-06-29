
t=int(input())
l=input().split()
l=list(map(int,l))
max1=0
max2=0
for i in range(0,len(l)-1):
    if l[i+1]>=l[i]:
            max2+=1
    else:
        max2=0
    max1=max(max1,max2)
max1=max1+1
print(max1)

            
