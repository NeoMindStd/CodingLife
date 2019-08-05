s = input()
word = input()
cnt = 0
while(True):
    index = s.find(word)
    if(index == -1):
        break
    s = s[s.find(word)+len(word):]
    cnt += 1
print(cnt)
