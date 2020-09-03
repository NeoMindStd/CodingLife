def solution(key, lock):
    hole = 0
    for row in lock: hole += row.count(0)
    if hole == 0: return True

    for i in range(4):
##        print('======')
##        for row in key: print(*row)
##        print('======')
        for rStep in range(len(key)+len(lock)-1):
            for cStep in range(len(key)+len(lock)-1):
                if isMatched(key, lock, rStep, cStep, hole): return True
        key = rotateMatrixCW(key)
        
    return False

def isMatched(key, lock, rStep, cStep, hole):
    rStart = max(len(key) - rStep - 1, 0)
    rEnd = min(len(key), len(lock) + len(key) - rStep - 1)
    rLockStart = max(0, rStep - len(key) + 1)
    
    cStart = max(len(key) - cStep - 1, 0)
    cEnd = min(len(key), len(lock) + len(key) - cStep - 1)
    cLockStart = max(0, cStep - len(key) + 1)

##    print(f'rStep:{rStep}, rStart: {rStart}, rEnd: {rEnd}, rlockStart: {rLockStart}, cStep:{cStep}, cStart: {cStart}, cEnd: {cEnd}, clockStart: {cLockStart}, hole: {hole}')

    matched = True
    cnt = 0
    for i in range(rStart, rEnd):
        for j in range(cStart, cEnd):
##            print(f'key: ({i}, {j}, lock:({rLockStart+i-rStart}, {cLockStart+j-cStart}))')
            matched &= key[i][j] !=\
                       lock[rLockStart+i-rStart][cLockStart+j-cStart]
            if key[i][j] == 1 and\
               lock[rLockStart+i-rStart][cLockStart+j-cStart] == 0: cnt += 1
                
##    print(matched, cnt)
    return matched and cnt == hole

def rotateMatrixCW(mat):
    result = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat)-1, -1, -1):
            row.append(mat[j][i])
        result.append(row)
    return result

#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
##print(solution([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0,1]], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 1]]))
