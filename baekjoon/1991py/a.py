import collections

n = int(input())

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

tree = Node("A")
for _ in range(n):
    datas = list(input().split())
    stack = collections.deque([tree])
    while True:
        tmp = stack.pop()
        if tmp.data == datas[0]:
            break
        if tmp.left is not None:
            stack.append(tmp.left)
        if tmp.right is not None:
            stack.append(tmp.right)
    if datas[1] != "." :
        tmp.left = Node(datas[1])
    if datas[2] != "." :
        tmp.right = Node(datas[2])

def preorder(node):
    print(node.data, end="")
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)
        
def inorder(node):
    if node.left is not None:
        inorder(node.left)
    print(node.data, end="")
    if node.right is not None:
        inorder(node.right)
        
def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.data, end="")

preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
