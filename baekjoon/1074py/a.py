N, r, c = map(int, input().split())

cnt = 0
flag = False
def search(x, y, size):
    global cnt, flag
    if size == 1:
        if (x, y) == (r, c):
            print(cnt)
            flag = True
        cnt += 1
        return
    if flag:
        return
    
    if r <= x+(size//2) and c <= y+(size//2):
        search(x, y, size//2)
    else:
        cnt += (size//2)**2
        
    if r <= x+(size//2) and c <= y+size:
        search(x, y+size//2, size//2)
    else:
        cnt += (size//2)**2
        
    if r <= x+size and c <= y+(size//2):
        search(x+size//2, y, size//2)
    else:
        cnt += (size//2)**2
        
    search(x+size//2, y+size//2, size//2)
        
search(0, 0, 2**N)
