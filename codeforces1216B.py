n=int(input())
li=list(map(int,input().split()))
li=[(li[i],i+1) for i in range(n)]
li=sorted(li,key=lambda x:x[0],reverse=True)
sol=0
for i in range(n):
    sol+=li[i][0]*i+1
print(sol)
for i in li:
    print(i[1],end=" ")
print()
    
    
