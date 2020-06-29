l=input().split()
n=int(l[0])
l=list(map(int,input().split()))
x=l[0]
m=1
for i in l[1:]:
    if i<l[m-1]:
        x+=(n+i-l[m-1])
        #print(n+i-l[m-1])
    elif i>l[m-1]:
        x+=(i-l[m-1])
        #print(i-l[m-1])
    elif i==l[m-1]:
        x+=0
        #print(x)
    m+=1
print(x-1)
    
