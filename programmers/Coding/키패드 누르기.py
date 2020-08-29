def solution(numbers, hand):
    answer = ''

    places = {i+1:(i//3, i%3) for i in range(9)}
    places['*'], places[0], places['#'] = (3, 0), (3, 1), (3, 2)
    cl, cr = '*', '#'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            cl = number
        elif number in [3, 6, 9]:
            answer += 'R'
            cr = number
        else:
            diffL = abs(places[cl][0]-places[number][0]) +\
                    abs(places[cl][1]-places[number][1])
            diffR = abs(places[cr][0]-places[number][0]) +\
                    abs(places[cr][1]-places[number][1])

            if diffL < diffR or (diffL == diffR and hand=='left'):
                answer += 'L'
                cl = number
            else:
                answer += 'R'
                cr = number
            
    
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
