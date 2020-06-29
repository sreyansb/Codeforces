for _ in range(int(input())):
    n,m,a,b,c=map(int,input().split())
    costs=list(map(int,input().split()))
    graph=[]*(n+1)
    for _1 in range(m+1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
