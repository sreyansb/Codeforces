def intersection(a,b):
    return [max(a[0],b[0]),max(a[1],b[1]),min(a[2],b[2]),min(a[3],b[3])]
def area(a):
    return max(a[2]-a[0],0)*max(a[3]-a[1],0)#because we have assumed from
#intersection we will get a[2]>a[0]
w=list(map(int,input().split()))
b1=list(map(int,input().split()))
b2=list(map(int,input().split()))
d=area(intersection(w,b1))
e=area(intersection(w,b2))
g=area(intersection(b1,b2))
if d+e-g==area(w):
    print("NO")
else:
    print("YES")
    
