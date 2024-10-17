# 구간합구하기5 / 40m

import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    ls = []
    for _ in range(n):
        ls.append(list(map(int, input().split())))

    # 누적합
    sum_ls = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            sum_ls[i][j] = sum_ls[i][j-1] + sum_ls[i-1][j] - sum_ls[i-1][j-1] + ls[i-1][j-1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        
        res = sum_ls[x2][y2] - sum_ls[x2][y1-1] - sum_ls[x1-1][y2] + sum_ls[x1-1][y1-1]        
        print(res)
        
if __name__ == '__main__':
    main()