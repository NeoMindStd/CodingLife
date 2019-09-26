l, c = map(int, input().split())
string = input().split()
string.sort()

mo = ('a', 'e', 'i', 'o', 'u')
answers = set()

def create(i, m_cnt, z_cnt, created):
    if m_cnt+z_cnt >= l:
        if m_cnt >= 1 and z_cnt >= 2:
            answers.add(created)
        return
    if i >= c:
        return
    if string[i] in mo:
        create(i+1, m_cnt+1, z_cnt, created+string[i])
    else:
        create(i+1, m_cnt, z_cnt+1, created+string[i])
    create(i+1, m_cnt, z_cnt, created)

create(0, 0, 0, "")

print('\n'.join(map(str, sorted(list(answers)))))
        
