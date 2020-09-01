def solution(records):
    answer = []

    names = {}
    msgs = []

    for record in records:
        try: op, uid, name = record.split()
        except: op, uid = record.split()
        if op  == 'Change':
            names[uid]=name
        elif op == 'Enter':
            names[uid]=name
            msgs.append((uid,'님이 들어왔습니다.'))
        elif op == 'Leave':
            msgs.append((uid,'님이 나갔습니다.'))
        
    for msg in msgs: answer.append(names[msg[0]]+msg[1])
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
