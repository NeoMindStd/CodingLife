def solution(N, stages):
    answer = []
    
    info = [[0,0] for _ in range(N+2)]
    
    for stage in stages:
        for i in range(1,stage+1): info[i][1] += 1
        info[stage][0] += 1

    for i in range(1, N+1):
        try: answer.append((-info[i][0]/info[i][1], i))
        except ZeroDivisionError: answer.append((0, i))
    
    return list(map(lambda x:x[1], sorted(answer)))

print(solution(8, [1,2,3,4,5,6,7]))
