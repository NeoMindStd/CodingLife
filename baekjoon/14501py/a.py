n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]

def search(day, fee):
    if day > n: return 0
    
    result = [0]
    for i in range(day, n):
        result.append(search(i + l[i][0], l[i][1]))
        
    return fee + max(result)

print(search(0, 0))
