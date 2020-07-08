for _ in range(int(input())):
    n=int(input())
    a=[[1 for _ in range(n+1)] for _ in range(n+1)]
    #print(a)
    for i in range(n):
        a[i][:n]=list(map(int,input()))
    #print(a)
    flag=0
    for i in range(n):
        for j in range(n):
            if a[i][j]==0:
                continue
            else:
                if a[i][j+1]==0 and a[i+1][j]==0:
                    flag=1
                    break
    if flag:
        print("NO")
    else:
        print("YES")
    
