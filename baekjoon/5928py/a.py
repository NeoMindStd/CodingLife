h,d,m=map(int,input().split())
t=h*1440+d*60+m-16511
print(-1 if t<0 else t)
