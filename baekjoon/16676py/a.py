n=input()
r=len(n)
s='1'*r
if n=='0':r=1
elif int(n)<int(s):r-=1
print(r)
