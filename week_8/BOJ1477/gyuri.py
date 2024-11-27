import sys
input = sys.stdin.readline

def main():
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))

    data = [0] + data + [L]
    data.sort()
    
    start, end = 1, L 
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2 
        needed = 0
        for i in range(1, len(data)):
            dist = data[i] - data[i - 1]
            if dist > mid:
                needed += (dist - 1) // mid  
        if needed > M:
            start = mid + 1  
        else:
            answer = mid
            end = mid - 1 
    
    print(answer)

if __name__ == "__main__":
    main()
