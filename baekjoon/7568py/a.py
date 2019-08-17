n = int(input())

people = list()
ranks = [1]*n

for i in range(n):
    people.append(tuple(map(int, input().split())))

for i in range(len(people)):
    for j in range(len(people)):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            ranks[j] += 1

print(*ranks)
