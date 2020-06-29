for i in range(int(input())):
    a,b=map(int,input().split())
    s=list(input())
    while(True):
        if '.'*a in s:
            s[s.index('.'):s.index('.')+a]='#'*a
            if '.'*b not in s:
                print("YES")
                break
            else:
                s[s.index('.'):s.index('.')+b]='#'*b
        else:
            print("NO")
            break
