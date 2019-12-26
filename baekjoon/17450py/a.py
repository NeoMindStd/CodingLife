l=[list(map(int,input().split()))for _ in range(3)]
l=list(map(lambda x:[x[1]*10/(x[0]*10-(500 if x[0]*10>=5000 else 0))],l))
l[0].append('S');l[1].append('N');l[2].append('U');
l.sort()
print(l[2][1])
