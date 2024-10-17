count = [0] * 3

def count_num(arr, x, y):
    global count
    if arr[x][y] == -1:
        count[0] += 1
    elif arr[x][y] == 0:
        count[1] += 1
    else:
        count[2] += 1

def same_num(arr, n, x, y):
    global count
    first_num = arr[x][y]
                
    for i in range(n):
        for j in range(n):
            if arr[x + i][y + j] != first_num:
                size = n // 3
                
                for dx in range(3):
                    for dy in range(3):
                        same_num(arr, size, x + dx * size, y + dy * size)
                return
            
    count_num(arr, x, y)
                
        
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

same_num(arr, n, 0, 0)

print(count[0])
print(count[1])
print(count[2])
