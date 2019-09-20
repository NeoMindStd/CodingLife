mushrooms = [int(input()) for _ in range(10)]
s = [-100]
for i in range(1, 11):
    s.append(sum(mushrooms[0:i]))
for i in range(1, 11):
    if s[i] >= 100 or i == 10:
        print(s[i] if (s[i]-100)**2 <= (s[i-1]-100)**2 else s[i-1])
        break
