s = [1, 2, 4]
for i in range(3, 10):
    s.append(s[-3]+s[-2]+s[-1])
for _ in range(int(input())):
    print(s[int(input())-1])
