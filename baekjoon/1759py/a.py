l, c = map(int, input().split())
chars = input().split()
chars.sort()
keys = []

for i in range(c-3):
    for j in range(i+1, c-2):
        for k in range(j+1, c-1):
            for l in range(k+1, c):
                keys.append(chars[i]+chars[j]+chars[k]+chars[l])

answers = []
for key in keys:
    cnt = 0
    for char in key:
        if char in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    if cnt >= 1 and cnt < 3:
        answers.append(key)

for answer in answers:
    print(answer)
            
