n = int(input())*int(input())*int(input())
l = list(0 for i in range(10))

while(True):
    if(n < 1):
        break
    l[int(n%10)]+=1
    n/=10
for i in l:
    print(i)
