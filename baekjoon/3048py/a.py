cnt = 0
def ant_mapping(ant):
    global cnt
    cnt += 1
    return (cnt, ant)

n1, n2 = map(int, input().split())
ant1 = list(map(ant_mapping, input()[::-1]))
ant2 = input()
t = int(input())
cnt -= t + .5
ant2 = list(map(ant_mapping, ant2))
print(''.join(list(map(lambda x:x[1], sorted(ant1+ant2)))))
