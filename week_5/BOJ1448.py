import sys

def triangle(length):
    length = sorted(length, reverse=True)
    for i in range(len(length)-2):
        if length[i] < (length[i+1] + length[i+2]):
            return length[i]+length[i+1]+length[i+2]
    return -1
    
def main():
    n = int(sys.stdin.readline().strip())
    length = []
    for _ in range(n):
        length.append(int(sys.stdin.readline().strip()))
    print(triangle(length))

if __name__=='__main__':
    main()
