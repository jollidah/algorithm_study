import sys

def solution():
    inp = sys.stdin.readline
    n, a, b = int(inp()), sorted(list(map(int, inp().split()))), sorted(list(map(int, inp().split())), reverse=True)
    res = 0
    for i in range(n):
        res += a[i] * b[i]
    print(res)

if __name__ == "__main__":
    solution()
