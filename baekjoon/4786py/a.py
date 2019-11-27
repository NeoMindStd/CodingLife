import sys;read=sys.stdin.readline
l=[]
while True:
    t=float(read())
    if t==999:break
    else:l.append(t)
r=[]
for i in range(len(l)-1):r.append('%.2f' %(l[i+1]-l[i]))
print('\n'.join(r))
