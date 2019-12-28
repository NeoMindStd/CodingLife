cp='!@#$%^&*()-+'
n=int(input())
s=input()
nc=sc=lc=cc=True
for c in s:
    if c in cp:cc=False
    elif ord('a')<=ord(c)<=ord('z'):sc=False
    elif ord('A')<=ord(c)<=ord('Z'):lc=False
    elif ord('0')<=ord(c)<=ord('9'):nc=False
r=0
for f in [nc,sc,lc,cc]:
    if f:r+=1
print(max(6-n,r))
