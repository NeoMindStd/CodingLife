koong = [1, 1, 2, 4]

for i in range(4, 69):
    koong.append(koong[i-1]+koong[i-2]+koong[i-3]+koong[i-4])

for _ in range(int(input())):
    print(koong[int(input())])
