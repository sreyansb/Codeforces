#had to go through the editorial
"""
import collections
n, q = map(int,input().split())
s = [int(i) for i in input().split()]
a = [int(input()) for _ in range(q)]
dic = [0] * 32
for key, val in collections.Counter(s).items():
    dic[key.bit_length()-1] = val
for s in a:
    ans = 0
    for i in range(31, -1, -1):
        count = min(s >> i, dic[i])
        ans += count
        s -= count << i
    print(ans if s==0 else -1)
"""
n,q=map(int,input().split())
a=list(map(int,input().split()))
li=[0]*32
for i in a:
    li[i.bit_length()-1]+=1
#print(li)
queries=[int(input()) for _ in range(q)]
for k in queries:
    ans=0
    for i in range(31,-1,-1):
        mini=min(k>>i,li[i])
        ans+=mini
        k-=mini<<i
    ans=ans if k==0 else -1
    print(ans)
    


    
    
