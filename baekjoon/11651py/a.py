import sys

points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

points.sort(key=lambda point: (point[1], point[0]))

result = ''
for point in points:
    result += f"{point[0]} {point[1]}\n"
print(result)
