"""def dfs(arr,k,visited,n):
    for i in range(n):
        if arr[k][i]:
            if i in visited:
                return i+1
            else:
                visited.add(i)
                dfs(arr,s[i]-1,visited,n)
                
            
n=int(input())
matrix=[[0 for i in range(n)] for j in range(n)]
s=list(map(int,input().split()))
for i in range(n):
    matrix[i][s[i]-1]=1
for i in range(n):

    visited=set()
    for k in range(n):
        if matrix[i][k]:
            visited.add(k)
            print(dfs(matrix,k,visited,n),end=" ")
        if len(visited)>0:
            break
    visited=set()
    print(dfs(matrix,i,visited,n),end=" ")
"""
n=int(input())
s=list(map(int,input().split()))
def dfs(a):
    visited=[0]*n
    k=a
    while(visited[k]!=1):
        visited[k]=1
        k=s[k]
    return k
for i in range(n):
    s[i]-=1
for i in range(n):
    print(dfs(i)+1,end=" ")
        
