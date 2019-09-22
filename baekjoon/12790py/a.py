import sys

for _ in range(int(sys.stdin.readline())):
    status = list(map(int, sys.stdin.readline().split()))
    hp = status[0] + status[4]
    hp = hp if hp > 1 else 1
    mp = status[1] + status[5]
    mp = mp if mp > 1 else 1
    atk = status[2] + status[6]
    atk = atk if atk > 0 else 0
    grd = status[3] + status[7]

    combat = 1*hp + 5*mp + 2*atk + 2*grd
    print(combat)
