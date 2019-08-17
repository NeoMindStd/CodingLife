for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = tuple(map(int, input().split()))
    if x1==x2 and y1==y2 and r1==r2 :
        print(-1)
        continue
    diffPow = (x1-x2)**2 + (y1-y2)**2
    sumPow = (r1+r2)**2
    rDiffPow = (r1-r2)**2
    if diffPow == sumPow or rDiffPow == diffPow :
        print(1)
    elif diffPow > sumPow or rDiffPow > diffPow :
        print(0)
    else:
        print(2)            
