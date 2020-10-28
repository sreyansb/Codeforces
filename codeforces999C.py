from heapq import heappush,heappop,heapify
n,k=map(int,input().split())
s=input()
di=[[] for i in range(26)]
for i in range(n):
    heappush(di[ord(s[i])-97],i)
j=0
flag=0
s=list(s)
while(j<k):
    if di[flag]:
        m=heappop(di[flag])
        s[m]=""
        j+=1
    else:
        flag+=1
print("".join(s))
        
    
    
