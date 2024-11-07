def dfs(tree, v, visited):
    global cnt_leaf
    visited[v] = True
    is_leaf = True
    
    for i in tree[v]:
        if not visited[i]:
            is_leaf = False
            dfs(tree, i, visited)
            
    if is_leaf:
        cnt_leaf += 1

n = int(input())
tmp = list(map(int, input().split()))
del_node = int(input())
cnt_leaf = 0

tree = [[] for _ in range(n)]
visited = [False] * n

for i in range(n):
    if tmp[i] != -1 and i != del_node:
        tree[tmp[i]].append(i)
        
root = tmp.index(-1)
        
if root == del_node:
    print(0)
else:
    dfs(tree, root, visited)
    print(cnt_leaf)
