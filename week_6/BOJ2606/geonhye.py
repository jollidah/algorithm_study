# 바이러스 / 10m

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

visited = [False] * (n + 1)

# 그래프 생성
graph = [[] for _ in range(n+ 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(n):
    virus = 0
    q = deque([n])
    visited[n] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                virus += 1
    return virus

print(bfs(1))