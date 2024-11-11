import sys
from collections import deque

def solution():
    inp = sys.stdin.readline
    n, dq, dt = int(inp()), deque(), ((1, 0), (0, 1))
    grid = [list(map(int, inp().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    dq.append((0, 0))
    while dq:
        y, x = dq.pop()
        cnt  = grid[y][x]
        for dy, dx in dt:
            if (nextY:=y + cnt * dy) < n and (nextX:=x + cnt * dx) < n and not visited[nextY][nextX]:
                visited[nextY][nextX] = True
                if nextY == n - 1 and nextX == n - 1 :
                    print("HaruHaru")
                    exit(0)
                dq.append((nextY, nextX))
    print("Hing")

if __name__ == "__main__":
    solution()