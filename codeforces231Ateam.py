n=int(input())
k=0
for i in range(n):
    l=input().split()
    cou=l.count('1')
    if cou>=2:
        k+=1
print(k)
    
