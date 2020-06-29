t=int(input())
for i in range(t):
    l=input().split()
    if int(l[0])-int(l[1])==1:
        flag=0
        for j in range(2,int(pow((int(l[0])+int(l[1])),0.5))+1):
            if (int(l[0])+int(l[1]))%j==0:
                flag=1
                break
        if flag==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
                
            
                       
        
