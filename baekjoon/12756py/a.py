aa,ah=map(int,input().split())
ba,bh=map(int,input().split())
while min(ah,bh)>0:ah-=ba;bh-=aa
if max(ah,bh)<=0:print('DRAW')
elif ah>0:print('PLAYER A')
else:print('PLAYER B')
