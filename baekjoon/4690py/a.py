result = []
for b in range(2, 98):
    for c in range(b+1, 99):
        for d in range(c+1, 100):
            value = (b**3 + c**3 + d ** 3)
            if value > 1_000_000: continue
            a = int(value**(1/3))
            if a**3 == value: result.append((a, b, c, d))
            a += 1
            if a**3 == value: result.append((a, b, c, d))

result.sort()
print('\n'.join(map(lambda x:f'Cube = {x[0]}, Triple = ({x[1]},{x[2]},{x[3]})', result)))
