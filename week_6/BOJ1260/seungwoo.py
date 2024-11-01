import sys
from collections import deque

def solution():
    def DFS(v):
        for child in childs[v]:
            if not visited[child]:
                visited[child] = True
                res.append(child)
                DFS(child)

    inp = sys.stdin.readline    
    (n, m, v) = map(int, inp().split())
    childs, dq = [[] for _ in range(n + 1)], deque()
    for _ in range(m):
        a, b = map(int, inp().split())
        childs[a].append(b)
        childs[b].append(a)
    visited, res = [False] * (n + 1), [v]
    
    for c in childs:
        c.sort()
    visited[v] = True
    DFS(v)
    print(*res)
    
    res = [v]
    dq.append(v)
    for i in range(1, n + 1):
        visited[i] = False
    visited[v] = True

    while dq:
        next = dq.popleft()
        for child in childs[next]:
            if not visited[child]:
                visited[child] = True
                dq.append(child)
                res.append(child)

    print(*res)

if __name__ == "__main__":
    solution()
