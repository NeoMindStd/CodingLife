import sys
people = list(set([tuple([i]+sys.stdin.readline().split()) for i in range(int(sys.stdin.readline()))]))

def merge_sort(p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)
        
def merge(p, q, r):
    i = p
    j = q+1
    age_fr = int(people[i][1] if i <= q else 201)
    age_bc = int(people[j][1] if j <= r else 201)
    tmp = []
    while age_fr+age_bc<402:
        if age_fr < age_bc:
            tmp.append(people[i])
            i += 1
            age_fr = int(people[i][1] if i <= q else 201)
        elif age_fr > age_bc:
            tmp.append(people[j])
            j += 1
            age_bc = int(people[j][1] if j <= r else 201)
        else:
            if people[i][0] < people[j][0]:
                tmp.append(people[i])
                i += 1
                age_fr = int(people[i][1] if i <= q else 201)
            else:
                tmp.append(people[j])
                j += 1
                age_bc = int(people[j][1] if j <= r else 201)
    for i in range(p, r+1):
        people[i] = tmp[i-p]

merge_sort(0, len(people)-1)
result = ''
for person in people:
    result += str(person[1]) + ' ' + person[2] + '\n'
print(result)
