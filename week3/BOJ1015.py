def sort_sequence(n, a):
    a_idx = [(a[i], i) for i in range(n)]
    
    a_idx = sorted(a_idx)
    
    new = [0] * n
    for i in range(n):
        before = a_idx[i][1]
        new[i] = before
        
    return new[::-1]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    print(sort_sequence(n, a))
    
if __name__=="__main__":
    main()
