n=int(input())
a=list(map(int,input().split()))
mappedlist=[0]*(n+2)
a.sort()
minimum=0
for i in list(set(a)):
    if mappedlist[i-1] or mappedlist[i] or mappedlist[i+1]:
        pass
    else:
        minimum+=1
        mappedlist[i]=1
    
