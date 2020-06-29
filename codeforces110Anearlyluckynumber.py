l=input()
fs=l.count('4')+l.count('7')
fs=str(fs)
if fs.count('4')+fs.count('7')==len(fs):
    print("YES")
else:
    print("NO")
