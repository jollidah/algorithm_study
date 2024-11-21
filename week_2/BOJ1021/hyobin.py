n, m = map(int, input().split())
queue = list(range(1, n+1))
count = 0

def left(a):
    global count
    tmp = a.pop(0)
    a.append(tmp)
    count += 1

def right(a):
    global count
    tmp = a.pop(-1)
    a.insert(0, tmp)
    count += 1

targets = list(map(int, input().split()))

for now in targets:
    target_index = queue.index(now)

    left_moves = target_index
    right_moves = len(queue) - target_index

    if left_moves <= right_moves:
        for _ in range(left_moves):
            left(queue)
    else:
        for _ in range(right_moves):
            right(queue)

    queue.pop(0)

print(count)
