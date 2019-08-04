items = list()
while(True):
    data = input()
    if(data == "END"):
        break
    items.append(data)

for item in items:
    print(item[::-1])
