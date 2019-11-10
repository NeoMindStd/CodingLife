print(*sorted([(i,sum(map(int,input().split())))for i in range(1,6)],key=lambda x:x[1])[-1])
