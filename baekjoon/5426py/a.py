for T in range(int(input())):
    cryptogram = input()
    n = int(len(cryptogram)**.5)

    table = [list(cryptogram[i*n:(i+1)*n]) for i in range(n)]

    decrypted = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            decrypted[i] += table[j][n-i-1]

    print(''.join(decrypted))
