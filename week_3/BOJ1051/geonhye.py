# 숫자 정사각형 / 25m

import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    ls = []
    for _ in range(n):
        ls.append(list(map(int, input().strip())))

    # 가능한 최대 길이
    mlen = min(n, m)

    res = [1]
    for l in range(2, mlen + 1):
        for i in range(m - l + 1):
            for j in range(n - l + 1):
                if ls[j][i] == ls[j][i+l-1] == ls[j+l-1][i] == ls[j+l-1][i+l-1]:
                    res.append(l * l)
                    continue
    print(res[-1])

if __name__ == '__main__':
    main()