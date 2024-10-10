import sys
input = sys.stdin.readline

def main():
    n = int(input())
    data = list(map(int, input().split()))
    result = [1 for _ in range(n)]

    result[0] = data[0]
    for i in range(1, n):
        for j in range(i):
            if data[j] < data[i]:
                result[i] = max(result[i], result[j]+data[i])
            else:
                result[i] = max(result[i], data[i])
    return max(result)

if __name__ == "__main__":
    print(main())