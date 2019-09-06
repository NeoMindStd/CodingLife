n = int(input())

space = [[' ']*(4*n-3) for _ in range((4*n-1) if n > 1 else 1)]

def create_universe(idx):
    char = '*' if idx %2 ==  0 else ' '
    # ┌
    for i in range(idx, 4*n-3 - idx):
        space[idx][i] = char
    for i in range(idx, ((4*n-1) if n > 1 else 1)-idx):
        space[i][idx] = char

        
    if n == 1 or idx >= 2*n-2:
        return
    # ┘
    for i in range(idx, 4*n-3-idx):
        space[4*n-2-idx][i] = char
    for i in range(idx+2, 4*n-1-idx):
        space[i][4*n-4-idx] = char
    space[idx+2][4*n-5-idx] = char
        
    create_universe(idx+1)

create_universe(0)

result = ''
for i in range(len(space)):
    if i == 1:
        result += '*\n'
    else :
        result += ''.join(map(str,space[i])) + '\n'

print(result)
