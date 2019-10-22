from sys import stdin

s = set()
for _ in range(int(stdin.readline())):
    cmd = stdin.readline().split()
    c = cmd[0]
    if c == 'add':
        s.add(int(cmd[1]))
    elif c == 'remove':
        try:
            s.remove(int(cmd[1]))
        except:
            pass
    elif c == 'check':
        print(1 if int(cmd[1]) in s else 0)
    elif c == 'toggle':
        if int(cmd[1]) in s :
            s.remove(int(cmd[1]))
        else :
            s.add(int(cmd[1]))
    elif c == 'all':
        s = set([i for i in range(1, 21)])
    else:
        s = set()
