"""input()
s=set(map(int,input().split()))
aver=sum(s)/len(s)
if aver==sum(s)//len(s):
        print(sum(s)//len(s)-min(s))
elif len(s)==2:
    print(max(s)-min(s))
else:
    print(-1)"""
n=int(input())
s=list(map(int,input().split()))
s=sorted(set(s))
k=set()
if len(s)>3:
    print(-1)
else:
    if len(s)==1:
        print(0)
    elif len(s)==2:
        j=s[1]-s[0]
        if j%2:
            print(j)
        else:
            print(j//2)
    elif len(s)==3:
        if (s[2]+s[0])/2==s[1]:
            print(s[1]-s[0])
        else:
            print(-1)

    
