def sum_of_sections1(matrix, x1, y1, x2, y2):
    total = 0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            total += matrix[i][j]
    return total

def prefix(matrix, n):
    prefix_sum = [[0] * (n+1) for _ in range(n+1)]
    
    # matrix의 구간합 테이블을 계산 -> (1,1)부터 (n,n)까지 더한 값
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
    
    return prefix_sum

def sum_of_sections(prefix_sum, x1, y1, x2, y2):
    result = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    return result

def main():
    n, m = map(int, input().split()) # 표의 크기 n, 합을 구해야 하는 횟수 m
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    prefix_matrix = prefix(matrix, n)
    result = []
    
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        result.append(str(sum_of_sections(prefix_matrix, x1, y1, x2, y2)))
    
    output = "\n".join(result)
    print(output)

if __name__=="__main__":
    main()
