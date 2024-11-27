#42m
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    data = list(map(int, input().split()))
    cnt = int(input())
    
    for i in range(n):
        if cnt <= 0: 
            break
        
        next = i
        for j in range(i + 1, min(i + cnt + 1, n)):
            if data[j] > data[next]:
                next = j
 
        for j in range(next, i, -1):
            data[j], data[j - 1] = data[j - 1], data[j]
            cnt -= 1
            if cnt <= 0:
                break
    
    print(" ".join(map(str, data)))

main()
