for T in range(int(input())):
    s = ''
    while True:
        tmp = input()
        if tmp=='':break
        s+=tmp
    eRatio = round((1-s.count('#')/len(s))*100,1)
    eRatio = eRatio if eRatio != int(eRatio) else int(eRatio)
    print(f'Efficiency ratio is {eRatio}%.')
