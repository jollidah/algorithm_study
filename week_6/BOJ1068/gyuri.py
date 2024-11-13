import sys
input = sys.stdin.readline

def main():
    def cnt_nodes(node, tree, delete):
        if node == delete:
            return 0
        
        if not tree[node]:
            return 1

        leaf_count = 0
        for child in tree[node]:
            leaf_count += cnt_nodes(child, tree, delete)
        
        return leaf_count

    n = int(input().strip())
    parent = list(map(int, input().strip().split()))
    delete = int(input().strip())

    tree = [[] for _ in range(n)]
    root = None

    for i in range(n):
        if parent[i] == -1:
            root = i 
        else:
            tree[parent[i]].append(i) 

    if delete != root and parent[delete] != -1:
        tree[parent[delete]].remove(delete)

    if root == delete:
        print(0)
    else:
        result = cnt_nodes(root, tree, delete)
        print(result)
if __name__=="__main__":
    main()