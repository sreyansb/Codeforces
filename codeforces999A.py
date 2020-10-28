n,k=map(int,input().split())
a=list(map(int,input().split()))
front=0
back=n-1
number=0
while(front<=back):
    j=min(a[front],a[back])
    if j>k:
        break
    if j==a[front] and j==a[back] and front!=back:
        front+=1
        number+=2
        back-=1
    elif j==a[front]:
        front+=1
        number+=1
    else:
        back-=1
        number+=1
print(number)
    
