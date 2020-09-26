while True:
    s, e = input().split()
    if s == e == '00:00': break
    
    s = list(map(int, s.split(':')))
    e = list(map(int, e.split(':')))

    r = [s[i] + e[i] for i in range(2)]
    
    if r[1] >= 60:
        r[0] += r[1] // 60
        r[1] %= 60
        
    d = 0
    if r[0] >= 24:
        d += r[0] // 24
        r[0] %= 24

    answer = '%02d:%02d'%(r[0], r[1])
    if d > 0: answer += f' +{d}'
    print(answer)
