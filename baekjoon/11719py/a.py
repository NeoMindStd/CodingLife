strings = list()

for i in range(100) :
    try:
        strings.append(input())
    except EOFError:
        break
    
for string in strings :
    print(string)
