n=int(input())
a=list(map(int,input().split()))
#a.sort()-> we cannot sort because they want in same order
if n<=2:
    print(0)
else:
    ans=10**9+1
    for d1 in range(-1,2):
        for d2 in range(-1,2):
            count=0
            a1=a[0]+d1
            a2=a[1]+d2
            d=a2-a1
            for i in range(0,n):
                val=abs(a[i]-a1-i*d)
                if val<=1:
                    count+=val
                else:
                    count=10**9+1
                    break
            ans=min(ans,count)
    print(-1 if ans>10**9 else ans)
            
                
                
                
