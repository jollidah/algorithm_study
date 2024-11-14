from collections import deque

def main():
    n,m,v = map(int, input().split())

    graph = [[0]*(n+1) for _ in range(n+1)]
    dfs_check = [False]*(n+1)
    bfs_check = [False]*(n+1)


    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1


    def dfs(v):
        dfs_check[v] = True
        print(v, end=' ')
        for i in range(1, n+1):
            if not dfs_check[i] and graph[v][i] == 1:
                dfs(i)

    def bfs(v):
        bfs_check[v] = True
        queue = deque()
        queue.append(v)

        while(queue):
            popV = queue.popleft()
            print(popV, end=' ')
            for i in range(1, n+1):
                if not bfs_check[i] and graph[popV][i] == 1:
                    queue.append(i)
                    bfs_check[i] = True

    dfs(v)
    print()
    bfs(v)
if __name__=="__main__":
    main()