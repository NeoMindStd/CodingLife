people = list(map(int, input().split()))
x, y, r = map(int, input().split())

try: print(people.index(x) + 1)
except: print(0)
