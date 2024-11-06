# 트리 / 20m

# 번호가 언급안된게 리프 노드
# n번 노드를 삭제하면 그것을 부모로 가지는 노드들을 따라가서 모두 삭제

import sys

n = int(sys.stdin.readline().strip())
tree = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())

def dfs(num, ls):
    ls[num] = -2
    for i in range(len(ls)):
        if ls[i] == num:
            dfs(i, ls)

def main():
    dfs(x, tree)

    res = 0
    for i in range(len(tree)):
        if tree[i] != -2 and i not in tree:
            res += 1

    print(res)

if __name__ == "__main__":
    main()