import sys; read = sys.stdin.readline

sys.setrecursionlimit(1_000_000)

results = []
    
n = int(read())
in_order = list(map(int, read().split()))
in_idx = {in_order[i]: i for i in range(n)}
post_order = list(map(int, read().split()))

def insert_from_in_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end: return

    results.append(post_order[post_end])
    root_idx = in_idx[post_order[post_end]]

    left_size = root_idx - in_start

    insert_from_in_order(in_start, root_idx - 1,
                         post_start, post_start + left_size - 1)
    insert_from_in_order(root_idx + 1, in_end,
                         post_start + left_size, post_end - 1)

insert_from_in_order(0, n - 1, 0, n - 1)

print(' '.join(map(str, results)))
