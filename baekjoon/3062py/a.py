for T in range(int(input())):
    n = int(input())
    m = int(str(n)[::-1])
    t = str(n + m)
    print('YES' if t == t[::-1] else 'NO')
