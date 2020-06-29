t=int(input())
l=list(map(int,input().split()))
toen=0
totcost=l[0]
for i in range(t-1):
    if toen+l[i]-l[i+1]<0:
        k=-1*(toen+l[i]-l[i+1])
        l[i]+=k
        totcost+=k
    toen+=l[i]-l[i+1]
print(totcost)
    
