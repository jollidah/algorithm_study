def increasing_seq(n, sequence):
    dp = [0] * n
    dp[0] = sequence[0]
    
    for i in range(n):
        for j in range(n):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], sequence[i] + dp[j])
            else:
                dp[i] = max(dp[i], sequence[i])
    
    return(max(dp))


def main():
    n = int(input())
    seq_input = input() #input 받는 방법 찾아봄
    seq = list(map(int, seq_input.split()))
    
    print(increasing_seq(n, seq))

if __name__=="__main__":
    main()
