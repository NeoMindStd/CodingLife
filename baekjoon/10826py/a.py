fibo=[0,1]
for i in range(9999):fibo.append(fibo[i]+fibo[i+1])
print(fibo[int(input())])
