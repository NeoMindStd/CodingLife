a = int(input())

i=0
b=a
while True:
    i+=1
    roo = b%10
    ros = ((b//10)+(b%10))%10
    b= roo*10 + ros
    if(b == a):
        print(i)
        break
