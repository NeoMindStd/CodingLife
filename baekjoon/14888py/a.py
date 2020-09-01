def calc(a, b, opCode):
    if opCode == 0: return a+b
    if opCode == 1: return a-b
    if opCode == 2: return a*b
    if opCode == 3: return -(-a//b) if a<0<b  else a//b

n = int(input())
a = list(map(int,input().split()))
ops = list(map(int,input().split()))

maxAns, minAns = -1_000_000_000, 1_000_000_000
def backTraking(operand, i, ops):
    if i  >= n - 2:
        global maxAns, minAns
        result = calc(operand, a[-1], ops.index(1))
        maxAns, minAns = max(maxAns, result), min(minAns, result)
        return
    for opCode in range(4):
        if ops[opCode] > 0:
            paramOp = ops.copy()
            paramOp[opCode] -= 1
            backTraking(calc(operand, a[i+1], opCode), i+1, paramOp)

backTraking(a[0], 0, ops)
print(maxAns)
print(minAns)
