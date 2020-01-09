l=map(int,input().split())
s=5000
for i in l:
    if i<2:s-=500
    elif i>2:s-=1000
    else:s-=800
print(s)
