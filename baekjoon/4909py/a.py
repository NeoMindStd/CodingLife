while True:
    scores = list(map(int, input().split()))
    if max(scores) == 0: break

    answer = str((sum(scores) - max(scores) - min(scores)) / (len(scores) - 2))
    answer = answer.split('.')
    try:
        i = len(answer[1])
        while i > -1:
            i -= 1
            if answer[1][i] != '0': break
        
        print(answer[0]+('.' if i >= 0 else '')+answer[1][:i + 1])
    except: print(answer)
