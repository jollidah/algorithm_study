import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        a = list(map(int, input().strip()))
        data.append(a)

    MAX = 1
    for i in range(n):
        for j in range(m):
            for size in range(1, min(n, m)):
                if i + size < n and j + size < m:
                    if data[i][j] == data[i][j + size] == data[i + size][j] == data[i + size][j + size]:
                        MAX = max(MAX, size + 1)
    print(MAX**2)


if __name__=="__main__":
    main()
