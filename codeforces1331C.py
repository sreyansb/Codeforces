for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[0]*26
    s=input()
    valid=list(map(int,input().split()))
    valid.sort()
    count=[0]*n
    for i in valid:
        count[i-1]+=1
    for i in range(n-1,0,-1):
        count[i-1]+=count[i]
    for i in range(n):
        a[ord(s[i])-97]+=count[i]+1
    print(*a)
        
