for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    di={}
    for i in range(n):
        if a[i] not in di:
            di[a[i]]=[]
        di[a[i]].append(i)
    flag="NO"
    for i in di:
        if len(di[i])>=3:
            flag="YES"
            break
    if flag=="NO":
        for i in di:
            if len(di[i])==2:
                if di[i][1]-di[i][0]>1:
                    flag="YES"
                    break
    print(flag)
                    
