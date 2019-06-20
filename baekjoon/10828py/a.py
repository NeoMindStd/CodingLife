top = -1
stack = list()

def push(x):
    global top
    top += 1
    stack.append(x)

def pop():
    global top
    try:
        r =  stack.pop()
        top -= 1
    except IndexError:
        r = -1
    return r

def getSize():
    global top
    return top+1
    
def isEmpty():
    global top
    return 1 if top == -1 else 0

def peek():
    try:
        r =  stack[-1]
    except IndexError:
        r = -1
    return r
    

for T in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "size":
        print(getSize())
    elif cmd[0] == "empty":
        print(isEmpty())
    elif cmd[0] == "top":
        print(peek())

