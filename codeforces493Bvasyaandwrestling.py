#USED TWO POINTERS WHEN SUMFIRST!=SUMSECOND
first=[]
second=[]
last=0
for i in range(int(input())):
    k=int(input())
    if k>0:
        first.append(k)
    elif k<0:
        second.append(-k)
    last=k
sumfirst=sum(first)
sumsecond=sum(second)
if sumfirst!=sumsecond:
    if sumfirst>sumsecond:
        print("first")
    else:
        print("second")
else:
    i=0
    j=0
    fi=len(first)
    se=len(second)
    while(i<fi and j<se and first[i]==second[j]):
        i+=1
        j+=1
    if (i!=fi and j!=se):
        if first[i]>second[j]:
            print("first")
        if first[i]<second[j]:
            print("second")
    elif fi!=se:
        if fi>se:
            print("first")
        else:
            print("second")
    else:
        if last<0:
            print("second")
        else:
            print("first")
            
        
