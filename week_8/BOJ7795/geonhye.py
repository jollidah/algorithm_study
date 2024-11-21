# 먹을 것인가 먹힐 것인가 / 20m

import sys
input = sys.stdin.readline

def binarySearch(a, b):
    res = 0
    memo = {}

    for i in range(len(a)):
        tmp = 0
        if a[i] in memo:
            res += memo[a[i]]
            continue
        else:
            l, r = 0, len(b)-1
            while l <= r:
                mid = (l + r )// 2
                if a[i] <= b[mid]:
                    r = mid - 1
                elif a[i] > b[mid]:
                    tmp += mid -l + 1
                    l = mid + 1
            memo[a[i]] = tmp
            res += tmp
    print(res)

if __name__ == "__main__":
    t = int(input().rstrip())
    for _ in range(t):
        an, bn = map(int, input().rstrip().split())

        A = list(map(int, input().strip().split()))
        B = sorted(list(map(int, input().strip().split())))

        binarySearch(A, B)