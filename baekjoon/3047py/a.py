abc = list(map(int, input().split()))
abc.sort()

s = input()

for i in range(3):
    print(abc[ord(s[i])-ord('A')], end=" ")
