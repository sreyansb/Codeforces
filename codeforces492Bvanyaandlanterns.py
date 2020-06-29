s=input().split()
l=int(s[1])
n=list(map(int,input().split()))
n=sorted(n)
diff=[]
if len(n)==1:
        diff.append(max((l-n[0]),n[0]-0))
else:
    for i in range(0,len(n)):
        if i==0:
            if n[i]!=0:
                diff.append(n[i])
            else:
                diff.append((n[i+1]-n[i])/2)
        elif i==len(n)-1:
            if n[i]!=l:
                diff.append(l-n[i])
            else:
                diff.append((n[i]-n[i-1])/2)
        else:
            diff.append((n[i]-n[i-1])/2)
print("%0.9f"%max(diff))
        
        
