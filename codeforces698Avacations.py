dp=[[200 for i in range(3)]for j in range(100)]
n=int(input())
li=list(map(int,input().split()))
dp[0][0]=1
if li[0]==1 or li[0]==3:
    dp[0][1]=0
if li[0]==2 or li[0]==3:
    dp[0][2]=0
for i in range(1,n):
    dp[i][0]=1+min(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    if li[i]==1 or li[i]==3:
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])
    if li[i]==2 or li[i]==3:
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])
print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))

