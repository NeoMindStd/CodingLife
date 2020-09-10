import sys

sys.setrecursionlimit(10_000)

class Node:
    def __init__(self, no, x, y, level = 0, parent = None, left = None, right = None):
        self.no = no
        self.x = x
        self.y = y
        self.level = level
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        parent = left = right = 'None'
        try: parent = self.parent.no
        except:pass
        try: left = self.left.no
        except:pass
        try: right = self.right.no
        except:pass
        
        return f'No.{self.no} - x: {self.x}, y: {self.y}, lvl: {self.level}, parent: {parent}, left:{left}, right:{right}'

def solution(nodeinfo):
    nodes = []
    n = len(nodeinfo)
    
    for i in range(n):
        nodes.append((i+1, nodeinfo[i][0], nodeinfo[i][1]))

    nodes.sort(key = lambda x:(-x[2], x[1]))
    #print(nodes)

    tree = Node(*nodes[0])
    tree_nodes = [tree]

    parent_start = parent_end = 0
    for i in range(1, n):
        level = tree_nodes[-1].level
        if tree_nodes[-1].y > nodes[i][2]:
            parent_start = parent_end
            parent_end = i
            level += 1

        # 시간초과 해결법: 부모의 레벨을 특정시킨 후, 해당 레벨대의 인덱스만 검색
        for j in range(parent_start, parent_end):
            if nodes[i][1] < nodes[j][1] and\
               tree_nodes[j].left is None and\
               tree_nodes[j].level == level - 1 :
                
                check_x, tmp = True, tree_nodes[j]
                while True:
                    x = tmp.x
                    tmp = tmp.parent
                    if tmp == None: break
                    sub_dir = 'L' if x < tmp.x else 'R'
                    
                    if sub_dir == 'L' and nodes[i][1] >= tmp.x or\
                       sub_dir == 'R' and nodes[i][1] <= tmp.x:
                        check_x = False
                        break
                    
                if check_x:
                    tree_nodes.append(Node(*nodes[i]))
                    tree_nodes[-1].level = level
                    tree_nodes[-1].parent = tree_nodes[j]
                    tree_nodes[j].left = tree_nodes[-1]
                    break
                
            elif nodes[i][1] > nodes[j][1] and\
                 tree_nodes[j].right is None and\
                 tree_nodes[j].level == level - 1 :
                
                check_x, tmp = True, tree_nodes[j]
                while True:
                    x = tmp.x
                    tmp = tmp.parent
                    if tmp == None: break
                    sub_dir = 'L' if x < tmp.x else 'R'
                    
                    if sub_dir == 'L' and nodes[i][1] >= tmp.x or\
                       sub_dir == 'R' and nodes[i][1] <= tmp.x:
                        check_x = False
                        break
                    
                if check_x:
                    tree_nodes.append(Node(*nodes[i]))
                    tree_nodes[-1].level = level
                    tree_nodes[-1].parent = tree_nodes[j]
                    tree_nodes[j].right = tree_nodes[-1]
                    break

##    print(*map(str,tree_nodes),sep='\n')

    answer = [[], []]

    preorder_traversal(tree, answer[0])
    postorder_traversal(tree, answer[1])

    return answer

def preorder_traversal(tree, result):
    result.append(tree.no)
    if tree.left is not None: preorder_traversal(tree.left, result)
    if tree.right is not None: preorder_traversal(tree.right, result)
    
def postorder_traversal(tree, result):
    if tree.left is not None: postorder_traversal(tree.left, result)
    if tree.right is not None: postorder_traversal(tree.right, result)
    result.append(tree.no)
    

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
