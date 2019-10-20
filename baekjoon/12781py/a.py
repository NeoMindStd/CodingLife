def ccw(pos1, pos2, pos3):
    x1, x2, x3 = pos1[0], pos2[0], pos3[0]
    y1, y2, y3 = pos1[1], pos2[1], pos3[1]
    tmp = x1*y2+x2*y3+x3*y1 - y1*x2-y2*x3-y3*x1
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

def isCross(a, b, c, d):
    ab = ccw(a, b, c)*ccw(a, b, d)
    cd = ccw(c, d, a)*ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return c<=b and a<=d
    return ab<0 and cd<0

pos = list(map(int, input().split()))
print(1 if isCross(pos[0:2], pos[2:4], pos[4:6], pos[6:8]) else 0)
