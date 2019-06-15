n = int(input())

def dumb():
    for i in range(n):
        #print(len(range(n)),
        #      len(range(n, i, -1)),
        #      len(range(2*i+1)))
        for j in range(n, i, -1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()

def init(n):
    layout = list()
    for i in range(n):
        tmp = list()
        for j in range(n-i-1):
            tmp.append(" ")
        for j in range(2*i+1):
            tmp.append("*")
        for j in range(2*i+1, 2*n):
            tmp.append(" ")
        layout.append(tmp)
    return layout

def draw(layout):
    n = len(layout)
    #for i in range(n//2, n):
    return layout

def print_layout(layout):
    for lane in layout:
        for space in lane:
            print(space, end="")
        print()

print_layout(draw(init(n)))
