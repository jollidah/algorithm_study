import sys

def solution():
    inp = sys.stdin.readline
    n, m = map(int, inp().split())
    
    grid = [inp().rstrip() for _ in range(n)]
    
    for l in range(min(n, m), -1, -1):
        for y in range(n - l):
            for x in range(m - l):
                if grid[y][x] == grid[y + l][x] == grid[y][x + l] == grid[y + l][x + l]:
                    print((l + 1)**2)
                    exit(0)

if __name__ == "__main__":
    solution()
