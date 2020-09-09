trash_words = set(['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'])

s = input().split()
answer = s[0][0]

for word in s[1:]:
    if word in trash_words: continue
    answer += word[0]

print(answer.upper())
