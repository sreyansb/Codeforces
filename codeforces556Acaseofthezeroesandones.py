"""very important problem wherein it is just to remove pairs of 01/10"""
input()
n=input()
if n.count('1')>=n.count('0'):
    print(n.count('1')-n.count('0'))
else:
    print(n.count('0')-n.count('1'))
