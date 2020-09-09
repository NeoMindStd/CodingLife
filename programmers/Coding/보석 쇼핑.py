def solution(gems):
    answers = []
    gem_set = set(gems)

    last = 0

    while last + len(gem_set) - 1 < len(gems):

        start, end, last = last, last + len(gem_set) - 1, len(gems)
        gem_dic = dict()
        
        for i in range(start, end):
            try: gem_dic[gems[i]] += 1
            except: gem_dic[gems[i]] = 1

        while end < len(gems):
            try: gem_dic[gems[end]] += 1
            except: gem_dic[gems[end]] = 1
            if len(gem_dic.keys()) == len(gem_set): break
            end += 1
            
        while start <= end and len(gem_dic.keys()) == len(gem_set):
            gem_dic[gems[start]] -= 1
            if gem_dic[gems[start]] <= 0: del gem_dic[gems[start]]
            if len(gem_dic.keys()) < len(gem_set):
                answers.append([start+1, end+1])
                last = start + 1
                break
            start += 1

        if end - start + 1  == set(gems): return [start+1, end+1]

    return min(answers, key = lambda x:(x[1]-x[0], x[0], x[1]))

print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["SE", "PUSS", "PUSS", "BOO", "SE"]))
#print(solution(["DIA"]))
#print(solution(["DIA", "DIA"]))
