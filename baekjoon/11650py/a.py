import sys

points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

points.sort(key=lambda point: (point[0], point[1]))

result = ''
for point in points:
    result += f"{point[0]} {point[1]}\n"
print(result)
