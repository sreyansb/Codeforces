n=int(input())
a=list(map(int,input().split()))
final=[]
for i in a:
    if i in final:
        final.remove(i)
        final.append(i)
    else:
        final.append(i)
print(len(final))
print(*final)
