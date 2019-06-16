from collections import Counter

s = list(input())
for i, ch in enumerate(s):
    if ch > 'Z':
        s[i] = chr(ord(ch)-(ord('a')-ord('A')))
    else :
        s[i] = ch
        
mosts = Counter(s).most_common()
try:
    if mosts[0][1] == mosts[1][1]:
        print('?')
    else :
        print(mosts[0][0])
except IndexError:
    print(mosts[0][0])
