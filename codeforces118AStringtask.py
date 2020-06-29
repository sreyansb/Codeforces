k=input()
l=['a','e','i','o','u','y','A','E','I','O','U','Y']

m=""
for i in k:
    if i not in l:
        if ord(i)>64 and ord(i)<91:
            m=m+"."+chr(ord(i)+32)
        else:
            m=m+"."+chr(ord(i))
print(m)
