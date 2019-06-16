n = int(input())

for i in range(n):
    k, s = input().split()
    for ch in s:
        for j in range(int(k)):
            print(ch, end="")
    print()
