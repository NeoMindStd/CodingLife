import collections
import sys

n = int(sys.stdin.readline())

class Node:
    def __init__(self, parent, data):
        self.parent = parent;
        self.data = data;
        self.children = collections.deque([])

class Tree:
    def __init__(self):
        self.tree = Node(None, 1);

    def push(self, a, b):
        stack = collections.deque([self.tree])
        pop = stack.pop
        push = stack.append
        
        while (stack):
            node = pop()
            if (node.data == a):
                node.children.append(Node(node, b))
                break
            elif (node.data == b):
                node.children.append(Node(node, a))
                break;
            stack += [child for child in node.children]
                
    def result(self):
        num = 2; 
        outs = collections.deque([])
        opush = outs.append
        while (num <= n):
            stack = collections.deque([self.tree])
            pop = stack.pop
            
            while (stack):                    
                node = pop()
                stack += [child for child in node.children]
                if (node.data == num):
                    opush(node.parent.data)
                    break
            num += 1
        print("\n".join(map(str, outs)))

tree = Tree()
push = tree.push

for _ in range(1, n):
    a, b = map(int,sys.stdin.readline().split())
    push(a, b)
tree.result()
