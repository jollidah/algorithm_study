#47m
#원래 짠 코드랑 좀 다름
    # #기존에 나왔던 알파벳을 나오게 하는 것이 가장 최소.
    # b_list = []
    # for i in B:
    #     if i not in b_list:
    #         b_list.append(i)
import sys

def main():
    input = sys.stdin.readline
    A, B = list(map(str, input().split()))
    nb = len(B)
    na = len(A)
    n = nb-na + 1
    MIN = float('inf')
    if n != 0:
        for i in range(n):
            cnt = 0
            for j in range(na):
                if A[j] != B[i + j]:
                    cnt += 1
            MIN = min(MIN, cnt)
    print(MIN)

if __name__ == "__main__":
    main()