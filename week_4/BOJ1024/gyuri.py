import sys
input = sys.stdin.readline 
def main():
    N, L = map(int, input().split())
    result = -1
    for L in range(L, 101): 
        temp = N - (L * (L - 1)) // 2
        if temp % L == 0: 
            x = temp // L
            if x >= 0:
                result = [x + i for i in range(L)]
                break

    if result == -1:
        print(-1)
    else:
        print(" ".join(map(str, result)))
        
if __name__ == "__main__":
    main()
