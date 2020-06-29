n,d=map(int,input().split())
s=list(map(int,input().split()))
sumt=sum(s)+10*(len(s)-1)
if sumt>d:
    sol=-1
else:
    sol=(d-sum(s))//5
print(sol)
    
