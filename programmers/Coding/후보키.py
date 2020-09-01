def solution(relation):
    answer = 0

    combs = []
    for i in range(len(relation[0])):
        getComb(combs, [i], len(relation[0])-1)
        
    combs.sort(key=lambda x:len(x))
    candKeys = []

    for comb in combs:
        isTried = False
        for candKey in candKeys:
            cnt = 0
            for col in candKey:
                if col in comb: cnt+=1
            isTried = cnt == len(candKey)
            if isTried: break
        if isTried: continue
        
        if isUniqueComb(relation, comb): candKeys.append(comb)

    answer = len(candKeys)
    
    return answer

def getComb(origin, comb, last):
    origin.append(comb)
    for i in range(comb[-1] + 1, last+1):
       getComb(origin, comb+[i], last)

def isUniqueComb(relation, comb):
    rows = set()
    for row in relation:
        result = []
        for col in comb: result.append(row[col])
        result = tuple(result)
        if result in rows: return False
        rows.add(result)

    return True

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
