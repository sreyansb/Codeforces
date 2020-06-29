n=int(input())
s=list(map(int,input().split()))
totalamount={'25':0,'50':0,'100':0}
if s[0]!=25:
    print("NO")
else:
    totalamount['25']+=1
    flag=0
    for i in range(1,n):
        if s[i]==25:
            totalamount['25']+=1
        elif s[i]==50:
            if totalamount['25']>0:
                totalamount['25']-=1
                totalamount['50']+=1
            else:
                flag=1
                print("NO")
                break
        elif s[i]==100:
            if (totalamount['25']>0 and totalamount['50']>0):
                totalamount['25']-=1
                totalamount['50']-=1
                totalamount['100']+=1
            elif totalamount['25']>2:
                totalamount['25']-=3
            else:
                flag=1
                print("NO")
                break

    if flag!=1:
        print("YES")
