while True:
    a, b, c = list(map(int, input().split()))
    if(a + b + c == 0): break
    print("right" if a**2 == b**2 + c**2 else ("right" if b**2 == a**2 + c**2 else ("right" if c**2 == a**2 + b**2 else "wrong")))
