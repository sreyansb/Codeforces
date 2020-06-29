def rec(m,n):
    if m<0 or n<0:
        return 0
    elif m==0 or n==0:
        return 1
    else:
        return 1+rec(min(m,n)+1,max(m,n)-2)
m,n=map(int,input().split())
temp=m
m=min(m,n)
if m!=temp:
    n=temp
print(rec(min(m,n)+1,max(m,n)-2))
#FIRST RECURSIVE SOLUTION EVER DEVELOPED BY ME

