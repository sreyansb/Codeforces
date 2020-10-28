from heapq import *
for _ in range(int(input())):
    n=int(input())
    arr=[0]*n
    ranges=[(n,0,n-1)]
    heapify(ranges)
    number=1
    while(ranges):
        size,l,r=heappop(ranges)
        if (r-l+1)%2:
            mid=(l+r)//2
            arr[mid]=number
        else:
            mid=(l+r-1)//2
            arr[mid]=number
        if mid!=l:
            heappush(ranges,(n-mid+l,l,mid-1))
        if mid!=r:
            heappush(ranges,(n-r+mid,mid+1,r))
        number+=1
        print(ranges)
    print(*arr)
