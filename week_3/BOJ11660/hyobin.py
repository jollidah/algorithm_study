import sys 
input = sys.stdin.readline

n, m = map(int,input().split())

l = [list(map(int,input().split())) for i in range(n)]

dp_list = [[0] * (n+1) for i in range (n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp_list[i][j] = l[i-1][j-1] + dp_list[i-1][j] + dp_list[i][j-1] - dp_list[i-1][j-1]
        

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    answer = dp_list[x2][y2] - dp_list[x1-1][y2] - dp_list[x2][y1-1] + dp_list[x1-1][y1-1]
    
    print(answer)
