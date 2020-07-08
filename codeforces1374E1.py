from math import inf
n,k=map(int,input().split())
dic={'11':[],'10':[],'01':[]}
for _ in range(n):
    a,b,c=input().split()
    a=int(a)
    if b=='1' or c=='1':
        dic[b+c].append(a)

dic['11'].sort()
dic['10'].sort()
dic['01'].sort()

sums={'11':[0],'10':[0],'01':[0]}
for i in dic:
    for j in dic[i]:
        sums[i].append(sums[i][-1]+j)
print(sums)

total=inf
for i in range(min(k+1,len(sums['11']))):
    number=k-i
    print(i,number)
    if number<len(sums['10']) and number<len(sums['01']):
            total=min(total,sums['11'][i]+sums['10'][number]+sums['01'][number])
            
if total==inf:
    print(-1)
else:
    print(total)
        
#wrong approach- you can optimise using prefix sum and it is not for sure that 11 will give the least
"""
if number>=k:
    total=sum(dic['11'][:k])
else:
    total=sum(dic['11'])

if number>=k:
    print(total)
    
else:
    diff=k-number
    if len(dic['01'])>=diff and len(dic['10'])>=diff:
        dic['01'].sort()
        dic['10'].sort()
        total+=sum(dic['01'][:diff])+sum(dic['10'][:diff])
        print(total)
    else:
        print(-1)
"""

    
