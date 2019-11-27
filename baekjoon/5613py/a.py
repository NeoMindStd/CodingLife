i=a=0
o='+'
while True:
    t=input()
    if t=='=':break
    if i%2==0:
        t=int(t)
        if o=='+':a+=t
        if o=='-':a-=t
        if o=='*':a*=t
        if o=='/':a//=t
    else:o=t
    i+=1
print(a)
