n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append(a - b)
    
arr.sort()

if len(arr) % 2 == 0:
    h = len(arr) // 2
    print(arr[h] - arr[h - 1] + 1)
    
else:
    print(1)
    
    
