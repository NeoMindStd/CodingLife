import sys

def move(ea, src, by, dest):
    if ea == 1:
        global result
        result.append(f'{src} {dest}\n')
        return 1
    else:
        return move(ea-1, src, dest, by) + move(1, src, by, dest) + move(ea-1, by, src, dest)

result = []
print(move( int(sys.stdin.readline()), 1, 2, 3 ))
print("".join(result))
        
