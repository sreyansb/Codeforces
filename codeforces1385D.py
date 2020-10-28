def solve(s,low,high,character):
    if low==high:
        return 1 if s[high]!=character else 0
    mid=(low+high)//2
    temp1,temp2=0,0
    for i in range(low,mid+1):
        temp1+=(s[i]!=character)
    for i in range(mid+1,high+1):
        temp2+=(s[i]!=character)
    temp1+=solve(s,mid+1,high,character+1)
    temp2+=solve(s,low,mid,character+1)
    return min(temp1,temp2)
           
for _ in range(int(input())):
    n=int(input())
    s=input()
    k=[ord(i) for i in s]
    print(solve(k,0,n-1,97))
