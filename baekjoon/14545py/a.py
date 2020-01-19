l=[0]
for i in range(1,1000001):l.append(l[-1]+i*i)
for T in range(int(input())):
    print(l[int(input())])
