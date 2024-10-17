import sys

def solution():
    def DFS(y, x, l):
        standard = grid[y][x]
        is_same = True
        for ty in range(l):
            for tx in range(l):
                if standard != grid[y + ty][x + tx]:
                    is_same = False
                    break
            if not is_same:
                break
        if is_same:
            res[standard + 1] += 1
        else:
            l //= 3
            for i in range(3):
                for j in range(3):
                    DFS(y + i * l, x + j * l, l)

    inp = sys.stdin.readline
    n = int(inp())
    grid, res = [list(map(int, inp().split())) for _ in range(n)], [0, 0, 0]
    DFS(0, 0, n)
    for r in res:
        print(r)

if __name__ == "__main__":
    solution()
