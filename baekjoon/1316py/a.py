def isGroupWord(word, char):
    if(len(word) == 1):
        return True
    elif(word.find(char) > 0):
        return False
    else:
        return isGroupWord(word[1:], word[0])


cnt = 0
for _ in range(int(input())):
    word = input()
    cnt += 1 if isGroupWord(word, word[0]) else 0

print(cnt)
