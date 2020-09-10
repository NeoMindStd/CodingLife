def solution(user_id, banned_id):
    answer = []
    banned_id.sort()
    dfs(banned_id, 0, set(user_id), tuple(), answer)
    
    return len(set(answer))

def dfs(banned_id, index, uid_set, comb, answer):
    if index >= len(banned_id):
        answer.append(tuple(sorted(comb)))
        return
    
    for uid in uid_set:
        if len(uid) != len(banned_id[index]): continue
        banned = True
        for i in range(len(uid)):
            if banned_id[index][i] != uid[i] and banned_id[index][i] != '*':
                banned = False
                break
        if banned: dfs(banned_id, index+1, uid_set-set([uid]), comb+tuple([uid]), answer)
    

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
