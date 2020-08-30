def solution(s):
    answer = len(s)
    
    for d in range(1, len(s)//2+1):
        i = 0
        tmp = len(s)
        while i < len(s) - d:
            if s[i:i+d] == s[i+d:i+d*2]:
                cnt = 2
                i += d
                while i+d<len(s) and s[i:i+d] == s[i+d:i+d*2]:
                    cnt += 1
                    i += d
                tmp -= d * cnt - d - len(str(cnt))
            else: i += d
        answer = min(answer, tmp)
    
    return answer

print(solution("abrabcabcadqabcabc"))
