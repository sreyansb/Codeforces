m=list(map(int,input().split()))
if sum(m)%len(m)==0 and sum(m)!=0:
    print(sum(m)//len(m))
else:
    print(-1)
