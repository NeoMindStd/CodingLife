s1,s2=map(int,input().split())
f1=f2=True
for T1 in range(s1):
    a,c=map(int,input().split())
    if a!=c:f1=False;break;
for T2 in range(s2):
    a,c=map(int,input().split())
    if a!=c:f2=False;break;
if f1 and f2:print('Accepted')
elif f1:print('Why Wrong!!!')
else:print('Wrong Answer')
