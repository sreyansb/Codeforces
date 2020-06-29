s=input()
if ord(s[0])>96 and ord(s[0])<123:
    print(chr(ord(s[0])-32)+s[1:])
else:
    print(s)
