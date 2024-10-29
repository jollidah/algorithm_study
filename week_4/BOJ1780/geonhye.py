# 종이의 개수 / 40m

import sys
input = sys.stdin.readline

n = int(input().strip())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

# -1, 0, 1
res = [0, 0, 0]

def solution(x, y, n):
    global res
    num = ls[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != ls[i][j]:
                # 같은 크기의 9개로 자르기 위한 사이즈
                cut_n = n // 3
                
                # cut_n 사이즈로 9개 자르기
                solution(x, y, cut_n) 
                solution(x + cut_n, y, cut_n) 
                solution(x + (cut_n*2), y, cut_n) 
                solution(x, y + cut_n, cut_n) 
                solution(x, y+ (cut_n*2), cut_n) 
                solution(x + cut_n, y + cut_n, cut_n) 
                solution(x + cut_n, y + (cut_n*2), cut_n) 
                solution(x + (cut_n*2), y + cut_n, cut_n) 
                solution(x + (cut_n*2), y + (cut_n * 2), cut_n) 
                return 
    res[num + 1] += 1

def main():
    solution(0, 0, n)
    print(*res)

if __name__ == '__main__':
    main()