m=int(input())
boys=list(map(int,input().split()))
n=int(input())
girls=list(map(int,input().split()))
nop=0
boys.sort()
girls.sort()
if m>=n:
    morepeople=boys
    lesspeople=girls
else:
    morepeople=girls
    lesspeople=boys

for i in lesspeople:
    if (i-1) in morepeople:
        nop+=1
        morepeople.remove(i-1)
    elif (i) in morepeople:
        nop+=1
        morepeople.remove(i)
    elif (i+1) in morepeople:
        nop+=1
        morepeople.remove(i+1)
print(nop)
    
