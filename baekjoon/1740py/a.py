n=str(bin(int(input())))[:1:-1]

answer = 0
for i in range(len(n)):
    if n[i]=='1': answer += 3**i

print(answer)
