def check(paper, x, y, n, counts):
    first = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != first:
                size = n // 3
                for dx in range(3):
                    for dy in range(3):
                        check(paper, x + dx * size, y + dy * size, size, counts)
                return
    
    counts[first + 1] += 1 

def main():
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    counts = [0, 0, 0] 
    check(paper, 0, 0, n, counts)
    print(counts[0]) 
    print(counts[1]) 
    print(counts[2]) 

if __name__ == "__main__":
    main()
