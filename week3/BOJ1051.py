def find_square(n, m, matrix):
    max_size = 1
    size = min(n, m)
    
    for x in range(size):
        for i in range(n-x):
            for j in range(m-x):
                if matrix[i][j] == matrix[i+x][j] == matrix[i][j+x] == matrix[i+x][j+x]:
                    max_size = max(max_size, x+1)

    return max_size**2
            

def main():
    n, m = map(int, input().split())
    
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    print(find_square(n, m, matrix))

if __name__=="__main__":
    main()
