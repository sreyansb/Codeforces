n=int(input())
times=list(map(int,input().split()))
times.sort()
su=0
count=0

for i in times:
    if su<=i:
        count+=1
        
        su+=i
    
print(count)
        
