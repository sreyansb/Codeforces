n=int(input())
s=list(input())
nost=0
for i in range(0,n,2):
    if s[i]==s[i+1] and s[i]=='a':
        s[i]='b'
        nost+=1
    elif s[i]==s[i+1] and s[i]=='b':
        s[i]='a'
        nost+=1
    
print(nost)
print("".join(s))
