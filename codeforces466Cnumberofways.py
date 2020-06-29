n=int(input())
a=list(map(int,input().split()))
for i in range(1,n):
    a[i]+=a[i-1]
x,answer=0,0
for i in range(n-1):
    if a[i]*3==a[n-1]*2:
        answer+=x
    if a[i]*3==a[n-1]:
        x+=1

print(answer)
        
    
