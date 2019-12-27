w,h,n=map(int,input().split())
s=0
for i in range(n):
    x,y=map(int,input().split())
    if i==0:cx,cy=x,y
    dx,dy=cx-x,cy-y
    if dx*dy>0:s+=max(abs(dx),abs(dy))
    else:s+=abs(dx)+abs(dy)
    cx,cy=x,y
print(s)
