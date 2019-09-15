s = input()
flag = s[1] != '0'
a = s[0:1 if flag else 2]
b = s[len(a) : len(s)]
print(int(a)+int(b))
