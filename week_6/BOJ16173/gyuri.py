import sys
input = sys.stdin.readline

def main():
    n = int(input().strip()) 
    grid = [list(map(int, input().split())) for _ in range(n)] 
    visited = [[False] * n for _ in range(n)]

    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= n or visited[x][y]:
            return False
        if x == n - 1 and y == n - 1:
            return True
        
        visited[x][y] = True
        jump = grid[x][y]

        return dfs(x + jump, y) or dfs(x, y + jump)

    if dfs(0, 0):
        print("HaruHaru")
    else:
        print("Hing")

if __name__ == "__main__":
    main()
