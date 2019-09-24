import collections
import sys


class Node:
    def __init__(self, parent, data):
        self.parent = parent;
        self.data = data;
        self.children = collections.deque([])
        
n = int(sys.stdin.readline())
node_dict = {1: Node(None, 1)}

class Tree:
    def __init__(self):
        self.tree = node_dict[1];

    def push(self, a, b):
        node_dict[b] = Node(node_dict[a], b)
        node_dict[a].children.append(node_dict[b])

                
    def result(self):
        outs = []
        for i in range(2, n+1):
            outs.append(node_dict[i].parent.data)
        print("\n".join(map(str, outs)))

tree = Tree()
tree.push

graph = {i:[] for i in range(1, n+1)}
checked = [False]*(n+1)
queue = collections.deque([])

for _ in range(1, n):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue.append(1)
while queue:
    cur = queue.popleft()
    if checked[cur]:
        continue
    checked[cur] = True
    while graph[cur]:
        tmp = graph[cur].pop()
        if checked[tmp]:
            continue
        queue.append(tmp)
        tree.push(cur, tmp)

tree.result()
