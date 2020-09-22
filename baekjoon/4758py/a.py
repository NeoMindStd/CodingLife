position_dic = {"Wide Receiver":[4.5, 150, 200],
                "Lineman":[6.0, 300, 500],
                "Quarterback":[5.0, 200, 300]}

while True:
    a, b, c = map(float, input().split())
    if a == b == c == 0: break
    
    result = []

    for key, value in position_dic.items():
        if a <= value[0] and b >= value[1] and c >= value[2]:
            result.append(key)
    
    print(' '.join(result) if result else 'No positions')
