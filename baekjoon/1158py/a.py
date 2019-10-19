class Node:
    def __init__(self,value, nxt=None):
        self.value = value
        self.nxt = nxt
n, k = map(int, input().split())
start = node = Node(0)
for i  in range(1, n+1):
    tmp = Node(i)
    node.nxt = node = tmp
node.nxt, node = start.nxt, start

result = []
for _ in range(n):
    for __ in range(k):
        tmp, node = node, node.nxt
    result.append(node.value)
    tmp.nxt = node.nxt
print("<"+", ".join(map(str, result))+">")
