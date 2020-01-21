w=list(map(int,input().split()))
print(*sorted([list(map(int,input().split()))for i in range(int(input()))],key=lambda x:abs(w[0]-x[0])+abs(w[1]-x[1]))[0])
