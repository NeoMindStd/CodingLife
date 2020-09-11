s = ''

while True:
    s += input()
    if s[-5:]=='E-N-D':
        s = s[:-5]
        break

s = ''.join(map(lambda x: x if ord('a')<=ord(x)<=ord('z') or x=='-' else ' ', s.lower()))
print(max(s.split(), key=lambda x:len(x)))
