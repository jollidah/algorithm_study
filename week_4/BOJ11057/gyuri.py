import sys 
input = sys.stdin.readline

def main():
    MOD = 10007
    n = int(input())
    dp = [1] * 10

    for i in range(n-1):
        for j in range(1, 10):
            dp[j] += dp[j-1]

    print(sum(dp) % MOD)

if __name__ == "__main__":
    main()