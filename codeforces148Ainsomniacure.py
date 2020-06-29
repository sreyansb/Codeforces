k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
e=[k,l,m,n]
i=0
e=sorted(e,reverse=True)
s=set(range(1,d+1))
while(i<4 and len(s)>e[-1]):
    s=s-set(range(e[i],d+1,e[i]))
    i+=1
if d==min(e):
    print(d)
else:
    print(d-len(s))

    
    
