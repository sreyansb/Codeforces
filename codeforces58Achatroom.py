s=input()
h=s.find('h')
e=s[h+1:].find('e')
s=s[h+1:]
l1=s[e+1:].find('l')
s=s[e+1:]
l2=s[l1+1:].find('l')
s=s[l1+1:]
o=s[l2+1:].find('o')

if h>=0 and e>=0 and l1>=0 and l2>=0 and o>=0:
    print("YES")
else:
    print("NO")
