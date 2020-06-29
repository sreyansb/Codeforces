k=int(input())
m=list(map(int,input().split()))
m.sort(reverse=True)
if k==0:
        print(0)
else:
    sum1=0
    i=0
    while(sum1<k and i<len(m)):
        sum1+=m[i]
        i+=1
    if i==12 and sum(m)<k:
        print(-1)
    else:
        print(i)
