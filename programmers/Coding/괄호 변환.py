def solution(p):
    return recursion(p)

conv = {'(':')', ')':'('}
def recursion(p):
    if p == "": return p

    for i in range(2, len(p)+1):
        if not isBalanced(p[:i]): continue
        
        u, v = p[:i], p[i:]
        
        if isCorrect(u): return u + recursion(v)
        
        tmp = "(" + recursion(v) + ")"
        for c in u[1:-1]: tmp += conv[c]
        return tmp
    
def isCorrect(p):
    cnt = 0
    for c in p:
        if c=='(': cnt += 1
        elif cnt < 1: return False
        else: cnt -= 1
    return True

def isBalanced(p):
    return p.count("(") * 2 == len(p)


print(solution("(()())()"))
