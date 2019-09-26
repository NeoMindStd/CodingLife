for _ in range(int(input())):
    string = input()
    stack = []
    push = stack.append
    pop = stack.pop
    flag = True
    for char in string:
        if char == '(':
            push(char)
        else:
            if not stack:
                flag = False
                break
            pop()
    print('YES' if not stack and flag else 'NO')
