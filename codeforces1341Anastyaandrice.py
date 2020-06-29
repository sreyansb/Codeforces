for _ in range(int(input())):
    n,a,b,c,d=map(int,input().split())
    flag=0
    for i in range(c-d,c+d+1):
        j=i/n
        if j>=a-b and j<=a+b:
                flag=1
                break
    if flag==0:
        print("No")
    else:
        print("Yes")
            
            
    
            
