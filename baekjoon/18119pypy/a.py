import sys; read = sys.stdin.readline

def strToBit(word):
    result = 0
    for ch in word: result |= 1 << (ord(ch) - ord('a'))
    
    return result
    
n, m = map(int, read().split())

words = [strToBit(read()[:-1]) for _ in range(n)]
memory = strToBit(map(lambda i: chr(ord('a')+i), range(26)))
result = []

for i in range(m):
    query, ch = input().split()
    query = int(query)

    if query == 2: memory |= strToBit(ch)
    else: memory &= ~strToBit(ch)

    cnt = 0
    for word in words:
        if word & memory == word: cnt += 1
    result.append(str(cnt))
   
print('\n'.join(result))