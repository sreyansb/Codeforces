#PLEASE READ THE CONSTRAINTS
n=int(input())
l=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
flag=0
for i in l:
    if i<=n:
        if n%i==0:
            print("YES")
            flag=1
            break
    else:
        break
if flag==0:
    print("NO")
    



        

        
