# 휴게소 세우기 / ?
import sys
input = sys.stdin.readline

def solution():
    # 휴게소 사이 거리를 돌며 mid값보다 큰 거리가 있을 때 거기 휴게소를 세워야함.
    start, end = 1, l-1

    res = []
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(len(store)-1):
            if store[i+1] - store[i] > mid:
                # 해당 구간에 cnt개의 휴게소를 지을 수 있음
                cnt += (store[i+1] - store[i] -1) // mid

        # 구해진 mid값이 너무 작음
        if cnt > m:
            start = mid + 1
        # 구해진 mid값이 큰 문제(계속해서 최적값을 찾아야함)
        else:
            res.append(mid)
            # res = mid
            end = mid - 1
    return min(res)

if __name__ == "__main__":
    n, m, l = map(int, input().rstrip().split())
    store = [0] + sorted(list(map(int, input().rstrip().split()))) + [l]
    print(solution())