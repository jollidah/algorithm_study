# 수열 정렬 / 35m

import sys
input = sys.stdin.readline

def main() :
    n = int(input().strip())
    a = list(map(int, input().split()))

    # 배열 a의 {값: 인덱스}
    a_dict = {}
    for i in range(len(a)):
        if a[i] not in a_dict:
            a_dict[a[i]] = [i]
        else:
            a_dict[a[i]].append(i)

    # b는 a의 비내림차순
    b = sorted(a)

    p = [0 for _ in range(n)]

    for i in range(len(b)):
        num = b[i]
        idx = a_dict[num][0]
        a_dict[num].pop(0)  # 중복 삭제
        p[idx] = i

    print(*p)

if __name__ == '__main__':
    main()