for _ in range(int(input())):
    n=int(input())
    s=input()
    a=[0]*n
    b=[0]*n
    j=0
    for i in range(n):
        if s[i]=='2' and j==0:
            a[i]='1'
            b[i]='1'
        elif s[i]=='2' and j==1:
            a[i]='0'
            b[i]='2'
        elif s[i]=='0':
            a[i]='0'
            b[i]='0'
        else:
            if j==0:
                a[i]='1'
                b[i]='0'
                j=1
            else:
                a[i]='0'
                b[i]='1'
    print("".join(a))
    print("".join(b))
            
            
