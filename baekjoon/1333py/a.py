n,l,d=map(int,input().split())
s=([False]*l+[True]*5)*n
t=0
while True:
    if t>=len(s):break
    elif s[t]:break
    else:t+=d
print(t)
