n=input()
flag=0
for i in range(len(n)):
    if flag==1:
        break
    if i+1<len(n):
        for j in range(i+1,len(n)):
            if flag==1:
                break
            if j+1<len(n):
                for k in range(j+1,len(n)):
                    s=int(n[i]+n[j]+n[k])
                    if s%8==0:
                        print("YES")
                        print(s)
                        flag=1
                        break
            if int(n[i]+n[j])%8==0 and flag!=1:
                flag=1
                print("YES")
                print(n[i]+n[j])
                break
    if int(n[i])%8==0 and flag!=1:
        print("YES")
        print(n[i])
        flag=1
        break
if flag==0:
    print("NO")
    
