n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1 
        else:    
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

result = sum(dp[n])

print(result % 10007)
