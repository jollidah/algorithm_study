# DFS와 BFS / 30m

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

visited_dfs = [False] * (n + 1)
visited_bfs = visited_dfs.copy()

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

graph = list(map(lambda x: sorted(x), graph))

# dfs
def dfs(n):
    visited_dfs[n] = True
    print(n, end = " ")
    for i in graph[n]:
        if not visited_dfs[i]:
            dfs(i)

# bfs
def bfs(n):
    q = deque([n])
    visited_bfs[n] = True

    while q:
        v = q.popleft()
        print(v, end = " ")
        visited_bfs[v] = True
        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

def main():
    dfs(v)
    print()
    bfs(v)

if __name__ == '__main__':
    main()