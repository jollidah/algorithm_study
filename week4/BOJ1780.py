# divide&conquer,  1h 시도하고 검색

minus_one = 0
zero = 0
plus_one = 0

def same_num(matrix, a, b, n):
    global minus_one, zero, plus_one
    
    num = matrix[a][b]
    same = True
    
    for i in range(a, a+n):
        for j in range(b, b+n):
            if matrix[i][j] != num:
                same = False
                break
            
    if same == True:
        if num == -1:
            minus_one += 1
        elif num == 0:
            zero += 1
        else:
            plus_one += 1
    
    else:
        size = n//3
        for i in range(3):
            for j in range(3):
                same_num(matrix, a+i*size, b+j*size, size)
                


def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    global minus_one, zero, plus_one
    
    same_num(matrix, 0, 0, n)
    
    print(minus_one)
    print(zero)
    print(plus_one)
    

if __name__=="__main__":
    main()
