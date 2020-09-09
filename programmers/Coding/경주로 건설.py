directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(board):    
    n = len(board)
    
    costs = []
    
    for i in range(1,3):
        visited = [[25*25*500] * n for _ in range(n)]
        visited[0][0] = 100
        costs.append(dfs(board, n, visited, 0, 0, directions[i], 0))

    return min(costs)

def dfs(board, n, visited, r, c, last_dir, cost):
    if r >= n-1 <= c:
##        print('=====', cost)
##        for row in visited: print(*row)
##        print('=====')
        return cost
    
    results = []
    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
            next_cost = cost + 100
            if direction != last_dir: next_cost += 500
            if visited[nr][nc] > next_cost:
                visited[nr][nc] = next_cost
                results.append(dfs(board, n, visited, nr, nc, direction, next_cost))
    return min(results) if results else 25*25*500


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
