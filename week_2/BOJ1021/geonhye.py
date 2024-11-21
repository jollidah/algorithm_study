# 회전하는큐 / 40m
import sys

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    target = list(map(int, sys.stdin.readline().strip().split()))

    ls = [i for i in range(1, N+1)]

    res = 0
    for t in target:
        i = ls.index(t)
        # 1번
        if ls[0] == t:
            ls = ls[1:]
            continue
        # 왼쪽 | 오른쪽까지의 최소거리
        # 왼쪽 회전
        if i < len(ls) - i:
            res += i
            tmp = ls[:i]
            ls = ls[i+1:] + tmp
        # 오른쪽 회전
        else:
            res += len(ls) - i
            tmp = ls[i+1:]
            ls = tmp + ls[:i]
    print(res)

if __name__ == "__main__":
    main()