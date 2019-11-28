c=list(map(int,input().split(':')))
t=list(map(int,input().split(':')))
c=c[0]*3600+c[1]*60+c[2]
t=t[0]*3600+t[1]*60+t[2]
r=[0,0,0]
if c>=t:t+=86400
t-=c
r[0]='%02d'%(t//3600)
t%=3600
r[1]='%02d'%(t//60)
r[2]='%02d'%(t%60)
print(':'.join(r))
