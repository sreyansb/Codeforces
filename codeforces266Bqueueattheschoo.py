s=input().split()
l=input()
for i in range(int(s[1])):
    k=""
    i=0
    while(i<len(l)):
        if i+1<len(l) and l[i]=='B' and l[i+1]=='G':
            k=k+"GB"
            i+=2
        else:
            k=k+l[i]
            i+=1
    l=k
print(l)
