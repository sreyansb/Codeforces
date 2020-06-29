"""k=fi.copy()
k.sort()
di={}
li=[]
init=1
k1=0
no=1
for i in range(len(now)):
    if k1>=len(k):
        break
    if k[k1] in list(range(init,now[i]+init)):
        di[k[k1]]=no
        k1+=1
    init+=now[i]
    no+=1
for i in fi:
    print(di[i])"""
n=int(input())
now=list(map(int,input().split()))
input()
fi=list(map(int,input().split()))
k=[0]*sum(now)
start=0
m=1
for i in now:
    k[start:start+i]=[m]*i
    start+=i
    m+=1
for i in fi:
    print(k[i-1])


     
    
