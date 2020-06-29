"""important solution it is"""
s=input()
if len(s)==1 and s.islower():
    s=s.upper()
elif s.isupper()!=0:
    s=s.lower()
elif s[0].isupper()==0 and s[1:].isupper()!=0:
    s=s[0].upper()+s[1:].lower()
print(s)
