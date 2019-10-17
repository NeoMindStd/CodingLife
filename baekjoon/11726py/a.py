s = [1, 2, 3]
for i in range(3, 1000):
    s.append(s[-2]+s[-1])
print(s[int(input())-1]%10007)
