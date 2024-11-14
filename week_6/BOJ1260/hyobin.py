from collections import deque

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)
            
def bfs(graph, start, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    graph[node1].sort()
    graph[node2].sort()

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
