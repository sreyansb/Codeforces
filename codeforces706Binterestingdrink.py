import bisect
n=int(input())
s=list(map(int,input().split()))
s.sort()
for i in range(int(input())):
    k=int(input())
    count=bisect.bisect_right(s,k,0,n)
    print(count)
