a=list(map(int,input().split()))
b=list(map(int,input().split()))
f=True
for i in range(5):
    if a[i]==b[i]:f=False;break
print('Y'if f else'N')
