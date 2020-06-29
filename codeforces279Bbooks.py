#brute force solution can be that we start from 1 and continue till sum>time
#same thing for 2 and so on.=>O(n**2) solution
#implemented using 2 pointers.
#one slides through the entire list,others through the list as well.
#performed 2*n times
n,t=map(int,input().split())
a=list(map(int,input().split()))
sum1=0
maxbooks=0
p1=0
p2=0
while (p1<n and p2<n):
    if sum1+a[p2]>t:
        maxbooks=max(maxbooks,p2-p1)
        #very important step to prevent negatives from creeping up.
        #use max function
        sum1=max(0,sum1-a[p1])
        p1+=1
    else:
        sum1+=a[p2]
        p2+=1
    if p2<p1:
        p2=p1
    #print(p1,p2,sum1,maxbooks)
print(max(maxbooks,p2-p1))
        
        
    
    
    


