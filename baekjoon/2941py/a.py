ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for ch in ca:
    s = s.replace(ch, 'a')

print(len(s))
