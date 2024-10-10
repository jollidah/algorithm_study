def find_square(a):
    for i in range(n-a+1):
        for j in range(m-a+1):
            if rec[i][j] == rec[i][j+a-1] == rec[i+a-1][j] == rec[i+a-1][j+a-1]:
                return True
    return False

n, m = map(int, input().split())

rec = [list(map(int, list(input()))) for i in range(n)]

s = min(n, m)

for i in range(s, 0, -1):
    if find_square(i):
        print(i**2)
        break
