import sys
from collections import deque

def solution():
    inp = sys.stdin.readline
    n, v, dq, cnt = int(inp()), int(inp()), deque(), 0
    childs, visited = [[] for _ in range(n + 1)], [False for _ in range(n + 1)]
    for _ in range(v):
        a, b = map(int, inp().split())
        childs[a].append(b)
        childs[b].append(a)
    visited[1] = True
    dq.append(1)
    while dq:
        com = dq.pop()
        for child in childs[com]:
            if not visited[child]:
                visited[child] = True
                cnt += 1
                dq.append(child)
    print(cnt)

if __name__ == "__main__":
    solution()
