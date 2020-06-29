import math
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sumi=[a[i]-b[i] for i in range(n)]
sump=0
pos=[]
neg=[]
sumn=0
sumi.sort()

for i in range(n):
    if sumi[i]>=0:
        sump+=1
        pos.append(sumi[i])
    else:
        sumn+=1
        neg.append(sumi[i])
nos=sump*(sump-1)//2

least_negative=neg[0]
i=0
while(i<sump):
    if pos[i]+least_negative>0:
        break
    i+=1
nos+=(sump-i)*sumn



    
    
    
    
    
    

