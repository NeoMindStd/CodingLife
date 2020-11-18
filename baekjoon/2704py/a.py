def intToBin(num):
    result = []
    num = int(num)
    while num > 1:
        result.append(num % 2)
        num //= 2
    result.append(num)
    while len(result) < 6: result.append(0)
    return ''.join(map(str, result[::-1]))

for T in range(int(input())):
    h, m, s = map(intToBin, input().split(':'))
    col = []
    for i in range(6):
        col.append(h[i])
        col.append(m[i])
        col.append(s[i])
    print(''.join(col), h+m+s)
