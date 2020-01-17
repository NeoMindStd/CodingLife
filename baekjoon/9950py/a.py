import sys;read=sys.stdin.readline
r=''
while True:
    l,w,a=map(int,read().split())
    if l==w==a==0:break
    elif l==0:l=a//w
    elif w==0:w=a//l
    else:a=w*l
    r+=f'{l} {w} {a}\n'
print(r)
