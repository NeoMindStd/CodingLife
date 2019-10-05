a = list(format(int(input()), 'b'))
a.reverse()
print(int(str("".join(a)), 2))
