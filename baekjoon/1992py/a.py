import sys

sys.setrecursionlimit(100_000)

n = int(input())
image = [list(input()) for _ in range(n)]

def encode(rs, cs, size):
    x = image[rs][cs]
    
    if size < 2: return x
    
    for i in range(rs, rs + size):
        for j in range(cs, cs + size):
            if x != image[i][j]:
                x = '2'
                break
        if x == '2': break
    
    if int(x) < 2: return x
    
    return '(' +\
           encode(rs, cs, size//2) +\
           encode(rs, cs + size//2, size//2) +\
           encode(rs + size//2, cs, size//2) +\
           encode(rs + size//2, cs + size//2, size//2) +\
           ')'
    
print(encode(0,0,n))
