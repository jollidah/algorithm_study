import sys
from collections import deque

def solution():
    inp = sys.stdin.readline
    n = int(inp())
    parents, childs, dq = list(map(int, inp().split())), [[] for _ in range(n)], deque()
    for i in range(n):
        if parents[i] != -1:
            childs[parents[i]].append(i)
    res = len(list(filter(lambda x: len(x) == 0, childs)))
    remove = int(inp())
    if not childs[remove] and len(childs[parents[remove]]) != 1:
        print(res - 1)
        exit(0)
    dq.append(remove)
    while dq:
        node = dq.pop()
        for child in childs[node]:
            if childs[child]:
                dq.append(child)
            else:
                res -= 1
    print(res)

if __name__ == "__main__":
    solution()
