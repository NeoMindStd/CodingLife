n, m, v = map(int, input().split())

l = []
for _ in range(m):
    l.append(tuple(map(int, input().split())))

def dfs(n, m, v, l):
    result = [v]
    stack = [v]
    check = dict()
    for i in range(1, n+1):
        check[i] = False
    check[v] = True

    while len(stack) > 0:
        tmp = []
        for line in l:
            if line[0] == stack[-1] and not check[line[1]]:
                tmp.append(line[1])
            elif line[1] == stack[-1] and not check[line[0]]:
                tmp.append(line[0])
        if len(tmp) == 0:
            stack.pop()
        else:
            point = min(tmp)
            stack.append(point)
            result.append(point)
            check[point] = True
    return result

def bfs(n, m, v, l):
    result = [v]
    queue = [v]
    check = dict()
    for i in range(1, n+1):
        check[i] = False
    check[v] = True

    while len(queue) > 0:
        tmp = []
        for line in l:
            if line[0] == queue[0] and not check[line[1]]:
                tmp.append(line[1])
            elif line[1] == queue[0] and not check[line[0]]:
                tmp.append(line[0])
        if len(tmp) == 0:
            queue.pop(0)
        else:
            point = min(tmp)
            queue.append(point)
            result.append(point)
            check[point] = True
    return result

print(*dfs(n, m, v, l))
print(*bfs(n, m, v, l))
