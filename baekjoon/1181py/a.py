import sys
words = list(set([sys.stdin.readline() for _ in range(int(sys.stdin.readline()))]))


def merge_sort(p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)
        
def merge(p, q, r):
    i = p
    j = q+1
    len_fr = len(words[i]) if i <= q else 99
    len_bc = len(words[j]) if j <= r else 99
    tmp = []
    while len_fr+len_bc<198:
        if len_fr < len_bc:
            tmp.append(words[i])
            i += 1
            len_fr = len(words[i]) if i <= q else 99
        elif len_fr > len_bc:
            tmp.append(words[j])
            j += 1
            len_bc = len(words[j]) if j <= r else 99
        else:
            for k in range(len_fr):
                if ord(words[i][k]) < ord(words[j][k]):
                    tmp.append(words[i])
                    i += 1
                    len_fr = len(words[i]) if i <= q else 99
                    break
                if ord(words[i][k]) > ord(words[j][k]):
                    tmp.append(words[j])
                    j += 1
                    len_bc = len(words[j]) if j <= r else 99
                    break
    for i in range(p, r+1):
        words[i] = tmp[i-p]

merge_sort(0, len(words)-1)
print(''.join(words))
