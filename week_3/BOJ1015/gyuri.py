import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    A = []
    for i in range(n):
        A.append((a[i], i))
    A.sort()

    P = [0] * n
    for new in range(n):
        val, origin = A[new]
        P[origin] = new

    
    print(" ".join(map(str, P)))


if __name__=="__main__":
    main()