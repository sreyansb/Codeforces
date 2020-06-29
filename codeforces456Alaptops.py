"""specs={}
sol="Poor Alex"
t=int(input())
for i in range(t):
   p,s=map(int,input().split())
   specs[i]=(p,s)
   #if p<s:
       sol="Happy Alex"
print(sol)
"""
# MY SOLUTION
specs={}
t=int(input())
for i in range(t):
   p,s=map(int,input().split())
   specs[i]=(p,s)
#z=sorted(specs,key=lambda i:specs[i][0])
flag=0
for i in range(1,t) :
        if (specs[i][0]>specs[i-1][0] and specs[i][1]<specs[i-1][1]) or (specs[i][0]<specs[i-1][0] and specs[i][1]>specs[i-1][1]):
            flag=1
            break
if flag:
    print("Happy Alex")
else:
    for k in range(2,i+1):
        
        if (specs[i][0]>specs[i-k][0] and specs[i][1]<specs[i-k][1]) or (specs[i][0]<specs[i-k][0] and specs[i][1]>specs[i-k][1]):
            flag=1
            break
    if flag:
            print("Happy Alex")
    else:
            print("Poor Alex")
