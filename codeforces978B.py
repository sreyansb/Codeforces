n=int(input())
a=input()
number=0
i=0
while(i<n):
    if a[i]!='x':
        i+=1
        continue
    count=1
    for j in range(i+1,n):
        if a[j]=='x':
            count+=1
        else:
            break
    if count>=3:
        number+=count-2
    i+=count
print(number)
        
