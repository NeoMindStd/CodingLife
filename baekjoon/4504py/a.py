n=int(input())
while True:
    a=int(input())
    if a==0: break
    print('%d is%sa multiple of %d.' %(a, ' NOT 'if a%n!=0 else' ', n))
