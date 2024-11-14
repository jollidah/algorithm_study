n = int(input())
num = list(map(int, input().split()))
s = int(input())

for i in range(n):
    if s == 0:
        break

    max_idx = i
    for j in range(i + 1, min(n, i + s + 1)):
        if num[j] > num[max_idx]:
            max_idx = j

    if max_idx != i:
        for k in range(max_idx, i, -1):
            num[k], num[k - 1] = num[k - 1], num[k]
        s -= (max_idx - i)

print(*num)
