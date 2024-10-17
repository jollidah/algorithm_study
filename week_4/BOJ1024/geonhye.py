# 수열의 합 / 45m

from collections import deque
import sys
input = sys.stdin.readline

def main(): 
    N, L = map(int, input().split())

    l = L
    while l <= 100:
        # 중간에 박기
        mid = N // l
        dq = deque([mid])
        attach_cnt = l - 1

        # 왼쪽 오른쪽
        left_num = mid - 1
        right_num = mid + 1
        for i in range(attach_cnt):
            if i % 2 == 0:
                dq.appendleft(left_num)
                left_num -= 1
                if left_num < -1:
                    break
            else:
                dq.append(right_num)
                right_num += 1
        if sum(dq) == N:
            return ' '.join(map(str, dq))

        dq = deque([mid])
        # 오른쪽 왼쪽
        left_num = mid - 1
        right_num = mid + 1
        for i in range(attach_cnt):
            if i % 2 == 0:
                dq.append(right_num)
                right_num += 1
            else:
                dq.appendleft(left_num)
                left_num -= 1
                if left_num < -1:
                    return -1
        if sum(dq) == N:
            return ' '.join(map(str, dq))

        l += 1
    return -1

if __name__ == '__main__':
    print(main())