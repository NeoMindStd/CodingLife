s = input()

for ch in range(ord('a'), ord('z')+1):
    try:
        print(s.find(chr(ch)), end=" ")
    except ValueError:
        print(-1, end=" ")
