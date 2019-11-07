birth,now=list(map(int,input().split())),list(map(int,input().split()))
print(*[now[0]-birth[0]-(1 if now[1:3]<birth[1:3] else 0),now[0]-birth[0]+1,now[0]-birth[0]],sep='\n')
