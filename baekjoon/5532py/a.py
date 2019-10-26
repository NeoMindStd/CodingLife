import math
l=[int(input()) for _ in range(5)]
print(l[0]-max(math.ceil(l[1]/l[3]), math.ceil(l[2]/l[4])))
