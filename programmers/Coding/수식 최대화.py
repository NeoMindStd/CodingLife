def solution(expression):
    answer = 0

    cases = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i!=j!=k!=i: cases.append({i:'+', j:'-', k:'*'})

    conv = []
    ops = set(list('+-*'))
    i, prev = 1, 0
    while True:
        if i >= len(expression):
            conv.append(int(expression[prev:]))
            break
        if expression[i] in ops:
            conv.append(int(expression[prev:i]))
            conv.append(expression[i])
            prev = i + 1
        i += 1
    
    for case in cases:
        tmp = conv[:]
        for i in range(3):
            while True:
                try:
                    st = tmp.index(case[i])
                    tmp = tmp[:st-1] + [eval(''.join(map(str,tmp[st-1:st+2])))] + tmp[st+2:]
                except: break
        answer = max(answer, abs(tmp[0]))
                
    
    return answer


print(solution("100-200*300-500+20"))
