found_path = False

def dfs(arr, n, x, y, visited):
    global found_path
    
    if x == n-1 and y == n-1:
        found_path = True
        return
        
    visited[x][y] = True
    
    dx = x + arr[x][y]
    dy = y + arr[x][y]
    
    if dx < n and not visited[dx][y]:
        dfs(arr, n, dx, y, visited)
    
    if dy < n and not visited[x][dy]:
        dfs(arr, n, x, dy, visited)
        

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dfs(arr, n, 0, 0, visited)

if found_path:
    print("HaruHaru")
else:
    print("Hing")
