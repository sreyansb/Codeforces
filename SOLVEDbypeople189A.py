n,a,b,c=map(int,input().strip().split(' '))
dp=[0]*(n+1)

for i in range(1,n+1):
	x=y=z=-1
	if i>=a:
		x=dp[i-a]
	if i>=b:
		y=dp[i-b]
	if i>=c:
		z=dp[i-c]
	if x==-1 and y==-1 and z==-1:
		dp[i]=-1
	else:
		dp[i]=max(x,y,z)+1
print(dp[n])
