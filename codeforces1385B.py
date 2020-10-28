for _ in range(int(input())):
    n=int(input())
    visited=[0]*(n+1)
    a=list(map(int,input().split()))
    final=[]
    for i in a:
        if visited[i]:
            continue
        else:
            final.append(i)
            visited[i]=1
    print(*final)
