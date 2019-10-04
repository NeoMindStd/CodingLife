n, f = int(input()), int(input()) 
p = (n//100) * 100
for i in range(p, p+100):
    if i % f == 0:
        print("%02d" %(i%100))
        break
