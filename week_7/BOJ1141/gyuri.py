#25m
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(input().strip())
    cnt = 0 
    data.sort()
    for i in range(n):
        flag = False
        for j in range(i+1, n):
            if data[i] == data[j][0:len(data[i])]:
                flag = True
                break
        if not flag:
            cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()