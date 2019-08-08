a, b, v = map(int, input().split())

def foo(n):
    global a,b
    return n*a - (n-1)*b

def bin_search(start, end):
    n = (start + end) // 2
    if(foo(n) >= v and foo(n-1) < v):
        return n
    elif(foo(n) > v):
        end = n
    else:
        start = n
    return bin_search(start, end)

print(bin_search(1, v))
