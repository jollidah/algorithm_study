n = int(input())

arr = [input().strip() for _ in range(n)]
arr.sort()

ans = n

for i in range(n - 1):
    if arr[i + 1].startswith(arr[i]):
        ans -= 1

print(ans)
