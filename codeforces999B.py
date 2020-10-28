n=int(input())
s=list(input())
divisors=[1,n]
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        divisors+=[i,n//i]
if n**0.5==int(n**0.5):
    divisors.pop()
divisors.sort()
for i in divisors:
    s[:i]=s[:i][::-1]
print("".join(s))
