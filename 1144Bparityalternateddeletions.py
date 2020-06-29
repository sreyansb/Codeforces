n=int(input())
k=list(map(int,input().split()))
even=sorted([i for i in k if i%2==0],reverse=True)
odd=sorted([i for i in k if i%2==1],reverse=True)
sum1=0
if len(even)==len(odd) or len(even)-len(odd)==1:
    sum1=0
else:
    if len(even)>len(odd):
        sum1=sum(even[len(odd)+1:])
    else:
        sum1=sum(odd[len(even)+1:])
print(sum1)
    
        
