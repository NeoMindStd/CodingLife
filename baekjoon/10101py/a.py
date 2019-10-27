a, b, c = tuple([int(input()) for _ in range(3)])
if a==b==c==60:
    print("Equilateral")
elif a+b+c==180:
    if a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
