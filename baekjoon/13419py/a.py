for T in range(int(input())):
    s = input()
    if len(s) % 2 != 0: s *= 2
    a, b = s[::2], s[1::2]
    print(a)
    print(b)
