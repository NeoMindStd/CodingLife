_ = int(input())
a = set(map(int, input().split()))
_ = int(input())
b = list(map(int, input().split()))

for each_b in b:
    print(1 if each_b in a else 0)
