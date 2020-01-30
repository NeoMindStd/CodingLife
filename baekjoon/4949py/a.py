while True:
    stack=[];push,pop=stack.append,stack.pop
    s=input()
    if s=='.':break
    r='yes'
    for c in s:
        if c in ['[','(']:
            push(c)
        elif c==']':
            if not stack or pop()!='[':r='no';break
        elif c==')':
            if not stack or pop()!='(':r='no';break
    if stack:r='no'
    print(r)
