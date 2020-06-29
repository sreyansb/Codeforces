for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    visited=[0]*n
    a.sort()
    di={}
    for i in range(n):
        for j in range(i+1,n):
            if abs(a[i]-a[j])==1:
                if visited[j]==0:
                    di[j]=1
            else:
                visited[j]=1
                if i not in di:
                    di[i]=0
                di[i]+=1
    print(len(di))
                
                
