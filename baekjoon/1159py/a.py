names = {chr(c):0 for c in range(ord('a'), ord('z')+1)}
for _ in range(int(input())):
    names[input()[0]] += 1
result = ""
for key, value in names.items():
    if value < 5: continue
    result += key
print(result if result!="" else "PREDAJA")
        
