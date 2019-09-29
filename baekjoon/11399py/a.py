n = int(input())
people = list(map(int, input().split()))
people.sort()

s = 0
for i in range(n):
    s += people[i]*(n-i)

print(s)
