def solution(s):
    answer = []

    s = s[2:-2].split('},{')
    for i in range(len(s)): s[i] = set(map(int,s[i].split(',')))
    s.sort(key = lambda x: len(x))

    found = set([])
    for subset in s:
        for item in subset:
            if item not in found:
                answer.append(item)
                found.add(item)
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
