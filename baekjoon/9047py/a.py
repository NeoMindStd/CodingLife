for T in range(int(input())):
    n = input()
    cnt = 0
    while n != '6174':
        cnt += 1
        tmp = ''.join(sorted(n))
        n = '%04d' %(int(tmp[::-1]) - int(tmp))
    print(cnt)
