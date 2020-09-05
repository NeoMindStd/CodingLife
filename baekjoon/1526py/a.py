for i in range(int(input()), 3, -1):
    s = str(i)
    if s.count('4') + s.count('7') == len(s):
        print(i)
        break
