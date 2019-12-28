a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=map(int,input().split())
l=sorted([(a1-b1)**2+(a2-b2)**2,(b1-c1)**2+(b2-c2)**2,(c1-a1)**2+(c2-a2)**2])
if l[0]**.5+l[1]**.5<=l[2]**.5:r='X'
elif l[0]==l[2]:r='JungTriangle'
elif l[0]==l[1]or l[1]==l[2]:
    if l[2]<l[0]+l[1]:r='Yeahkak2Triangle'
    elif l[2]>l[0]+l[1]:r='Dunkak2Triangle'
    else:r='Jikkak2Triangle'
else:
    if l[2]<l[0]+l[1]:r='YeahkakTriangle'
    elif l[2]>l[0]+l[1]:r='DunkakTriangle'
    else:r='JikkakTriangle'
print(r)
