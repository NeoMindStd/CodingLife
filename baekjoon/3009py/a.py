points = [input().split() for _ in range(3)]
x_list = [point[0] for point in points]
y_list = [point[1] for point in points]

print(min(x_list) if x_list.count(min(x_list)) == 1 else max(x_list),
      min(y_list) if y_list.count(min(y_list)) == 1 else max(y_list))
