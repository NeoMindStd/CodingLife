from sys import stdin

for line in stdin:
  print(sum(map(int, line.split())))
