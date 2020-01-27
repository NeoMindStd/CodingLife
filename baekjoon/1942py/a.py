c=0
def f(a,b):
    global c
    if int(''.join(a))%3==0:c+=1
    a[2]='%02d'%((int(a[2])+1)%60)
    if a[2]=='00':
        a[1]='%02d'%((int(a[1])+1)%60)
        if a[1]=='00':a[0]='%02d'%((int(a[0])+1)%24)
for T in range(3):
    a,b=map(lambda x:x.split(':'),input().split())
    c=0
    while a[0]!=b[0]or a[1]!=b[1]or a[2]!=b[2]:f(a,b)
    f(a,b)
    print(c)
