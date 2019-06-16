n = list(map(int, input()))

a = [0 for _ in range(10)]

while(True):
    if(len(n)==0) :
        break
    a[n[-1]]+=1
    del n[-1]

a[6]=a[9]=(a[6]+a[9])//2 + (a[6]+a[9])%2
print(max(a))
