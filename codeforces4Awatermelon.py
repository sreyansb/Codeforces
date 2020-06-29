n=int(input())
flag=0
for i in range(2,n,2):
    if (n-i)%2==0:
        print("YES")
        flag=1
        break
if flag==0:
    print("NO")
    
