n = int(input())
scores = {'Adrian':[0,'ABC'], 'Bruno': [0,'BABC'], 'Goran': [0,'CCAABB']}
s = input()

for i in range(n):
    for score in scores.values():
        if score[1][i%len(score[1])] == s[i]: score[0]+=1

m=max(scores.values())[0]
print(m)
print(*map(lambda x: x[0],filter(lambda x: x[1][0]>=m, scores.items())),sep='\n')
