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

"""
#dp approach
n=int(input())
a=list(map(int,input().split()))
sequenceuptoi=[1]*n
maxs=1
for i in range(1,n):
    if a[i]>=a[i-1]:
        sequenceuptoi[i]=sequenceuptoi[i-1]+1
        maxs=max(maxs,sequenceuptoi[i])
print(maxs)
"""

            
