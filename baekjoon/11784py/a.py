import sys
for line in sys.stdin:
    res = ""
    for i in range(0, len(line)-1, 2):
        s = line[i:i+2]
        res += chr(int(s, 16))
    print(res)
