import sys

sys.setrecursionlimit(10000)

class Node:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def post_order_traversal(tree, results):
    if tree.left != None: post_order_traversal(tree.left, results)
    if tree.right != None: post_order_traversal(tree.right, results)
    results.append(tree.key)

for line in sys.stdin:
    key = int(line)
    try:
        tmp = tree
        while True:
            if key < tmp.key:
                if tmp.left is None:
                    tmp.left = Node(key)
                    break
                tmp = tmp.left
            elif key > tmp.key:
                if tmp.right is None:
                    tmp.right = Node(key)
                    break
                tmp = tmp.right
    except: tree = Node(key)

results = []
post_order_traversal(tree, results)
print('\n'.join(map(str, results)))
