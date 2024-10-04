import sys
from collections import deque

def solution():
    inp = sys.stdin.readline
    n, _ = map(int, inp().split())
    targets = list(map(int, inp().split()))
    dq = deque(range(1, n + 1))
    res = 0
    for target in targets:
        cnt = 0
        while (next:=dq.popleft()) != target:
            cnt += 1
            dq.append(next)
        res += min(cnt, len(dq) + 1 - cnt)
    print(res)

if __name__ == "__main__":
    solution()