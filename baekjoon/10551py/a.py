s = input()
finger=dict()
finger[1]=['`', '1', 'Q', 'A', 'Z']
finger[2]=['2', 'W', 'S', 'X']
finger[3]=['3', 'E', 'D', 'C']
finger[4]=['4', 'R', 'F', 'V', '5', 'T', 'G', 'B']
finger[5]=['6', 'Y', 'H', 'N', '7', 'U', 'J', 'M']
finger[6]=['8', 'I', 'K', ',']
finger[7]=['9', 'O', 'L', '.']
finger[8]=['0', 'P', ';', '/', '-', '[', "'", '=', ']']

count = {i:0 for i in range(1, 9)}

for c in s:
    for i in range(1, 9):
        if c in finger[i]:
            count[i] += 1
            break

print("\n".join(map(str, count.values())))
