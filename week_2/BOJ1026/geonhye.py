# 보물 / 25m
import sys

def main():
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))

    A.sort()

    res = 0
    for i in range(N):
        res += A[i] * max(B)
        B.remove(max(B))
    print(res)

if __name__ == "__main__":
    main()