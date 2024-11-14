def dfs(graph, v, visited):
    global count
    
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    

n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(v):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)
    

dfs(graph, 1, visited)

print(count)
