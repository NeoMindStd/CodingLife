n, m, l = map(int, input().split())
people = [0] * n
i = 0
people[i] += 1

while max(people) < m:
    if people[i] % 2 > 0: i = (i + l) % n
    else:
        pm = 1
        if i - l < 0: pm = -1
        i = abs(i - l) % n * pm
    people[i] += 1
    
print(sum(people) - 1)
