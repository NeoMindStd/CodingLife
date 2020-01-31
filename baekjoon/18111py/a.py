import sys;read=sys.stdin.readline
n,m,b=map(int,read().split())
l,m=[],257
for _ in range(n):
    l.append(list(map(int,read().split())))
    m=min(m,min(l[-1]))
height,time=256,128000000
for h in range(m,257):
    t,blocks=0,b
    for row in l:
        for col in row:
            if col>h:
                t+=(col-h)*2
                blocks+=col-h
            elif col<h:
                t+=h-col
                blocks-=h-col
    if blocks<0:break
    if time>=t:time,height=t,h
print(time,height)
