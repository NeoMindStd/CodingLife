n = int(input())

#1-1
#2-5
#3-9
#4-13

space = [[' ']*(4*n-3) for _ in range(4*n-3)]

def create_universe(idx):
    char = '*' if idx %2 ==  0 else ' '
    # ┌
    for i in range(idx, 4*n-3 - idx):
        space[idx][i] = char
        space[i][idx] = char
        space[4*n-4-idx][i] = char
        space[i][4*n-4-idx] = char
    
    if idx >= 2*n-2:
        return
        
    create_universe(idx+1)

create_universe(0)

result = ''
for i in range(len(space)):
    result += ''.join(map(str,space[i])) + '\n'

print(result)
